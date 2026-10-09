---
name: night-passage
description: Use when generating the student's optional Night Passage - a Bible passage read aloud (Piper TTS) and delivered at 8:30 pm as audio plus text: chosen to speak to their week, their worries and where they are up to in their reading. Every passage is quoted from the profile's Bible files.
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
    - scripture
    - piper
    - tts
    - cron
    related_skills:
    - morning-prayer
    - morning-minute
    - afternoon-checkin
    - agent-onboarding
    - setup-walkthrough
    - solo-bible-walk
---
# Night Passage

The **Night Passage** is an optional rhythm: a short passage of
the Bible, read aloud and delivered at 8:30 pm (or the student's
chosen evening time) as **audio + text** in their channel. It
exists for one reason, plainly: at night a phone can become a
pit. The Night Passage gives the student a better thing to end
the day on - a few verses, a voice reading them, and a line to
fall asleep with. It is a full stop for the day, in place of the
scroll.

The passage is **dynamic**: chosen every evening from the
student's real state - what they are carrying, where their
reading has reached, and what happened recently - and always
quoted exactly from the profile's Bible files, with the
translation named.

**Prerequisites.** Piper installed with a chosen voice, the
`language` memory key set, the delivery channel working, and the
Bible files present in `bible/`.

## Input contract

1. **Tailoring keys** (Mnemosyne): `student_age`, `focus_goal`,
   `interests`, `location`, `blocker`, `off_limits`. Honour
   `off_limits` silently.
2. **Today's picture**: the last one or two Afternoon Check-In
   summaries, the current essential, and anything the student
   said about tomorrow - the passage should speak to the week
   they are actually having.
3. **What weighs on them**: worries and blockers shared
   recently. The passage answers this week's actual weight,
   gently - a night's reading never diagnoses, never lectures.
4. **Where their reading is up to**: memory keys `reading` and
   `night_passage_position` (for example "John 5"). If the
   student is following their own book, **continue it**, six to
   twelve verses a night. If there is no plan, default to a
   steady walk through one Gospel (suggest John; Mark for a
   faster story) - and break the walk when the week calls for a
   specific passage, for example a Psalm of comfort after a hard
   day.
5. **The archive**:
   `~/.hermes/profiles/buildwithjesus-agent/night-passage-archive.md`.
   Do not repeat a passage used in the last ~14 entries.

## Solo mode (read the `solo_mode` memory key)

When `solo_mode` is true, tonight's passage is the next stop on the
**Bible Walk** (see `solo-bible-walk`): continue from
`solo-walk-archive.md`, quote exactly as always, and keep the night's
peace-first rules. The walk reading is the night's content; the
framing and closing stay the same. If the student asks questions
about the passage, answer by the walk's contract: text only, labelled
sense lines, "the text doesn't say" when it doesn't.

## Step 0 - Load credentials

Same as `morning-minute`, Step 0: load the profile `.env` into
`os.environ` before anything else.

## Step 1 - Choose the passage (6 to 12 verses)

- **Peace and light only at night.** Choose passages that
  comfort, steady or give courage. Do NOT choose end-times
  visions, judgment scenes or heavy violence for an 8:30 pm
  reading. The whole point is a student sleeping better.
- Match the state. Starting points, not a playlist: anxious -
  peace (John 14:25-27; Psalm 23; Philippians 4:4-7);
  discouraged - courage (Joshua 1:5-9; Psalm 121); ashamed -
  grace (Romans 8:31-39; 1 John 1:5-9); scattered - wisdom
  (Psalm 1; Proverbs 3:1-8); grateful - thanks (Psalm 100;
  Colossians 3:12-17); waiting - patience (Psalm 130;
  Lamentations 3:21-26). Pick fresh ones - the archive will
  tell you what has been used.
- If the student follows their own plan (for example reading
  Romans), continue their book, and record the new position in
  the `night_passage_position` memory key at setup time - the
  cron run itself does not write memory, so read the key and
  keep continuity from the archive instead.

Then copy the passage **exactly** from the profile's Bible
files (`bible/WEB.pdf` default; KJV and ASV available): open
with `read_file`, page with `offset`, copy it as written,
punctuation included. One translation per reading, translation
named with the reference. **Never from memory** - if the files
cannot be read, say so plainly and give the reference only.
This is SOUL.md's standing rule.

## Step 2 - Write the framing (~40 to ~90 words around the passage)

- **Opening** (one line, spoken): "A passage for tonight,
  <name>." Then the reference, in natural speech terms.
- **The passage** itself: read as it is. No interruptions, no
  commentary between verses.
- **Closing** (one or two lines): a gentle question or a
  blessing to fall asleep on, then a plain, unhurried sign-off
  in the spirit of: "Put the phone down now. Goodnight,
  <name>." Write it fresh each night; keep it kind and short.

Tone: quiet, steady, unhurried. No moralising, no homework, no
fear. The Night Passage is a reading, a breath and a full stop -
it never gives an action plan (that is the Morning Minute's job).

## Step 3 - Pre-clean the text for TTS

Same rules as `morning-minute`, Step 3 (em dashes to commas,
natural-speech references, no Markdown, full stops). Save the
canonical text to
`~/.hermes/profiles/buildwithjesus-agent/night-passage-today.txt`.

**Overwrite safety:** if the file already exists, read it first
with `read_file`, then save. A blind overwrite is refused by the
write guard and silently leaves yesterday's text in place.

## Step 4 - Piper TTS

The same verified pattern as `morning-minute`, Step 4. Write
`~/.hermes/profiles/buildwithjesus-agent/night-passage-today.wav`.

## Step 5 - Convert to OGG

```bash
ffmpeg -y -hide_banner -loglevel error \
  -i "night-passage-today.wav" -c:a libopus -b:a 24k \
  "night-passage-today.ogg"
```
Sanity check: ~60 to ~150 seconds typical. Under 45 seconds
suggests truncation.

## Step 6 - Publish to here.now (archival)

Same flow as `morning-minute`, Step 6. Remote path:
`buildwithjesus/night-passage-YYYY-MM-DD.ogg`.

## Step 7 - Deliver in the channel

Same delivery pattern as `morning-minute`, Step 7: Telegram
voice bubble via multipart `sendVoice`, then the text as a
`sendMessage` below; WhatsApp via the bridge. The text body:
the opening line, the passage with its reference, the closing
line. When delivering manually in chat, `MEDIA:<public-url>` on
its own line above the text.

## Step 8 - Archive

Save each night to
`~/.hermes/profiles/buildwithjesus-agent/night-passage-archive.md`:

```markdown
## 29 September 2026
**Passage:** John 5:1-15 (WEB)
**Why:** <half a line: "continuing John" or "a hard week - a Psalm of trust">

<opening line, passage, closing line>

[Listen](night-passage-2026-09-29.ogg)

---
```

The archive carries continuity (what was read, where the walk
has reached) and the dedup window.

## Setting it up (onboarding, or any time)

- **During onboarding:** the "Night Passage schedule" question -
  see `agent-onboarding`. Default `30 20 * * *` (8:30 pm). Keep
  at least half an hour between it and the Planning Session
  (9 pm default).
- **Any time after:** when the student asks ("set up my nightly
  Bible reading"), confirm the time and frequency, then create
  the job:

```python
cronjob(
    action="create",
    schedule="30 20 * * *",
    name="Night Passage",
    prompt="""You are running the student's Night Passage for
    tonight. Use the night-passage skill. The student's language
    is read from the language memory key - write everything in
    it. The voice is <voice path from setup>. The delivery
    channel is <telegram/whatsapp>. Continue their current
    reading from the archive; pick a passage that speaks to
    their week - peace and light only, never heavy passages at
    night; quote it exactly from the profile's Bible files with
    the translation named (never from memory); run Piper TTS,
    convert to OGG, deliver as audio + text. Do not write
    memories or ask for credentials. Deliver only the final
    response with the audio and the text.""",
    enabled_toolsets=["file", "terminal", "tts"],
)
```

## Pitfalls

- **Heavy passages at night.** Never a judgment scene or an
  end-times vision at bedtime. Peace, courage, comfort, hope.
- **Never quote from memory.** Exactly as the `bible/` files
  hold it, translation named.
- **Repeats and stalled reading.** Check the archive; keep the
  walk moving (or note deliberately re-reading a loved Psalm -
  but not within the ~14-night window).
- **Duplicating the Morning Minute.** No action plans, no
  teaching summary - a reading, a breath, a full stop.
- **Doom tone or guilt.** If the student missed days, no
  mention; the next passage simply arrives.
- **Language, em dashes, send timeouts, MSYS paths** - as
  `morning-prayer`.

## Related skills

- `morning-prayer` - the morning bookend; same rules and craft.
- `morning-minute` - hosts the shared mechanics (Piper, here.now,
  channel delivery).
- `afternoon-checkin` and `planning-session` - its neighbours in
  the evening.
- `agent-onboarding` - hosts the setup question and job
  management.
