# The Bible in this profile

This folder is the profile's Scripture store: the source the agent
grounds every Bible quote in. It is an addition to the agent's
knowledge — read on demand with the file tools, and treated as the
only text the agent quotes Scripture from.

| File | Translation | Pages | Notes |
|---|---|---|---|
| `KJV.pdf` | King James Version (1769) | 1,704 | Public domain in the US; Crown rights apply in the UK. Includes the Apocrypha, as the historic edition carries it. |
| `WEB.pdf` | World English Bible | 1,566 | Public domain. Plain modern English — the agent's default for explaining. Includes the Apocrypha. |
| `ASV.pdf` | American Standard Version (1901) | 1,453 | Public domain. The 66 books, formal and more literal. |

Sources: ebible.org. Kept as unmodified PDFs with a real text layer
(not scans), so `read_file` extracts the text and the agent can check
any passage before it speaks.

## The rule the agent follows

SOUL.md carries it strictly: every Scripture quote is copied from
these files, exactly as written, with the translation named, and never
from model memory. If a file cannot be read, the agent says so and
gives the reference, rather than reciting from memory.

## Working with these files

- To find a passage, search the extracted text, or page through with
  `read_file` (the `offset` parameter walks the text).
- To print them: they are print-format PDFs, ready as they are.
- To swap in another translation: drop a text-layer PDF into this
  folder and update the list in SOUL.md and this file. A word of care:
  most modern translations (NIV, ESV, NLT, NASB, CSB and so on) are
  copyrighted. Fine for a student's personal copy; not fine to
  redistribute in this repo or ship with the product. Keep the shipped
  set to public-domain editions.

## Optional: semantic search

If a student wants instant lookup across the whole Bible, ask the
agent to set up local document search over this folder (for example
the Hermes `qmd` skill, or a memory provider that ingests documents).
The files and the rule stay the same either way.
