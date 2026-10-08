---
name: morning-prayer
description: Use when generating the student's optional Morning Prayer - a short, personal prayer delivered at 6 am as Piper TTS audio plus text, shaped by their goals, their week, their worries, and the Scriptures they are reading. Every verse is quoted from the profile's Bible files.
version: 1.0.0
author: Build with Jesus Agent contributors
license: MIT
platforms:
- linux
- macos
- windows
metadata:
  hermes:
    tags:
    - buildwithjesus
    - prayer
    - piper
    - tts
    - cron
    - scripture
    related_skills:
    - morning-minute
    - night-passage
    - agent-onboarding
    - eight-essentials-curriculum
    - setup-walkthrough
---
# Morning Prayer

The **Morning Prayer** is an optional rhythm for a student who
follows Jesus: a short, personal prayer delivered at 6 am (or the
time the student chose) as **audio + text** in their channel
(Telegram or WhatsApp). The point is to start the day with God
before the feed.

The prayer is **dynamic**: it is written fresh every morning from
the student's real life - their goals, what happened in the last
day or two, what weighs on them, and the Scriptures they are
reading. It is never a template with a name dropped in.

**Prerequisites.** The student is a Christian - a young person or
an adult (or has explicitly asked for this rhythm). The `language` memory key
is set, Piper is installed with a chosen voice, the delivery
channel works, and the profile's Bible files live in `bible/`
(see `bible/README.md`).

## Input contract

Before writing, gather:

1. **The tailoring keys** (Mnemosyne): `student_age`,
   `focus_goal`, `interests`, `location`, `blocker`,
   `off_limits`. Calibrate the language to the student's age;
   honour `off_limits` silently.
2. **What they are up to** - the last one or two Afternoon
   Check-In summaries and the current essential of the week, so
   the prayer can bless the actual work of their week.
3. **What weighs on them** - anything the student has shared
   recently: a worry, a test, a hard conversation, a hope. Weave
   in one or two touches, lightly. This is a prayer, not a
   status report; never lecture about a blocker.
4. **The Scriptures they are reading** - read the `reading`
   memory key if set ("I'm reading Romans"). If not set, use
   the current essential's passage. If neither, pick a verse
   that speaks to what they shared.
5. **The prayer archive** -
   `~/.hermes/profiles/buildwithjesus-agent/morning-prayer-archive.md`.
   Check the verses used in the last ~14 entries and choose one
   that has not appeared. The archive is the source of truth;
   search the whole file before settling on a verse.

## Step 0 - Load credentials

Cron runs in a fresh subprocess with no chat context. **Load the
profile `.env` into `os.environ` exactly as `morning-minute`,
Step 0, does - before anything else.** Check the same required
keys, then proceed.

## Step 1 - Choose the day's verse, from the profile's Bible

The verse must be copied from the profile's Bible files:
`bible/WEB.pdf` (default - plain modern English), `bible/KJV.pdf`,
or `bible/ASV.pdf`.

- Open the file with `read_file` - the text layer extracts, and
  the `offset` parameter pages through it. Find the verse, then
  **copy it exactly as written**, punctuation included.
- Keep the quote inside ONE translation and **name the
  translation with the quote**: "... (WEB)".
- **Never quote from memory.** If the file cannot be read -
  missing, moved, unreadable - give the reference only, and say
  plainly that the files could not be opened. This is the
  standing Scripture rule in SOUL.md, not a preference.
- If lookups feel slow on the student's machine, the agent may
  keep a plain-text extraction of one translation in
  `~/.hermes/profiles/buildwithjesus-agent/bible-cache/` (the
  same public-domain text). The rule does not change: one
  translation per quote, translation named, and anything you
  quote exactly as the files hold it.
- In cron context, shell extraction is not available: piped
  commands (`pdftotext | grep`, long one-liners) are blocked and
  `/tmp` does not exist on Windows. `read_file` on the PDFs is the
  route — it is what the verified field runs used.

## Step 2 - Write the prayer (~120 to ~200 words)

Read it aloud as you draft it, because Piper will read it aloud
too. Shape:

- **Greeting** (one line): to God, in the student's own voice.
  Calibrate to age - a 13-year-old and a 22-year-old do not
  pray the same sentence.
- **The Word** (2 to 4 lines): the day's verse, quoted with the
  reference read naturally, then one short sentence praying
  through it.
- **Their week** (3 to 6 lines): the actual life - a goal they
  set, what happened yesterday, one worry held gently.
  Specific enough to be theirs; light enough to read before
  school.
- **The build** (1 to 2 lines): the Build with Jesus thread -
  learning, making, giving. One line that carries the student's
  real building into the prayer, in their own voice: a project,
  a skill, homework, something they are making for someone. Ask
  God's help to build well and to give gladly. Natural, never a
  slogan; it should sound like their life, because it is.
- **Others** (1 to 2 lines): family, friends, their church,
  their community - one of these, not all.
- **Close**, exactly: `In the name of the Father, and of the
  Son, and of the Holy Spirit. Amen.`

Tone: warm, plain, short sentences. No fear. No doom. Never
promise an outcome ("everything will be fine") - ask for
strength and presence instead. No moralising; the prayer
trusts, it does not instruct. Every prayer carries one line of
the Build with Jesus thread - learn, build, give - woven in,
never recited.

If the student is going through something serious (a loss, a
family crisis, health), keep the prayer simple and steady, and
add a gentle line pointing them to a trusted adult - a parent,
a pastor, their church family.

## Step 3 - Pre-clean the text for TTS

Same rules as `morning-minute`, Step 3: strip em dashes
(replace with commas), rewrite references as natural speech
("Philippians 4:6-7" becomes "Philippians, chapter four, verses
six and seven"), spell out abbreviations, sentence-end every
line, drop any Markdown. Save the canonical text to
`~/.hermes/profiles/buildwithjesus-agent/morning-prayer-today.txt`.

## Step 4 - Piper TTS

Use the exact verified Piper pattern from `morning-minute`,
Step 4 (native `piper.exe`, the voice table, the MSYS path
pitfall), with the student's `piper_path` and `piper_voice_path`
from onboarding. Write the audio to
`~/.hermes/profiles/buildwithjesus-agent/morning-prayer-today.wav`.
If the household recorded `tts_fallback: edge` at onboarding, use
the recorded fallback voice and say so in the archive.

## Step 5 - Convert to OGG

```bash
ffmpeg -y -hide_banner -loglevel error \
  -i "morning-prayer-today.wav" -c:a libopus -b:a 24k \
  "morning-prayer-today.ogg"
```
Sanity check: ~90 to ~180 seconds of audio. Under a minute
suggests the TTS input was truncated.

## Step 6 - Publish to here.now (archival)

Same publish flow as `morning-minute`, Step 6 - the day's audio
stays at a stable URL. Remote path:
`buildwithjesus/morning-prayer-YYYY-MM-DD.ogg`.

## Step 7 - Deliver in the channel

Same delivery pattern as `morning-minute`, Step 7: Telegram
voice bubble via multipart `sendVoice`, then the prayer text as
a `sendMessage` below it; WhatsApp via the bridge's media
endpoint with the text after. When delivering manually in chat,
put `MEDIA:<public-url>` on its own line above the text. Never
deliver only one of the two: the student is meant to hear it
and read it.

The text body: a one-line greeting ("Good morning, <name>.
Here's today's prayer."), the title `Morning Prayer - <Weekday,
date>`, the verse reference, then the full prayer.

## Step 8 - Archive

Save each day's prayer to
`~/.hermes/profiles/buildwithjesus-agent/morning-prayer-archive.md`:

```markdown
## 29 September 2026
**Verse:** Psalm 23:1-3 (WEB)
**Reads:** <one line: what the prayer carried today>

<full prayer text>

[Listen](morning-prayer-2026-09-29.ogg)

---
```

The archive gives the student (and a parent or mentor) a record,
and gives tomorrow's run its verse-dedup and continuity.

## Setting it up (onboarding, or any time)

- **During onboarding:** the "Morning Prayer schedule" question -
  see `agent-onboarding`. Default `0 6 * * *`. If the Morning
  Minute is also at 6, stagger the two (prayer at 6:00, minute
  at 6:15, or the other way round - the student chooses).
- **Any time after:** when the student asks ("set up my morning
  prayer"), confirm the time and frequency, then create the job:

```python
cronjob(
    action="create",
    schedule="0 6 * * *",
    name="Morning Prayer",
    prompt="""You are running the student's Morning Prayer for
    today. Use the morning-prayer skill. The student's language
    is read from the language memory key - write everything in
    it. The voice is <voice path from setup>. The delivery
    channel is <telegram/whatsapp>. Gather the student's goals,
    recent check-ins and what they are reading; choose a verse
    from the profile's Bible files and quote it exactly with the
    translation named (never from memory); write the prayer, run
    Piper TTS, convert to OGG, deliver as audio + text. Do not
    write memories or ask for credentials. Deliver only the
    final response with the audio and the prayer text.""",
    enabled_toolsets=["file", "terminal", "tts"],
)
```

Manage, pause or change it with `cronjob(action="list"/"update"/
"pause")` - see `agent-onboarding`, "Managing existing jobs".

## Pitfalls

- **Only on an explicit request.** A prayer is a Christian practice;
  create this job only when the student asks for this rhythm.
- **Never quote from memory.** From the `bible/` files, exactly,
  translation named. Hard rule.
- **Repeating verses.** Search the whole archive before
  settling, not just the tail.
- **Doom tone.** The student may be anxious; the prayer lowers
  the temperature - no fear, no warnings, no prophecy.
- **Length creep.** Over ~200 words the audio runs past three
  minutes. Cut.
- **Language.** Intro, prayer and audio all go out in the
  `language` memory key.
- **Em dashes in TTS input** become commas.
- **Telegram send timeout.** Generate and archive regardless;
  when the push fails, deliver manually in chat with `MEDIA:`.
- **MSYS path mangling** with piper and python - native
  `C:\...` paths (see `morning-minute`, Step 4).

## Related skills

- `night-passage` - the evening reading that closes the day.
- `morning-minute` - the plan that follows; both can share the
  6 am hour, staggered.
- `agent-onboarding` - hosts the setup questions and job
  management.
- `setup-walkthrough` - Piper install and voice pick.
