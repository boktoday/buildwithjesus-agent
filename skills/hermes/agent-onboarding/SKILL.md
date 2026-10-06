---
name: agent-onboarding
description: Use when a new Build with Jesus Agent profile needs guided first-run setup, identity choices, the student's language for the guide and messages, tradition (Christian or Universal), morning voice and delivery channel (Telegram or WhatsApp), Piper TTS and Jina AI setup, Eight Essentials guide loading, Eight Essentials delivery order (sequential or randomised), memory preferences, and Morning Minute + Afternoon Check-In + Planning Session schedules. Plan the setup conversationally, obtain approval, apply only the selected changes, and verify every result.
version: 2.0.0
author: Build with Jesus Agent contributors
license: MIT
platforms:
- linux
- macos
- windows
metadata:
  hermes:
    tags:
    - hermes
    - onboarding
    - setup
    - buildwithjesus-agent
    - eight-essentials
    - integrations
    - tools
    - memory
    - cron
    - piper
    - jina
    - telegram
    - whatsapp
    related_skills:
    - hermes-agent
    - hermes-mnemosyne
    - morning-minute
    - afternoon-checkin
    - eight-essentials-curriculum
    - setup-walkthrough
---
# Build with Jesus Agent Onboarding

## Overview

Use this skill to turn a blank or lightly configured Build with Jesus
Agent profile into a setup chosen by its owner — the parent or
mentor setting up the profile for a young person, or the young person
themselves if they're old enough to install their own tool.

The workflow is conversational and consent-gated: learn the
identity, the student's language, the tradition (Christian or
Universal), the morning voice and delivery channel, the Piper and
Jina credentials, and the Eight Essentials guide loaded into
`essentials/`. Recommend a small
capability bundle, show the proposed changes, apply only what the
user approves, and verify the result.

This is a **capability planner**, not a blind installer. A Hermes
toolset exposes a capability, a skill provides operating
instructions, a plugin or MCP server provides an integration, and a
desktop application such as Obsidian or Notion is a separate
dependency. Explain that distinction in plain language when it
matters.

The setup must work for a public starter profile. Never assume the
student's name, age, location, timezone, family, faith, schools, or
accounts. Ask instead.

## When to use

- A new student (or parent setting up for a student) starts the
  Build with Jesus Agent profile for the first time.
- The user says "set me up," "configure my assistant," "help me get
  the morning minute working," or similar.
- The user wants to choose their language, tradition, voice,
  delivery channel, Piper/Jina setup, or load the Eight Essentials
  guide.
- The user asks to add or change the Morning Minute, the Build with Jesus
  Check-In, or any other recurring job.
- The user asks to review or change an existing starter setup.

**Don't use for:**

- Installing Hermes itself or repairing the Hermes runtime; use
  `hermes-agent`.
- Diagnosing an already configured integration; load the matching
  integration or troubleshooting skill.
- Promoting the Build with Jesus Agent course, taking payment, or handling
  subscription access — that lives in the product itself, not here.
- Making medical, legal, or financial decisions on the student's
  behalf.
- Creating a cron job from an incomplete request when the delivery
  destination, schedule, or content would be ambiguous.

## Operating rules

1. Ask one small group of related questions at a time. Don't
   present a forty-item questionnaire.
2. Start with identity, language, and tradition, then move to the
   four product-specific setups (Piper, Jina, channel, guide). Don't
   ask users to choose toolset names they have never seen.
3. Explain what will happen before it happens. No installation,
   account connection, credential request, or persistent cron
   creation without explicit approval.
4. **Never ask the user to paste a password, API key, OAuth code,
   payment information, or private token into chat.** Use the
   provider's official setup flow and pause at the credential gate.
5. Read-only discovery is allowed before approval when it does not
   access private account content. Don't silently read connected
   accounts, note vaults, calendars, or mailboxes.
6. Keep setup choices local to the active profile. Don't edit
   another Hermes profile or global configuration unless the user
   explicitly requests that scope.
7. After a persistent toolset or provider change, tell the user
   whether a new session or gateway restart is required. Don't
   claim a new tool is available until a fresh-process check
   confirms it.
8. A cron job runs in a fresh session with no current-chat context.
   Every LLM-driven cron prompt must be self-contained.
9. **Run the orientation in the live session — don't delegate it
   to a sub-agent.** Onboarding is a conversation: each answer
   shapes the next question, and the setup actions are instant.
10. Don't put memory writes in cron prompts. Mnemosyne is
    provider-injected, not a toolset, and cron contexts
    intentionally skip Mnemosyne tools. Health responses must not
    be stored automatically.
11. Never use `enabled_toolsets: ["mnemosyne"]`; that is not a
    valid configuration. Use the `memory` provider setup for
    memory and the `cronjob` tool for schedules.
12. **For young students: bring a parent in when a setup step
    involves money, an adult service, or a long-term commitment.**
    Don't lecture; just say so plainly and offer the parent-briefing
    note.

## Phase 0 — Inspect before changing anything

Before proposing changes, inspect only the active profile:

1. Use `hermes config get onboarding` if the CLI supports the key.
   If it is absent, don't treat that as an error.
2. Use `hermes memory status` to identify the active memory
   provider and whether it is installed.
3. Use `hermes tools` to view the current toolset selection.
4. Call `cronjob(action="list")` before creating any recurring job.
5. If the user mentions a specific integration, inspect the
   installed skill inventory with `skills_list()`.
6. Confirm Piper is installed: try the test-synthesis command from
   `setup-walkthrough` Skill Step 1. This probe gates the audio
   jobs. If it fails, pause for Piper install (routes in
   `setup-walkthrough`: `pip install piper-tts`, or the release
   binary) — do not create the Morning Minute, Morning Prayer, or
   Night Passage jobs until Piper synthesizes, or until the user
   explicitly chooses the fallback below. If the household
   explicitly declines Piper, record `tts_fallback: edge` in
   profile memory, name the Edge fallback voice in the job prompts,
   and say the fallback out loud in the setup plan — the engine
   must never diverge silently.
7. Confirm the guide MD files are loaded: list
   `essentials/*/lessons/`. If any folder has only `README.md`,
   note which essential needs its chapter dropped in.

Report the starting state briefly. Don't dump credentials, full
environment files, private account data, or the entire skill
library.

## Phase 1 — Ask the human questions

Use this order, adapting to answers already given. Keep questions
plain-language.

### Identity

Ask:

- "What should I call you?" (the parent/mentor, or the student
  themselves).
- "What would you like to call me?" (default suggestion: *the
  Build with Jesus Agent*, or whatever the user prefers).
- "If the agent is for a student, what should it call them?"
- "How old is the student?" (this helps calibrate advice and
  safety gates — a 13-year-old and a 17-year-old have different
  autonomy needs).
- "Do you prefer concise, conversational, formal, or highly
  detailed replies?"

If the user skips a question, use a neutral default and say what
was assumed.

### Your language

Ask:

> "Which language would you like your guide, lessons and messages
> in?"

Offer the ten guide languages: English, Bahasa Melayu, ไทย (Thai),
Tiếng Việt (Vietnamese), Bahasa Indonesia, Filipino (Tagalog),
Español, 中文 (Chinese), 한국어 (Korean), 日本語 (Japanese). A
student who wants any other language gets it too — the agent writes
and teaches in it wherever it can; the ten are the languages with a
fully published guide edition.

What the choice changes:

- The agent writes its messages (Morning Minute text, Check-In,
  Planning Session) in this language.
- It reads the English lesson files and teaches in this language.
- It shares the student's published guide edition — read online, or
  the offline pack for no-internet reading. All ten links live in
  `essentials/guide-editions.md`.
- If the README exists in the student's language
  (`README.<code>.md`), point to it for setup reading.

Record the choice in profile memory as `language` (e.g. `ms`, `tl`,
`es`; `en` if skipped). Every skill that writes to the student reads
this key first. Do not guess a student's language from their name,
location, or tradition — ask.

### Profile and life

This is where the agent learns enough about the student to actually
tailor the work. Without this section the Morning Minute, the
check-in, and the lesson selection are all generic. With it, the
agent can recommend the local park for Nature, name a friend the
student could reach out to for Community, or notice that the
student's Body question is really a sleep question because they
mentioned late-night studying.

Ask the questions in three small groups. Do not present all ten at
once.

#### Group 1 — Basics

- "How old is the student?" (or "what year/grade are they in?").
  Used to calibrate autonomy gates — a 13-year-old and a 17-year-old
  have different autonomy needs, different activities, and
  different language. If the parent is the one answering and the
  student is older, the parent should still answer the basics so
  the agent gets them right.
- "Where do they live — city or town, and country?" Enough to
  recommend local places for Nature, set the right time zone, and
  (later) suggest meet-ups. No street address. No precise location.
- "What's the living situation — parents, siblings, or on their
  own?" Used to know when to bring a parent into a setup step (the
  parent-gate rule), and to set the right tone for the family
  briefing later.
- "What's their week look like — school, work, both, neither?" Used
  to set realistic defaults for the Morning Minute and check-in
  schedules, and to know when "weekday only" makes sense.

#### Group 2 — What they care about

- "What are they into right now? Three things, however small."
  Hobbies, sports, music, games, causes, fandoms, classes they
  actually like. The agent uses these to pick examples for every
  chapter (a Skills example that mentions the student's sport
  lands better than one that doesn't) and to suggest Body
  activities that fit the student's actual life.
- "What's one thing they want to be different about themselves in
  three months? Anything, however small." This becomes the
  student's *focus goal*. The agent picks which essential to lead
  with, which daily prompt to surface, and which activity to
  recommend. The student can change it later.
- "Who do they spend time with — friends, family, online, mostly
  alone?" Used for the Real Community chapter. The agent does
  *not* lecture about friendship. It asks one good question and
  honours the answer.

#### Group 3 — What's getting in the way (and what's off-limits)

- "What's getting in the way of the things they want? Honestly."
  This is the most useful single question. Sleep, screens, anxiety,
  a person, no money, no time, no idea where to start — the answer
  tells the agent which essential to lead with and which activity
  to skip. The agent honours the answer without diagnosing or
  lecturing.
- "Anything I should *not* bring up — topics, people, situations?"
  Stored in memory. The agent checks this before recommending any
  Scripture quote, any conversation starter, any community
  suggestion. Off-limits is honoured silently.

If a question gets skipped, use the neutral default (age → "young person",
location → "your area", and so on) and tell the student what was
assumed. Don't push. The student can fill in missing fields later by
chatting.

### Tradition (the most important early choice)

Ask:

> "Two ways to teach the Eight Essentials. Christian — Bible-
> anchored, with Scripture in the Morning Minute. Universal —
> secular, with reflection and intention in place of prayer. Which
> works for you? Or tell me your tradition and I'll build that in."

The agent will not mix traditions. If the student brings their own
tradition, keep every quote and framing accurate to it. The student
(or parent) can change later, but lessons will branch from this point.

### Piper TTS install + voice pick

Hand off to the **`setup-walkthrough` skill**. That skill walks the
user through installing Piper (or verifying the existing native
binary), picking a voice, and verifying with a test synthesis.

**Ask the student which voice they want to wake up to:**

> "Which voice should <student> wake up to each morning? Here are
> the options: US male (Joe), US female (Amy), UK male (Alan), UK
> female (Jenny Dioco), or Australian female (Natasha)."

Use the student's name, never a hardcoded example name. Don't
default to Joe silently — make the choice explicit. The voice the
student picks shapes whether they actually listen to the Morning
Minute. The five voices are the Piper catalogue (see
`setup-walkthrough` and `morning-minute` Step 4): record the chosen
voice and the two verified paths in profile memory as `piper_path`
(the binary) and `piper_voice_path` (the `.onnx` model). The audio
job prompts name those paths, not just a voice name.

The agent does NOT ask for keys or tokens in chat. It walks the
user to where they add things themselves.

### Jina AI free API key

Hand off to `setup-walkthrough` Skill Step 2. Sign up at
<https://jina.ai/>, free tier, no credit card. Verify with a real
search before moving on.

### Delivery channel

Ask:

> "Where should the Morning Minute and the Afternoon Check-In
> land? Telegram or WhatsApp?"

- **Telegram** — easier, clearer, audio player renders inline.
  Recommend for most students.
- **WhatsApp** — only if the household uses WhatsApp and not
  Telegram. Costs money per message via the official Business API,
  or requires a personal bridge (Node.js + Baileys).

Hand off to `setup-walkthrough` Skill Step 3 to walk through the
chosen channel's bot setup.

### Eight Essentials guide loading

Hand off to `setup-walkthrough` Skill Step 4. The lesson files ship
with the repo — the agent reads each `essentials/<NN-name>/lessons/`
folder and confirms the chapter is present before moving on.

Share the guide's published edition in the student's language (the
`language` key): the read-online link, and the offline pack for
households with limited internet. All ten editions' links live in
`essentials/guide-editions.md`.

If a folder is missing its chapter, say so plainly — never invent
lesson content.

### Memory

Ask whether the student already has a memory provider set up.
Recommend **Mnemosyne** (local-first, profile-scoped, no external
account) as the default. Set it up.

### Notes

Ask:

> "Does the student use a notes system — Obsidian, Notion, plain
> Markdown folders, or something else?"

If yes, ask which system and which vault or workspace they want to
connect. Don't read the vault or workspace before the user
identifies and approves it.

### The role reminder (say it at setup)

State plainly, once, in your own words: you are an assistant - a
thought partner, build partner, researcher and teacher - and **not**
a companion, and not an adviser for serious personal matters (mental
health, health, relationship crises, big decisions). When something
is bigger than a chat, you will always point the student to a real
person - a parent, a trusted adult, a leader, a counsellor - and to
helplines. One short moment, not a lecture. This is the first of the
regular reminders; the `hard-moments` skill carries the cadence.

### Family briefing (parents and guardians)

Offer the one-page family brief to the parent or guardian: what the
assistant is and is not, where every local record lives, the safety
model, and their controls - pause anything, cap spending via
`spend-log.md`, edit the helplines for their country. The repo ships
it at `FAMILY.md`; point them to it and offer to send a copy in the
chat. Ask if they want a monthly spend cap set while you are there.

### Capability boundaries

Ask only about capabilities relevant to the work:

- **Web research:** Jina search and fetch (already configured).
- **Browser automation:** broader website interaction.
- **Local files:** read and write files in approved locations.
- **Terminal:** run local commands; higher-trust.
- **GitHub:** push, pull, open issues, open PRs (for parent or
  student to track their progress).
- **Calendar, reminders, email, or other accounts:** connect only
  the specific service requested, with the user completing
  authentication.

### Toolset walkthrough

Every CLI toolset is **already enabled by default**. The walkthrough
is a review, not an install. Tell the user everything is on, then
walk each toolset in plain language and ask whether they want to
keep it or turn it off. Peel back only what they decline.

The full toolset list lives in the README's "What's loaded"
section. The agent walks it concisely, mentioning only the toolsets
relevant to the student's work (web, file, terminal, code_execution,
memory, skills, cronjob, todo, kanban, vision, tts, video, clarify).

#### Web search backend (Jina — usually configured above)

If the user already did the Jina step, the `web` toolset is wired.
If not, fall back to SearXNG or a hosted API. Verify with a real
query before calling it working.

#### Provider / model

Confirm the model provider works end-to-end. The profile defaults
to `openrouter` with `deepseek-v4-flash` — one key for a large
catalogue including free-tier and multimodal (image, audio) models.
The agent walks the user through adding the key if it isn't set.

### Morning Minute schedule

Ask for:

- Delivery time and timezone (default 6 am, student's local
  timezone).
- Whether it should run every day or only school days or only
  weekends.
- The voice (already picked in Piper step).

### Morning Prayer schedule (optional)

For a student following Jesus, offer the **Morning Prayer** — a
short personal prayer (audio + text) delivered in the morning.

Ask for:

- Whether they would like it at all (it is optional; they can add
  or drop it any time by asking).
- Delivery time and timezone (default 6 am). If their Morning
  Minute is also at 6, offer to stagger the two: prayer at 6:00
  and minute at 6:15, or the other way round.
- Whether it should run every day or only school days or only
  weekends.

### Night Passage schedule (optional)

Offer the **Night Passage** — a Bible passage read aloud (audio +
text) in the evening: a better thing to end the day on than the
scroll.

Ask for:

- Whether they would like it at all (optional; can be added or
  dropped any time).
- Delivery time and timezone (default 8:30 pm).
- Whether it should run every day or only school nights or only
  weekends.

### Eight Essentials delivery order

Ask the student (or their parent if the student is younger) how they
want the Eight Essentials to be delivered:

> "There are two ways I can serve up the Eight Essentials.
> **Sequential** — one through eight, in order, with each building on
> the last. This is the most coherent and is what the guide was
> written for. **Randomised** — drawn from any essential on any day,
> with a knowledge summary from the guide plus a daily activity,
> matched to what you seem to need that day. This is more flexible
> but each essential takes longer to land. Which works for you?"

If the student is unsure, default to **sequential**. Sequential is
the path the guide was designed for; randomised is a power-user
choice for young people who already know what they need.

Record the choice in profile memory as `essentials_order` with the
value `sequential` or `randomised`. The Morning Minute cron prompt
and the `eight-essentials-curriculum` skill both read this key.

### What the choice changes

| Mode | What the agent does |
|---|---|
| **Sequential** | Walks essentials 01 through 08 in order. Each day's Morning Minute references the previous day's essential where it makes sense. The guide's flow is preserved. Recommended for new students. |
| **Randomised** | Picks the essential for the day based on three signals: what hasn't been touched in the longest time, what the student said they were struggling with recently, and what fits the day's energy. Each Morning Minute opens with a short knowledge summary from the chosen essential's guide chapter and proposes one small activity. Best for students who already know what they need. |

In both modes, **all eight essentials are covered** — sequential
just covers them in a fixed order; randomised spreads them across
days but never skips one permanently.

The student can switch later by updating the `essentials_order`
memory key — no re-onboarding required.

### Afternoon Check-In schedule

Ask for:

- Delivery time and timezone (default 5 pm).
- Whether it should run every day or only school days or only
  weekends.

### Planning Session schedule

Ask for:

- Delivery time and timezone (default 9 pm, before bed).
- Whether it should run every day or only school days or only
  weekends.

Explain what it is: before bed, the agent drafts tomorrow's plan
(school tasks, homework deadlines, the week's essential, one
real-world thing), the student edits it, and the plan saves
locally — no app, no account, no cloud sync.

### Build projects (the project track)

Mention that the agent can guide bigger builds: a workshop project,
or a short or long project - an app, a local-first website or a
dashboard for a real need in the student's life, their church or
their community - or a real-world build from the guide's activities.
Ask whether the student would like the **Build Round** question in
the nightly Planning Session ("starting something new, keeping one
going, or finishing and giving one away"). Default: yes, asked once
a week once a project is active or an idea is waiting. The question
and the full pipeline live in the `build-project` skill - no setup
needed; it activates when a project starts.

### Token Router (optional)

Mention the optional Hermes Token Router and offer to enable it.

Explain it plainly: *"The Token Router narrows the tools the agent can use by default. It doesn't hide anything from you — you can still ask anything. It just keeps the agent from wandering into things like code execution or data analysis when you just want a conversation about the day's essential. If token usage is a concern, turn it on. If you want the full surface available, leave it off."*

See the README for the manual enable steps if the user declines.

## Phase 2 — Present the setup plan

Before applying anything, show a compact plan in this shape:

```text
Proposed setup

Identity:
- Call you: <name>
- Call the student: <student name>
- Student age: <age>
- Call me: <assistant name>
- Reply style: <style>

Language:
- Guide, lessons and messages: <language>
- Guide edition: <shared / to share after setup>

Profile:
- Student age / year: <age or year>
- Location: <city/town, country>
- Living situation: <parents / siblings / on their own>
- Week: <school / work / both / neither>
- Into right now: <3 things>
- Focus goal (3 months): <one thing to change>
- Friendship circle: <friends / family / online / mostly alone>
- Getting in the way: <honest answer or "skipped">
- Off-limits: <topics/people/situations or "none">

Tradition:
- Christian / Universal

Eight Essentials delivery:
- Sequential (1 → 8) / Randomised

Piper TTS:
- Voice: <voice name>
- Verified: <yes / no>

Jina AI:
- Key: <present in .env>
- Verified: <yes / no>

Delivery channel:
- Telegram / WhatsApp
- Verified: <yes / no>

Eight Essentials guide:
- Loaded chapters: <list of essentials with lesson files>
- Missing: <list of essentials without lesson files>

Memory:
- Mnemosyne (local-first) / <other>

Integrations:
- Obsidian / Notion / GitHub / none

Token Router:
- Enabled / Disabled

Scheduled jobs:
- Morning Minute at <time> in <timezone>, <days>
- Afternoon Check-In at <time> in <timezone>, <days>

I will not install applications, connect accounts, or create
recurring jobs until you approve this plan.
```

A clear response such as "yes," "apply it," or an equivalent
approval is required before applying persistent changes. If the
user changes one item, revise the plan and request approval again.

## Phase 3 — Apply and verify

Apply only the approved items, in this order:

1. Identity and style in the active profile.
2. Profile and life fields in the active profile memory (writes
   `student_age`, `location`, `living_situation`, `week_shape`,
   `interests`, `focus_goal`, `friendship_circle`, `blocker`,
   `off_limits`, and `language` keys in Mnemosyne).
3. Tradition in the active profile memory (writes a `tradition`
   key in Mnemosyne).
4. Piper paths in the active profile memory (`piper_path` and
   `piper_voice_path`, both from the verified setup-walkthrough
   probe — or the explicit `tts_fallback: edge` decision).
5. Jina key in `.env` (user adds it themselves; agent verifies).
6. Delivery channel credentials in `.env` (user adds them
   themselves; agent verifies with a test message).
7. Guide MD files in `essentials/<NN-name>/lessons/` (user drops
   them in; agent lists the folder to confirm).
8. Memory choice with `hermes config set` or `hermes memory setup`.
   For the recommended Mnemosyne setup: if a session shows the
   "mnemosyne declares Python dependencies" warning, install the plugin
   with its own installer and enable it with
   `hermes plugins enable hermes-mnemosyne` — full guide in the
   `hermes-mnemosyne` skill.
9. Approved skill or integration setup, pausing at all credential
   and permission gates.
10. Toolset selection through `hermes tools` if a persistent
    capability change is required.
11. Existing cron inventory with `cronjob(action="list")`.
12. New scheduled jobs using the Morning Minute and Build with Jesus
    Check-In templates below.
13. A final readback and concise status report.

After each action, verify its actual result.

If a change requires a new session, say `New session required`
rather than pretending the current context has reloaded it.

## Scheduled setup options

### Morning Minute (the daily 6 am plan)

Default schedule: `0 6 * * *` (every day at 6 am, student
timezone). Override per the student's choice.

The Morning Minute cron prompt must say:

- Use only the Eight Essentials guide MD files in
  `essentials/<NN-name>/lessons/`. Read at least one lesson per
  day. Track which lessons have been read; do not repeat within
  ~30 days.
- **Read the `essentials_order` memory key.** If `sequential`,
  walk essentials 01 through 08 in order and reference the
  previous day's essential where it makes sense. If `randomised`,
  pick today's essential based on three signals: longest gap
  since last touched, what the student said they were struggling
  with recently, and what fits the day's energy. In both modes,
  every essential must still be covered eventually.
- Stay inside the chosen tradition (Christian or Universal). Don't
  mix the two.
- **If `randomised`:** open the Morning Minute with a one-paragraph
  knowledge summary from the chosen essential's guide chapter,
  then propose one small activity for the day. The summary is
  what carries the essential's teaching on a randomised day;
  the activity is the practice.
- Generate a brief plan: the day's essential, one small action,
  and the quote or reflection. See `morning-minute` skill for the
  full contract.
- Run Piper TTS with the student's chosen voice. Convert to OGG.
  Upload to here.now for the public audio URL. Deliver inline in
  Telegram or WhatsApp with the text below.
- Archive the day's plan text to
  `~/.hermes/profiles/buildwithjesus-agent/morning-minute-archive.md`.
- Don't write memories or ask for credentials in the cron prompt.
- Don't use Mnemosyne tools from the cron context.

Example creation call after approval:

```python
cronjob(
    action="create",
    schedule="0 6 * * *",
    name="Morning Minute",
    prompt="""You are running the student's Morning Minute for today.
        Use the morning-minute skill. The student's tradition is
        <christian/universal>. The essentials delivery order is
        <sequential/randomised> — read this from the essentials_order
        memory key, not from this prompt. The voice is <piper voice model path>, binary at <piper binary path>.
        The student's language is read from the language memory key —
        write all student-facing text in it.
        The delivery channel is <telegram/whatsapp>. Generate the day's
        plan, run Piper TTS, upload to here.now, deliver inline. Do
        not write memories or ask for credentials. Deliver only the
        final response with the audio and the plan text.""",
    enabled_toolsets=["file", "terminal", "tts"],
)
```

The actual Morning Minute skill (`skills/hermes/morning-minute/`)
contains the full contract — read it before generating.

### Morning Prayer (optional, 6 am)

Default schedule: `0 6 * * *`. If the Morning Minute keeps the
6 am slot, stagger the two (for example prayer `0 6`, minute
`15 6`).

The prayer cron prompt must say:

- Use the `morning-prayer` skill for the full contract.
- Gather the student's goals, recent check-ins and what they are
  reading; choose a verse from the profile's Bible files, quoted
  exactly with the translation named (never from memory).
- Write everything in the student's `language` memory key.
- Run Piper TTS, convert to OGG, deliver as audio + text.
- Don't write memories or ask for credentials in the cron prompt.
- Archive to
  `~/.hermes/profiles/buildwithjesus-agent/morning-prayer-archive.md`.

Example:

```python
cronjob(
    action="create",
    schedule="0 6 * * *",
    name="Morning Prayer",
    prompt="""You are running the student's Morning Prayer for today.
        Use the morning-prayer skill. The student's language is read
        from the language memory key — write everything in it. The
        voice is <piper voice model path>, binary at <piper binary path>. The delivery channel is
        <telegram/whatsapp>. Choose a verse from the profile's Bible
        files (never from memory), quote it exactly with the
        translation named, write the prayer, run Piper TTS, convert
        to OGG, and deliver as audio + text. Do not write memories
        or ask for credentials. Deliver only the final response with
        the audio and the prayer text.""",
    enabled_toolsets=["file", "terminal", "tts"],
)
```

### Night Passage (optional, 8:30 pm)

Default schedule: `30 20 * * *`. Keep at least half an hour between
it and the Planning Session (9 pm default).

The passage cron prompt must say:

- Use the `night-passage` skill for the full contract.
- Continue the student's own reading if they have one (the
  `reading` / `night_passage_position` memory keys); otherwise
  keep a steady walk through one Gospel.
- Choose a passage that speaks to the week — peace, courage,
  comfort. Never heavy or frightening passages at night.
- Quote exactly from the profile's Bible files with the
  translation named (never from memory).
- Run Piper TTS, convert to OGG, deliver as audio + text.
- Archive to
  `~/.hermes/profiles/buildwithjesus-agent/night-passage-archive.md`.

Example:

```python
cronjob(
    action="create",
    schedule="30 20 * * *",
    name="Night Passage",
    prompt="""You are running the student's Night Passage for tonight.
        Use the night-passage skill. The student's language is read
        from the language memory key — write everything in it. The
        voice is <piper voice model path>, binary at <piper binary path>. The delivery channel is
        <telegram/whatsapp>. Continue their current reading from the
        archive; pick a passage that speaks to their week — peace
        and light only, never heavy passages at night; quote it
        exactly from the profile's Bible files with the translation
        named (never from memory); run Piper TTS, convert to OGG,
        and deliver as audio + text. Do not write memories or ask
        for credentials. Deliver only the final response with the
        audio and the text.""",
    enabled_toolsets=["file", "terminal", "tts"],
)
```

### Afternoon Check-In (the afternoon reflection)

Default schedule: `0 17 * * *` (every day at 5 pm, student
timezone). Override per the student's choice.

The check-in cron prompt must say:

- Read the most recent Morning Minute text from the archive.
- Compose a short text message (3 to 6 paragraphs): how the day
  went, one small action for tomorrow, one question to sit with
  overnight.
- Stay inside the chosen tradition.
- Deliver as plain text (no audio) to the student's channel.
- Save a one-line summary to Mnemosyne so tomorrow's Morning
  Minute can open with a callback.

Example:

```python
cronjob(
    action="create",
    schedule="0 17 * * *",
    name="Afternoon Check-In",
    prompt="""You are running the student's Afternoon Check-In
    for today. Use the afternoon-checkin skill. The student's
    tradition is <christian/universal>. Deliver a short text
    message and save a one-line summary to memory. Do not write
    anything else to memory and do not ask for credentials in
    the cron prompt.""",
    enabled_toolsets=["file", "memory"],
)
```

## Managing existing jobs

Before creating a job, call:

```python
cronjob(action="list")
```

If an equivalent job exists:

- Ask whether to keep, update, pause, or remove it.
- Use the exact returned job ID when names are ambiguous.
- Use `cronjob(action="update", job_id="<id>", ...)` for an
  approved change.
- Use `cronjob(action="pause", job_id="<id>")` to stop delivery
  without deleting history.
- Use `cronjob(action="resume", job_id="<id>")` to restart a
  paused job.
- Use `cronjob(action="remove", job_id="<id>")` only after
  explicit approval because removal deletes the schedule.

After creating or updating a job, call `cronjob(action="list")`
and read every created job back field by field: name, schedule,
`skills`, and `prompt`. A creation can land a mangled field (seen
in the field: the first created job's `skills` array arrived
corrupted while later jobs were fine) — if anything is off, repair
it with `cronjob(action="update", job_id="<id>", ...)` before
reporting success. "Created" on screen is not "correct on disk";
the readback is the proof.

## Common pitfalls

1. **Double onboarding.** Hermes already has a built-in
   `onboarding.profile_build: ask` first-touch offer. Let that
   handle the consent-gated profile-build offer, then use this
   skill for capability and schedule choices.
2. **Asking for credentials in chat.** Walk the user to where
   they add things themselves. Never accept keys, tokens, or
   passwords in chat.
3. **Treating a skill as an application installer.** The
   `setup-walkthrough` skill walks the user through Piper, Jina,
   and channel setup — but it doesn't install the user's notes
   app, calendar, or anything else. Confirm those separately.
4. **Creating duplicate crons.** Cron jobs run in fresh sessions
   and don't remember that a similar job was created earlier.
   Always call `cronjob(action="list")` first.
5. **Using memory in cron.** Mnemosyne is not a valid toolset and
   is intentionally skipped in cron contexts.
6. **Fabricating lesson content.** If the Eight Essentials guide
   hasn't been dropped into `essentials/<NN-name>/lessons/`, say
   so. Don't invent chapters.
7. **Mixing traditions.** A Christian student should not get a
   reflection from Marcus Aurelius. A Universal student should
   not get a Psalm. Verify tradition in memory before generating.
8. **Credential leakage.** Never place API keys, tokens, OAuth
   codes, or full account contents in a cron prompt, job name,
   response, skill file, or package artifact.
9. **Skipping the parent for young students.** When a setup
   step involves money, an adult service, or a long-term
   commitment, bring a parent or trusted adult into the
   conversation.
10. **Assuming a language.** Ask; never infer the student's
    language from a name, location, or tradition.

## Verification checklist

- [ ] Identity, profile and life, and tradition were confirmed
      before being written. Profile fields (age, location, hobbies,
      focus goal, friendship circle, blocker, off-limits) all
      landed in Mnemosyne with the student's approval.
- [ ] Language was captured, stored as `language`, and the student's
      guide edition link was shared.
- [ ] Piper was verified with a test synthesis (or the explicit
      Edge fallback was chosen and recorded).
- [ ] Jina API key was verified with a real search.
- [ ] Delivery channel was verified with a test message.
- [ ] Eight Essentials guide MD files are present in every
      `essentials/<NN-name>/lessons/` folder.
- [ ] No credentials, private account contents, vault paths, or
      personal identifiers entered the public package.
- [ ] Memory choice was explicitly selected and verified
      (`hermes memory status`; note its plugin line can display stale
      on some layouts — a fresh session with no dependency warning is
      the real proof. Mnemosyne install guide: the `hermes-mnemosyne`
      skill).
- [ ] Notes or other integrations were distinguished from their
      Hermes skills and configured only after approval.
- [ ] Toolset changes used `hermes tools` or a documented one-off
      toolset override.
- [ ] Existing jobs were listed before any recurring job was
      created.
- [ ] Morning Minute and Afternoon Check-In jobs were created only
      when individually approved, with self-contained prompts.
- [ ] If chosen, the Morning Prayer and Night Passage jobs were
      created with the agreed schedules (Morning Prayer staggered
      from the Morning Minute when both hold the 6 am hour).
- [ ] The Build Round was offered (the `build-project` project
      track) and the student's answer recorded.
- [ ] The role reminder was said plainly (an assistant, not a
      companion) and the `hard-moments` cadence noted.
- [ ] The family brief (`FAMILY.md`) was offered, and the spend
      cap question asked.
- [ ] Newly created jobs were read back field by field (name,
      schedule, skills, prompt) and any mangled field repaired.
- [ ] Post-change config, skill, toolset, and cron state were read
      back.
- [ ] Any required fresh-session or gateway-restart gate was
      reported honestly.