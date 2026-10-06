#!/usr/bin/env python3
"""fetch_edition.py - one-time download of a student's Scripture edition.

Usage:
    python bible/fetch_edition.py <language-code>     # e.g. es, tl, zh, vi, ja, ko, id
    python bible/fetch_edition.py --list

Reads bible/editions.json, downloads the freely-licensed "verse per
line" text from eBible.org, converts the book codes to readable book
names, and writes bible/<language-code>/<edition-id>.txt with a
licence header. Idempotent: re-running with the same edition says
"up to date"; a different content hash is reported as an upstream
change.

Only editions listed in editions.json are fetchable, and only
public-domain or freely-licensed editions belong there. English ships
separately as PDFs in bible/ (KJV, WEB, ASV) and is not fetched.
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys
import urllib.request
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent
REGISTRY = ROOT / "editions.json"
BASE = "https://ebible.org/Scriptures/{id}_vpl.zip"
UA = {"User-Agent": "Mozilla/5.0 (buildwithjesus-agent; bible/fetch_edition.py)"}

BOOKS = {
    "GEN": "Genesis", "EXO": "Exodus", "LEV": "Leviticus", "NUM": "Numbers",
    "DEU": "Deuteronomy", "JOS": "Joshua", "JDG": "Judges", "RUT": "Ruth",
    "1SA": "1 Samuel", "2SA": "2 Samuel", "1KI": "1 Kings", "2KI": "2 Kings",
    "1CH": "1 Chronicles", "2CH": "2 Chronicles", "EZR": "Ezra",
    "NEH": "Nehemiah", "EST": "Esther", "JOB": "Job", "PSA": "Psalms",
    "PRO": "Proverbs", "ECC": "Ecclesiastes", "SNG": "Song of Songs",
    "ISA": "Isaiah", "JER": "Jeremiah", "LAM": "Lamentations",
    "EZK": "Ezekiel", "DAN": "Daniel", "HOS": "Hosea", "JOL": "Joel",
    "AMO": "Amos", "OBA": "Obadiah", "JON": "Jonah", "MIC": "Micah",
    "NAM": "Nahum", "HAB": "Habakkuk", "ZEP": "Zephaniah", "HAG": "Haggai",
    "ZEC": "Zechariah", "MAL": "Malachi", "MAT": "Matthew", "MRK": "Mark",
    "LUK": "Luke", "JHN": "John", "ACT": "Acts", "ROM": "Romans",
    "1CO": "1 Corinthians", "2CO": "2 Corinthians", "GAL": "Galatians",
    "EPH": "Ephesians", "PHP": "Philippians", "COL": "Colossians",
    "1TH": "1 Thessalonians", "2TH": "2 Thessalonians", "1TI": "1 Timothy",
    "2TI": "2 Timothy", "TIT": "Titus", "PHM": "Philemon", "HEB": "Hebrews",
    "JAS": "James", "1PE": "1 Peter", "2PE": "2 Peter", "1JN": "1 John",
    "2JN": "2 John", "3JN": "3 John", "JUD": "Jude", "REV": "Revelation",
}
LINE_RE = re.compile(r"^([A-Z0-9]{3}) (\d+:\d+)(?:\s(.*))?$")
TAG_RE = re.compile(r"<[^>]+>")

# Alternate USFM-style codes used by some editions, mapped to the canonical set.
ALIASES = {
    "1JO": "1JN", "2JO": "2JN", "3JO": "3JN", "EZE": "EZK", "JAM": "JAS",
    "JOE": "JOL", "JOH": "JHN", "MAR": "MRK", "NAH": "NAM", "PHI": "PHP",
    "SOL": "SNG",
}


def load_registry():
    if not REGISTRY.exists():
        sys.exit("editions.json not found next to this script")
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def list_editions(reg):
    print("Freely-licensed Scripture editions (fetch at onboarding):")
    for code, e in reg["editions"].items():
        print("  %-8s %-42s %s" % (code, e["id"] + "  " + e["name"], e.get("status", "")))
    print("\nEnglish ships as PDFs in bible/ (KJV, WEB, ASV).")


def licence_line(about_html: str) -> str:
    text = TAG_RE.sub(" ", about_html)
    text = re.sub(r"\s+", " ", text)
    for kw in ("public domain", "creative commons", "copyright", "license", "licence"):
        idx = text.lower().find(kw)
        if idx != -1:
            return text[max(0, idx - 40): idx + 220].strip()
    return "(licence text not found in about page - check ebible.org details page)"


def fetch(code, reg, force=False):
    entry = reg["editions"].get(code)
    if not entry:
        sys.exit("No registry entry for '%s'. Add it to bible/editions.json first." % code)
    eid = entry["id"]
    url = BASE.format(id=eid)
    print("Fetching %s ..." % url)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r:
        blob = r.read()
    sha = hashlib.sha256(blob).hexdigest()
    print("  downloaded %.1f MB | sha256 %s" % (len(blob) / 1e6, sha[:16]))

    with zipfile.ZipFile(__import__("io").BytesIO(blob)) as z:
        names = z.namelist()
        txt_name = next((n for n in names if n.endswith("_vpl.txt")), None)
        about_name = next((n for n in names if n.endswith("_about.htm")), None)
        if not txt_name:
            sys.exit("No _vpl.txt inside the zip: %s" % names)
        raw = z.read(txt_name).decode("utf-8-sig", "replace")
        about = z.read(about_name).decode("utf-8", "replace") if about_name else ""

    lic = licence_line(about) if about else "(no about page in zip)"
    out_lines, books, verses, unknown = [], set(), 0, set()
    for ln in raw.splitlines():
        m = LINE_RE.match(ln.strip())
        if not m:
            continue
        code3, ref, text = m.group(1), m.group(2), (m.group(3) or "").strip()
        code3 = ALIASES.get(code3, code3)
        if code3 not in BOOKS:
            unknown.add(code3)
            continue
        books.add(code3)
        verses += 1
        out_lines.append("%s %s%s" % (BOOKS[code3], ref, (" " + text) if text else ""))

    if unknown:
        print("  WARNING unknown book codes skipped:", sorted(unknown))

    header = (
        "# %s\n# Language: %s | Edition id: %s\n# Source: https://ebible.org/%s/ (verse-per-line text)\n"
        "# Licence: %s\n# Source zip SHA-256: %s\n# Fetched: %s | Converted by bible/fetch_edition.py\n\n"
        % (entry["name"], code, eid, eid, lic, sha, __import__("datetime").date.today().isoformat())
    )
    dest_dir = ROOT / code
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / (eid + ".txt")
    if (not force) and dest.exists() and ("SHA-256: %s" % sha) in dest.read_text(encoding="utf-8", errors="replace"):
        print("  up to date: %s" % dest)
        return
    dest.write_text(header + "\n".join(out_lines) + "\n", encoding="utf-8", newline="\n")
    print("  wrote %s | books: %d | verses: %d" % (dest, len(books), verses))
    print("  licence: %s" % lic[:200])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("language", nargs="?", help="language code, e.g. es / tl / zh / vi / ja / ko / id")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--force", action="store_true", help="re-convert even if the source sha matches")
    args = ap.parse_args()
    reg = load_registry()
    if args.list or not args.language:
        list_editions(reg)
        return
    fetch(args.language, reg, force=args.force)


if __name__ == "__main__":
    main()
