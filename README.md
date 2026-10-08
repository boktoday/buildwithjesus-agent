# Build with Jesus Agent — overview and setup workflow

The **Build with Jesus Agent** is a personalised AI assistant built on
[Hermes Agent](https://hermes-agent.nousresearch.com/docs) for
young people — and adults walking the same road — learning to put
the **Eight Essentials** into daily practice. It is a gentle mentor
that runs a daily rhythm of audio plans, reflection check-ins, and
small actions, taught from the Eight Essentials guide that ships
with the repo.

This edition is built for the **Build with Jesus** project. It lives
comfortably in the **Christian faith**: the agent helps teach
Bible passages, can help shape prayers, and always points the student
back to their church and its leaders - or, in Solo mode, to a trusted
adult. The walker builds real
things for their church and community, and gives them away.

This README is the overview and the workflow for getting the agent
working end to end. Read it once, then run through the steps.

> **Two ways in.** Take the **build path** and build the agent piece by piece: one capability, one payoff, each week, with audio to follow. Or install it with the setup workflow below.
>
> **Start the build path: <https://gladtobe.here.now/build-path/>**

---

## What this product is

The Eight Essentials are learned best by **doing one small thing a
day** over weeks and months — not by reading a book. The Build with Jesus
Agent exists to make that daily rhythm stick:

- A **Morning Minute** lands at a chosen time in the student's chat
  (Telegram or WhatsApp). It's a brief audio plan for the day, plus
  text.
- An **Afternoon Check-In** lands in the afternoon. It's a short
  text message: how the day went, what's next, one question to sit
  with overnight.
- A **Planning Session** lands before bed. It maps tomorrow: school
  tasks, homework deadlines, the essential they're working on this
  week, one real-world thing they want to do. The agent drafts the
  plan, the student edits it, and it saves locally — no app, no
  account, no cloud sync.
- The agent teaches from the **Eight Essentials guide** stored in the
  repo (`essentials/01..08/lessons/christian.md`), written for a
  Christian young person.
- The guide is also published in **ten languages** — read online, or
  downloaded as an offline pack for use without internet. See
  `essentials/guide-editions.md`.
- Two **optional rhythms** a student can switch on: a **Morning
  Prayer** at 6 am (text + audio, shaped by their goals, their week
  and what they are reading) and a **Night Passage** at 8:30 pm — a
  Bible passage read aloud, chosen to speak to their week. Both quote
  every verse from the profile's own Bible files (`bible/`).

**Who walks with it.** The walk is designed around young people and
works unchanged for adults — including adults walking without a
church or group (Solo mode; no pressure either way). Setup asks one
question, "Who's walking?", and records `adult_mode`: an adult gets
adult-to-adult register, no parental gates, and no family briefing;
everything else — the essentials, the rhythm, the Scripture rules —
is the same road.

The agent does not lecture. It draws the wisdom out of the student
with questions, holds the rhythm gently, and restarts them when they
fall off — without scolding.

**For parents and guardians:** `FAMILY.md` is the one-page brief —
what this assistant is and is not, where every record lives, and
your controls: pause anything, cap spending, edit the helplines.

**What it stands on:** `COMMANDMENTS.md` holds the **Ten Commandments
for AI Agents**, the standard this agent holds itself to: the task as
given, truth with provenance, honest ignorance, loud correction,
borrowed authority, kept secrets, no flattery, an assistant and never
a companion, and receipts for everything. Form III in that file is the
acceptance criteria for whoever builds the harness, and the Plain Ten
appears on the AI page (https://buildwithjesus.com/ai).

### Two delivery orders

Every student also picks how the Eight Essentials are served:

- **Sequential** (default) — walk through essentials 1 to 8 in order.
  This is the most coherent and is the order the guide was written
  for. Recommended for new students.
- **Randomised** — draw any essential on any day, matched to what
  the student seems to need that day (longest gap, recent struggle,
  day's energy). Each Morning Minute opens with a knowledge summary
  from the chosen essential plus one small activity. Best for
  students who already know what they need.

In both modes, **all eight essentials are covered eventually.** The
student can switch later by updating the `essentials_order` memory
key — no re-onboarding required.

### Solo mode

For a walker learning without a church — or without one they
want to attend. If they say so during orientation, the agent switches
on **Solo mode**: alongside the Eight Essentials, it walks them
through the Bible at their own pace (John, Genesis, Psalms, Proverbs,
Luke), and every reading and answer is held to a strict rule — only
the actual Bible text, quoted exactly from the downloaded
translation, translation named, nothing invented, nothing glossed.
Questions the text does not answer get a plain answer: "the text
doesn't say". No pressure about church in either direction, ever.

### The Eight Essentials (in the order the guide teaches them)

1. **Silence** — sit still, be alone with your own thoughts
2. **Body** — sleep, food, water, movement, sunlight
3. **Skills** — useful real-world competence (cook, fix, build, budget)
4. **Digital Self-Defence** — privacy, attention, identity literacy
5. **Real Community** — people who know your name
6. **Knowledge Without Wi-Fi** — owned, not rented
7. **Nature** — prescribed time outside, non-negotiable
8. **Tested Faith** — yours, and it holds under pressure

---

## The Bible in this profile

Three public-domain Bible translations ship in `bible/`, for the agent
to ground every Scripture quote in:

| File | Translation | Notes |
|---|---|---|
| `bible/KJV.pdf` | King James Version (1769) | Public domain in the US (Crown rights apply in the UK). |
| `bible/WEB.pdf` | World English Bible | Public domain. Modern plain English — the agent's default for explaining. |
| `bible/ASV.pdf` | American Standard Version (1901) | Public domain. Formal, and more literal. |

These are the profile's Scripture store: the grounded source the agent
retrieves from rather than recalls past — its own slice of the
knowledge base. SOUL.md carries the rule the agent follows strictly:
**every quote is copied from these files, exactly as written, with the
translation named, and never from model memory.** `read_file` extracts
the text from the PDFs, so the agent opens the verse and quotes it,
and pages through the file for longer passages.

A quick check:

```bash
ls bible/*.pdf        # expect KJV.pdf  WEB.pdf  ASV.pdf
```

**Language editions.** Students who use one of the guide's other
languages get their Scripture from a freely-licensed edition
downloaded once at onboarding (`python bible/fetch_edition.py <code>`,
registry in `bible/editions.json`): Reina-Valera 1909 (Spanish),
Unlocked Literal Bible (Tagalog), Chinese Union Version (simplified
and traditional), Vietnamese 1934 - with more languages added after
licence verification. Where no verified edition exists yet, the agent
quotes the English exactly and gives a clearly-marked sense line in
the student's language; it never passes a machine translation off as
Scripture.

To swap in another translation, drop a text-layer PDF into `bible/`
and update the list in SOUL.md. One word of care: most modern
translations (NIV, ESV, NLT, NASB, CSB and so on) are copyrighted —
fine for a student's own personal use, but they cannot be
redistributed in this repo or shipped with the product. Keep the
shipped set to public-domain editions.

---

## How it works

### The daily loop

```
06:00  Morning Minute       Piper TTS audio + text → Telegram or WhatsApp
        ↓
day    Student does the one small action
        ↓
17:00  Afternoon Check-In  Text only → Telegram or WhatsApp
        ↓
21:00  Planning Session      Text only → Telegram or WhatsApp
       Agent drafts tomorrow's plan → student edits → saves locally
        ↓
        Sleep
        ↓
        Repeat
```

The agent reinforces the loop without nagging. Missed days restart
gently. No scolding. No moralising.

**About the schedule:** The times shown above are in the student's
local timezone. The cron daemon stores schedules in **UTC**. If you
choose 6 am AEST (UTC+10), the cron stores `0 20 * * *` (20:00 UTC).
The schedule is always "the time in your timezone" — the conversion to
UTC is automatic.

### The agent's job at each turn

| When | The agent |
|---|---|
| First chat on a fresh profile | Offers the orientation, briefly, in its own voice |
| Student says "set me up" | Runs `agent-onboarding` (consent-gated, phased) |
| Student asks a question | Reads the relevant `essentials/<NN-name>/lessons/*.md`, synthesises, teaches |
| Morning Minute cron fires | Generates the day's plan, runs Piper, uploads, delivers inline |
| Check-In cron fires | Reads the most recent Morning Minute, drafts a short reflection, delivers as text |
| Planning Session cron fires | Drafts tomorrow's plan (school tasks, deadlines, weekly essential, one real-world thing), the student edits it, saves locally |
| Student asks for a deeper dive | Uses the `eight-essentials-curriculum` skill — reads the guide, teaches from it |

### What runs in the background

Three cron jobs, all off until the student approves them at onboarding:

1. **Morning Minute** — fires at the chosen time in the student's
   timezone, every day (or weekdays only, if preferred). Generates
   audio + text and delivers to Telegram or WhatsApp.
2. **Afternoon Check-In** — fires at the chosen afternoon time,
   same day-rule as the Morning Minute. Sends a short text message.
3. **Planning Session** — fires before bed (default 9 pm), same
   day-rule. Drafts tomorrow's plan for the student to edit, then
   saves it locally.

All three are **opt-in** — the orientation creates them only after
explicit approval.

### The twenty daily prompts

A small library of go-to questions a walker can put to the
Build with Jesus Agent at any time. The agent reads the relevant guide
chapter, draws on what it already knows about the student, and
answers in their voice, Bible-anchored.

The point is **not** to answer all twenty each day. The point is
to have a small set of go-to prompts that surface the essentials,
draw out reflection, and turn curiosity into a daily practice.
Pick one or two. Skip the rest. Rotate through the week.

The prompts are written in the young person's voice. The agent does not
lecture back. It asks the question, holds space for the answer,
and follows up with one small action.

The full prompts file lives at
`essentials/00-introduction/lessons/prompts.md`. The agent reads
it when the student asks for "something to think about," a
question to sit with, or help getting unstuck.

#### By mode

| Mode | Prompts |
|---|---|
| Self-reflection | #1, #3, #6, #7, #12, #15, #16, #20 |
| Activity | #2, #9, #13, #14, #17, #19 |
| Critical thinking | #5, #8, #10, #18 |
| Daily ritual | #11, #16, #20 |

#### By energy

| Energy | Suggested prompts |
|---|---|
| Tired, low | #1, #20, #11 |
| Wired, curious | #5, #10, #14 |
| Stuck or flat | #3, #9, #15 |
| Want to think | #4, #6, #16, #18 |
| Want to do | #2, #9, #13, #17, #19 |

#### By essential (every essential surfaces at least twice)

| Essential | Prompts that lean into it |
|---|---|
| Silence | #1, #7, #9, #12, #16 |
| Body | #2, #9, #14, #19 |
| Skills | #8, #13, #14 |
| Digital Self-Defence | #4, #8, #18 |
| Real Community | #6, #15, #17 |
| Knowledge Without Wi-Fi | #3, #6, #8, #10, #11 |
| Nature | #9, #19 |
| Tested Faith | #1, #5, #7, #10, #16, #18 |

#### Heavy prompts (use rarely)

Prompts **#1**, **#5**, **#10**, and **#18** are heavy. The agent
never leans on them. The student must ask for them by name. If
the student asks for a heavy prompt and the agent judges it is
the wrong day, the agent may gently offer a lighter alternative
and explain why.

#### The twenty

| # | Question | Mode | Energy | Essentials |
|---|----------|------|--------|------------|
| 1 | Ask me one question that I probably don't want to answer, but should. | Self-reflection | Tired / low | All eight (esp. Tested Faith, Silence) |
| 2 | Give me a 10-minute task that will make me uncomfortable in a useful way. | Activity | Want to do | Body, Silence, Tested Faith |
| 3 | What did I do three days ago that I haven't done since? Why? | Self-reflection | Stuck / flat | Self-knowledge, Knowledge Without Wi-Fi |
| 4 | Pick one essential I'm weakest at. What's the smallest practice I could do today? | Critical thinking | Want to think | All eight (diagnostic) |
| 5 | Argue against my last decision. What would a wise critic say? | Critical thinking | Wired / curious | Knowledge Without Wi-Fi, Tested Faith |
| 6 | If I had to teach a Year 7 student one thing I've learned this year, what should it be? | Self-reflection | Want to think | Knowledge Without Wi-Fi, Real Community |
| 7 | Where in my life am I performing instead of actually doing? Where am I actually doing instead of performing? | Self-reflection | Tired / low | Tested Faith, Silence |
| 8 | What am I currently outsourcing that I should be building myself? | Critical thinking | Want to think | Skills, Digital Self-Defence, Knowledge Without Wi-Fi |
| 9 | Give me a 30-minute activity that requires no phone and no one else. | Activity | Stuck / flat | Body, Silence, Nature |
| 10 | What is one belief I hold that I couldn't defend if pressed? Should I keep it anyway? | Critical thinking | Wired / curious | Tested Faith, Knowledge Without Wi-Fi |
| 11 | Quiz me on something I've forgotten I used to know. | Daily ritual | Tired / low | Knowledge Without Wi-Fi |
| 12 | Ask me about the last time I was genuinely bored, and what I noticed in the silence. | Self-reflection | Stuck / flat | Silence, Body |
| 13 | Suggest one thing I could finish today that I started more than a week ago. | Activity | Want to do | Skills, Tested Faith |
| 14 | Walk me through how to do something practical I don't know how to do yet — feed myself, fix a puncture, write a CV, change a tyre. | Activity | Wired / curious | Skills, Body |
| 15 | Who in my life would show up at 2am? Who wouldn't? Why? | Self-reflection | Stuck / flat | Real Community |
| 16 | Compare how I spent my time today vs how I said I wanted to spend it. Where's the gap? | Daily ritual | Want to think | Tested Faith, Silence |
| 17 | Give me a conversation starter I could use with one person I haven't spoken to properly in a while. | Activity | Want to do | Real Community |
| 18 | If I deleted every app on my phone except three, which three should stay and why? | Critical thinking | Want to think | Digital Self-Defence, Tested Faith |
| 19 | Walk me outside for 15 minutes — what should I actually look at, listen for, notice? | Activity | Want to do | Nature, Body, Silence |
| 20 | End the day with me. Three things that happened, three things I noticed, one thing I'm grateful for. | Daily ritual | Tired / low | All eight (closing the day) |

#### How the agent uses them

The agent reads
`essentials/00-introduction/lessons/prompts.md` whenever the student
asks for a prompt. It does **not** paste prompts at the student. It
references one, invites the student to read it, and holds space
for the answer. It never asks three prompts in a row.

In **sequential** delivery order, prompts naturally cluster around
the essential the student is on. In **randomised** order, the
agent picks the prompt that matches the moment. All eight
essentials remain available in both modes.

---

## Daily rituals

This is the at-a-glance map of every ritual the agent runs — what it
is, when it fires, where it lands, and where it is documented in
detail.

| Ritual | When | Channel | What happens |
|---|---|---|---|
| **Morning Minute** | Daily at the student's chosen time (default 6 am) | Telegram or WhatsApp — **voice bubble + text** | Audio plan for the day, focused on one small action from the current essential. |
| **Afternoon Check-In** | Daily at the student's chosen time (default 5 pm) | Telegram or WhatsApp — **text only** | Reflection on how the day went, plan for tomorrow, one question to sit with overnight. |
| **Planning Session** | Daily before bed at the student's chosen time (default 9 pm) | Telegram or WhatsApp — **text only** | Agent drafts tomorrow's plan (school tasks, homework deadlines, the week's essential, one real-world thing), and asks the Build Round when a project is active. The student edits it. Saves locally. |
| **Essential Summary** | On demand, any time the student asks | Telegram or WhatsApp — **voice note** | 3 to 5 minute spoken summary of one essential + a short written key-points list. |
| **Essential Lesson** | On demand, any time the student asks | here.now — **HTML page link in chat** | Three-page lesson on one essential with cited sources, key quotes, and a short quiz. |
| **Essential Poem** | On demand, any time the student asks | Telegram or WhatsApp — **voice note + text** | A rhyming spoken-word poem on the essential, read aloud with text underneath. |
| **Essential Song** | On demand, any time the student asks | Telegram or WhatsApp — **MP3 voice note + text** | The agent writes a poem about the essential, then turns it into a real song via Google Lyria 3 on OpenRouter. Costs ~$0.08 per song — confirm before running. |
| **Essential Music Video** | On demand, any time the student asks | here.now — **MP4 video link in chat** | The song above, plus a storyboard of still images stitched together with the audio, optional poem-text overlay. Costs ~$0.35 total — confirm before running. |

**The day.** The Morning Minute opens the day, the Check-In closes
it, and the Planning Session maps tomorrow before sleep. The three
on-demand formats (Summary / Lesson / Poem) are there whenever a
walker wants to learn an essential more deeply than the
Morning Minute can cover in one minute.

**Where the code lives.** Each row links to a skill in the repo:

| Ritual | Skill path |
|---|---|
| Morning Minute | `skills/hermes/morning-minute/` |
| Afternoon Check-In | `skills/profile/afternoon-checkin/` |
| Planning Session | `skills/profile/planning-session/` |
| Essential Summary, Lesson, Poem, Song, Music Video | `skills/profile/essential-deep-dives/` (Song and Music Video use `skills/creative/openrouter-lyria-music/` and `skills/creative/poem-song-video-studio/`) |

**Consent.** The three cron-based rituals (Morning Minute, Check-In,
Planning Session) are off until the student or parent approves them
during onboarding. The five on-demand formats (Summary, Lesson,
Poem, Song, Music Video) are available immediately — the student
just asks. The two paid formats (Song and Music Video, Lyria 3 +
storyboard images) require the student to confirm spend each time
the agent is asked for one. See [The setup workflow →
What runs in the background](#what-runs-in-the-background) for the
exact opt-in flow.

**Song and Music Video skills.** The two paid formats reuse two
existing skills rather than reinventing them:

| Format | Underlying skill | What it adds on top of `essential-deep-dives` |
|---|---|---|
| **Essential Song** | `skills/creative/openrouter-lyria-music/` | POEM lyrics → MP3 audio via Google Lyria 3 (~$0.08/song). |
| **Essential Music Video** | `skills/creative/poem-song-video-studio/` | SONG + ~8 storyboard images + ffmpeg → MP4 (~$0.35 total). |

Both skills already exist in the repo with full Lyria 3 model
notes, scripts, and a cost guard. The agent loads the underlying
skill when the student asks for the format.

**How to customise.** The agent walks the student through choosing
the time, timezone, and day-rule for each cron ritual during setup.
All three can be paused, resumed, or removed later with
`cronjob(action="...")`. The on-demand formats pick up the student's
settings automatically; their voice and length are inherited from
the morning-minute Piper voice already chosen.

---

## Guided commands (/slash)

Sixteen shortcuts for the daily rituals, the build round, the deep
dives, the twenty prompts, the guide and outreach. They live in the
`bwj-commands` plugin and appear automatically in CLI autocomplete,
`/help`, and the Telegram command menu.

| Command | What it does | Skill it starts |
|---|---|---|
| `/morning` | Runs today's Morning Minute now - audio + text | `morning-minute` |
| `/prayer` | Runs today's Morning Prayer now - audio + text | `morning-prayer` |
| `/checkin` | Runs today's Afternoon Check-In now | `afternoon-checkin` |
| `/tomorrow` | Runs tonight's Planning Session (plans tomorrow), opening with the Build Round | `planning-session` |
| `/passage` | Runs tonight's Night Passage now - audio + text | `night-passage` |
| `/build` | The Build Round: start / keep going / finish. Takes an argument - `/build start`, `/build keep`, `/build finish` - or the idea in a sentence | `build-project` |
| `/summary` | An essential's key points plus a 3 to 5 minute voice note | `essential-deep-dives` (Format 1) |
| `/lesson` | A three-page HTML lesson with cited sources and a quiz - delivered as a link | `essential-deep-dives` (Format 2) |
| `/poem` | A rhyming spoken-word poem - voice note + text | `essential-deep-dives` (Format 3) |
| `/song` | An original song about an essential (~$0.08; the agent confirms spend first) | `essential-deep-dives` (Format 4) |
| `/video` | A music video for the song (~$0.35; spend confirmed first) | `essential-deep-dives` (Format 5) |
| `/question` | One of the twenty prompts, to sit with. Takes a number (`/question 13`) or a mood (`tired`, `wired`, `stuck`, `think`, `do`) | `essentials/00-introduction/lessons/prompts.md` |
| `/ideas` | Brainstorm things to build or do this week - tailored, and routable into the build track | `build-project` + guide activities |
| `/guide` | The student's guide edition - read online plus the offline pack | `essentials/guide-editions.md` |
| `/outreach` | Finds a real need to build for: target list, first message, discovery questions, expressions of interest | `outreach` |
| `/recap` | Your week in review: learned, built, gave, one win, one thing for next week | `weekly-review` |

Each command simply starts the same flow the schedule would run, in the
live conversation - consent, voice and cost rules all still
apply. They are shortcuts, never requirements: students can always just
ask in a sentence ("run my Morning Minute").

**One-time setup.** The plugin ships in `plugins/bwj-commands/`. Enable
it, and (for Telegram/WhatsApp) allow it to start turns in the live
session:

```bash
hermes plugins enable bwj-commands
```

```yaml
# config.yaml
plugins:
  enabled:
    - bwj-commands
  entries:
    bwj-commands:
      allow_gateway_injection: true
```

On the gateway the commands appear in the Telegram bot menu automatically.

---

## Build projects (short and long)

Two sizes of making, one loop: Learn. Build. Give.

- **Small builds** (`build-coach`) — one-activity things: a shelf,
  a repair, welcome cards. Done in a sitting or a weekend.
- **Projects** (`build-project`) — a workshop day, or a short or
  long project. Most often the walker using the agent to design
  and vibe-code something real: an **app**, a **local-first
  website**, a **dashboard** — for a need in their own life, their
  church, or their community. Or a real-world build from the
  guide's activities.

Once something is on the workbench, the nightly Planning Session
opens with the **Build Round**:

> "Build round: are we starting something new, keeping one going,
> or finishing and giving one away?"

Three doors, three different jobs: find the need and scope the
smallest thing that helps; run maker sessions where the student
directs and the agent generates alongside them; and finish properly
— tested by the person it is for, named, with a how-to card, then
**given away** (`handover`). The agent keeps the record in
`build-project.md`: the inbox of ideas, the active project card,
and an archive of everything finished and given.

**The story.** After the give, `handover` offers to write one page
about the build - the need, the making, the giving, in the
student's words. It is what they show their church and their
family, and it makes every outreach conversation easier.

Defaults keep it safe: local-first (no accounts, no servers, $0),
no personal data collection, consent from whoever it is for, and a
parent or leader in the loop for anything hosted or public. One
project at a time — the inbox holds the rest.

**Where ideas come from.** Three places: the student's own life
(build-project Door 1), a brainstorm (`/ideas`, or the activity
prompts in the twenty), or a real need found through outreach - see
the outreach section below.

**Finding a need to build for.** For needs outside their own life,
the `outreach` workflow (next section) finds a real problem, makes
the free-build offer, and captures expressions of interest. A
qualified need comes back into this pipeline as the project card.

**Where the code lives.**

| Track | Skill path |
|---|---|
| Small builds | `skills/profile/build-coach/` |
| Projects (pipeline + Build Round) | `skills/profile/build-project/` |
| Finding a need (outreach) | `skills/profile/outreach/` |
| The give-away | `skills/profile/handover/` |

---

## Outreach - find a real need to build for

Stage two of the build track. Stage one is building for yourself and
learning the craft; stage two is going out and serving a real need.
The `outreach` skill (and the `/outreach` command) carries the whole
workflow:

1. **The target list** - three to five places: the school, the church
   and its ministries, community hubs (library, community centre,
   sports club, food bank, aged care).
2. **The first message** - the offer in the student's own words:
   *"If there's something hard to keep track of, plan, or share where
   you are, I'd love to build you a small, simple tool for free and
   hand it over as a gift. No cost, no catch."* One question rides
   along: what's the most annoying repetitive task in your week?
3. **The discovery conversation** - a ten-question set that finds
   what people actually need: what's repetitive, what lives on
   paper, what breaks when someone is away, how they cope now, what
   "solved" looks like.
4. **Five filters** - real, small, buildable, safe, givable. A need
   that passes becomes the project card; "not now" is a normal
   outcome, logged like everything else.
5. **The brief, then the yes** - one page, in their words, with the
   give-away promise. Then the build runs through `build-project`
   and ends in `handover`.

**The expressions-of-interest page.** Organisations can also come to
the student: the workflow includes a single-page site the student
builds themselves - the offer as the headline, their finished builds
as proof, how it works, and a short expressions form routed to a
family-monitored inbox (no trackers, no personal data beyond what
the reply needs). It prints as a flyer with a QR code for
noticeboards.

**Safety defaults** run through everything: a parent or youth
leader approves the target list and every step, official channels
only, never meeting anyone alone, no personal data collection, one
polite follow-up maximum. The whole campaign lives in
`skills/profile/outreach/` and is tracked in `outreach-log.md`.

---

## What it costs to run

Build with Jesus Agent runs **pay-as-you-go** — no subscription. You top up
an OpenRouter account and the agent draws from that credit.

| Expense | Amount | Notes |
|---|---|---|
| **First month** | **about $20** | Covers setup plus the first month of real use while the student settles in |
| **Ongoing** | **$5–$10 a month** | Light daily use on low-cost models |

The profile leans on low-cost models for the routine work:

- **DeepSeek V4 Flash** — the default for daily chat and lessons.
- **Google Gemini 3.7 Flash** — the fast fallback for short tasks.
- **Open-source models** (free or near-free tiers) — for basic,
  high-volume work that does not need a frontier model.

Free tiers rotate month to month, so the exact list changes. See the
live free-models list at <https://openrouter.ai/openrouter/free>. The
profile defaults to cheap options and only reaches for a larger model
when a task genuinely needs one.

---

## Tutorials

Prefer a guided walkthrough? The tutorial hub collects all the setup pages in one place:

- **The build path** — seven pages that teach by building it: the agent made piece by piece, with audio to follow. Start at <https://gladtobe.here.now/build-path/>.
- **The onboarding curriculum** — seven pages: the installer course, from first install to an agent wired up to chat.
- **The walkthrough sheets** — the setup on a single page, in three languages.

Open the hub at <https://gladtobe.here.now/hub-tutorials.html>. The workflow below covers the same ground in text, step by step.

---
## The setup workflow

### 1 — Prerequisites (one-time, on the machine)

You need:

- **Hermes Agent** installed. Quick check: `hermes --version`. See
  the [install guide](https://hermes-agent.nousresearch.com/docs).
- **Python 3.10 through 3.13** (not the Windows Windows Store shim —
  a real install). `python --version`.
- **Piper TTS.** A working install (`pip install piper-tts` is the
  quickest route; more in `INSTALL.md`, Step 4). See Step 2 below.
- **ffmpeg** for WAV → OGG conversion. `ffmpeg -version`.
- **A model provider key.** The profile defaults to
  `openrouter + deepseek-v4-flash`. One key unlocks a large catalogue
  of models — including free-tier and multimodal (image, audio) models.
  Sign up free at <https://openrouter.ai/> and add the key with
  `hermes setup`. OpenCode Go is the fallback.
- **A Jina AI free API key** for web search. Sign up free at
  <https://jina.ai/> — no credit card. The free tier is enough for a
  walker's daily use.
- **A Telegram bot** (recommended) or a WhatsApp bridge. Telegram is
  much easier — see Step 4.

### 2 — Download the profile (one-time)

Get `buildwithjesus-agent.zip` from the install sheet
(https://gladtobe.here.now/buildwithjesus/install.html) and extract it
into your Hermes profiles folder:

```bash
# Mac / Linux:
unzip -q ~/Downloads/buildwithjesus-agent.zip -d ~/.hermes/profiles/

# Windows:
tar -xf "%USERPROFILE%\Downloads\buildwithjesus-agent.zip" -C "%LOCALAPPDATA%\hermes\profiles"

hermes profile use buildwithjesus-agent
hermes chat
```

> **Note:** the profile directory is named `buildwithjesus-agent`, not
> `buildwithjesus`. Update commands that reference the profile path
> accordingly.

Then install the memory plugin once — Mnemosyne (local-first memory)
is not bundled with Hermes; its installer fetches the packages itself:

```bash
# Linux / macOS
~/.hermes/hermes-agent/venv/bin/mnemosyne-hermes --hermes-home ~/.hermes install
```

On Windows, run
`%LOCALAPPDATA%\hermes\hermes-agent\venv\Scripts\mnemosyne-hermes.exe`
with `--hermes-home "%LOCALAPPDATA%\hermes" install --python "%LOCALAPPDATA%\hermes\hermes-agent\venv\Scripts\python.exe"`,
then enable it for this profile:

```bash
hermes plugins enable hermes-mnemosyne
```

A fresh chat session should show no "mnemosyne declares Python
dependencies" warning. Windows symlink errors and the status-display
quirk are covered in `INSTALL.md`, Step 1b.

> **Windows:** profiles live at `%LOCALAPPDATA%\hermes\profiles`
> (`C:\Users\<you>\AppData\Local\hermes\profiles`), not `~/.hermes`.

To pull updates later:

```bash
git -C ~/.hermes/profiles/buildwithjesus-agent pull
```

### 3 — First chat → orientation

On the first chat, the agent opens with:

> "Before we dive in — want me to walk you through setup? It takes a
> couple of minutes and gets your tools, memory, and the morning
> minute working the way you want. Or we can skip it and just start."

Say yes (or just ask *"help me set up my profile"* any time). The
`agent-onboarding` skill runs.

### 4 — The orientation (consent-gated)

The orientation is conversational. The agent asks one small group of
related questions at a time and **pauses at every credential gate** — it
never asks for keys or tokens in chat.

Here is what it covers, in order:

| Step | What happens | Where you add things |
|---|---|---|
| Step | What happens | Where you add things |
|---|---|---|
| 1. Identity | Names (yours, the student's, the agent's), reply style, and the language for the guide, lessons and messages | Stored in the profile memory |
| 2. Profile and life | Age, location, living situation, week shape, 3 interests, focus goal, friendship circle, blocker, off-limits — the fields the agent uses to tailor the Morning Minute and lessons | Stored in profile memory |
| 3. Piper install + voice | Verifies Piper works, picks a voice, downloads the voice model | Voice model in `piper-voices/` |
| 4. Jina API key | Sign up free, add to `.env`, agent verifies with a real search | `JINA_API_KEY=` in `.env` |
| 5. Delivery channel | Telegram or WhatsApp bot credentials | `TELEGRAM_BOT_TOKEN=` / `WHATSAPP_*` in `.env` |
| 6. Eight Essentials guide | Confirms the lesson MD files are in `essentials/01..08/lessons/`, and shares the guide's edition in the student's language (`essentials/guide-editions.md`) | Files in the repo |
| 7. Memory | Mnemosyne recommended (local-first, no external account) | `hermes memory setup` |
| 8. Morning Minute schedule | What time, what timezone, what days | Created as a cron job |
| 9. Afternoon Check-In schedule | What time, what timezone, what days | Created as a cron job |
| 10. Planning Session schedule | What time (default 9 pm), what timezone, what days | Created as a cron job |
| 11. Token Router (optional) | The plugin that narrows the tool surface | `plugins.enabled` in `config.yaml` |

At the end the agent shows a **Proposed setup** summary and waits for
your explicit approval before applying anything.

### 5 — Verify each piece

Before the first scheduled Morning Minute, verify each component:

```bash
# Piper works — test synthesis (paths vary by OS; see below)
echo "The Morning Minute is ready." | piper -m piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx -f /tmp/piper-test.wav

# Jina works
curl -s -H "Authorization: Bearer jina_xxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
  "https://s.jina.ai/https://hermes-agent.nousresearch.com/docs"
# → clean snippet of the docs page means it works

# Telegram bot works (sends a test message)
# Use the test script in Step 3 of the Telegram setup below.
# If you get "chat not found", you must first send any message to your bot in Telegram.

# Guide MD files are present
for d in essentials/*/lessons/; do echo "--- $d ---"; ls "$d"; done

# Mnemosyne is configured
hermes memory status

# Cron jobs are queued
cronjob(action="list")
```

**Piper binary locations by platform:**

| Platform | Typical path |
|---|---|
| Linux | `/data/.hermes/bin/piper/piper` |
| macOS (Homebrew) | `/opt/homebrew/bin/piper` |
| macOS (manual) | `~/Library/Piper/piper` |
| Windows | `C:/Users/<you>/.openhuman/bin/piper/piper/piper.exe` |
| Windows (pip) | `pip install piper-tts`, then `piper` on PATH |

The orientation will probe for Piper and find it if it's on your PATH.
If it's installed somewhere unusual, the orientation will ask for the
path.

**Voice model storage** (populate once, reuse forever):

| Voice | Locale | Hugging Face path |
|---|---|---|
| `en_US-joe-medium` | US male | `rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx` |
| `en_US-amy-medium` | US female | `rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx` |
| `en_GB-alan-medium` | UK male | `rhasspy/piper-voices/resolve/main/en/en_GB/alan/medium/en_GB-alan-medium.onnx` |
| `en_GB-jenny_dioco-medium` | UK female | `rhasspy/piper-voices/resolve/main/en/en_GB/jenny_dioco/medium/en_GB-jenny_dioco-medium.onnx` |
| `en_AU-natasha-medium` | AU female | `rhasspy/piper-voices/resolve/main/en/en_AU/natasha/medium/en_AU-natasha-medium.onnx` |

Fetch pattern (example — Joe on Linux):

```bash
mkdir -p ~/.hermes/piper-voices/en/en_US/joe/medium
curl -sL --fail \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx" \
  -o ~/.hermes/piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx
curl -sL --fail \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx.json" \
  -o ~/.hermes/piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx.json
```

### 6 — First scheduled run

The Morning Minute fires at the next scheduled time in the student's
timezone. It generates audio (Piper), uploads to here.now for a public
URL, then delivers that audio directly to Telegram via multipart upload
— **not** via a `MEDIA:<url>` link (here.now's Cloudflare configuration
blocks Telegram's file-fetch bot). The Check-In fires at the next
scheduled afternoon time.

### 7 — Day-to-day operation

The student doesn't interact with the agent through a terminal every
day. The Telegram or WhatsApp chat **is** the daily surface:

- **Morning Minute** arrives as a voice bubble + text plan.
- **Morning Prayer** (optional) arrives at 6 am as a voice bubble
  + text — a short prayer shaped by the student's week and what they
  are reading. See `skills/profile/morning-prayer/`.
- **Afternoon Check-In** arrives as text.
- **Night Passage** (optional) arrives at 8:30 pm as a voice bubble
  + text: a Bible passage chosen to speak to the week, a better end
  to the day than the scroll. See `skills/profile/night-passage/`.
- **Planning Session** arrives before bed as text — the agent
  drafts tomorrow's plan (school tasks, homework deadlines, the
  week's essential, one real-world thing), the student edits it,
  and it saves locally. See
  `skills/profile/planning-session/`.
- **Reply to the check-in** with a one-line note on how the day went.
  The agent saves a summary and uses it as the callback in tomorrow's
  Morning Minute.
- **Ask questions any time.** "What does tested faith actually look
  like?" "How do I find a real community?" The agent reads the guide
  and teaches.

#### Deeper ways to learn an essential (on demand)

Beyond the daily rhythm, the student can ask for any of **three deeper
formats** on any essential. All three are handled by the
`essential-deep-dives` skill (see `skills/profile/essential-deep-dives/`),
and all three require nothing but asking:

- **Essential Summary** — the key points of one essential in plain
  language, plus a 3 to 5 minute **voice note** the agent generates
  (Piper) and drops into the chat so the student can listen while
  walking or doing chores.
- **Essential Lesson** — a beautiful **three-page lesson** built as an
  HTML page and published to the household's **here.now** account.
  It teaches the essential with **cited sources** (researched via the
  Jina API whenever the lesson needs material the guide doesn't
  carry), **key quotes**, and a short **quiz** the student answers on
  the page. The agent sends the link in the chat.
- **Essential Poem** — a rhyming **spoken-word poem** on the
  essential, read aloud as a voice note with the text below so the
  student can read along.
- **Essential Song** — the agent writes an original poem about the
  essential, then turns it into a real song (MP3) via
  `google/lyria-3-pro-preview` on OpenRouter (~$0.08 per song).
  The voice note plays in chat, the text of the poem follows.
  Confirm spend before running.
- **Essential Music Video** — the Song above, plus a storyboard of
  image frames stitched with the audio and optional poem-text
  overlay (~$0.35 in total for song + storyboard images + ffmpeg
  assembly). Published as an MP4 to here.now; the link goes in
  chat. Confirm spend before running.

The agent reads the guide before drafting any of them, reads the guide carefully, and tailors to the student's profile — the
same rules as the curriculum skill.

### 8 — Maintenance

Occasional:

- `hermes update` — pulls the standard Hermes skill library into the
  profile (curated skills are never overwritten).
- `git -C ~/.hermes/profiles/buildwithjesus-agent pull` — gets upstream
  improvements to the guide or skills.
- `cronjob(action="list")` — confirms both jobs are still scheduled.

---

## What you'll configure in `.env`

The profile ships with `.env.example` showing every variable. Here is
what you actually set.

### Required (any setup)

```bash
# Model provider key
OPENAI_API_KEY=...          # or your provider's key name

# Web search (free)
JINA_API_KEY=jina_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Required for Telegram delivery

```bash
# Get these from @BotFather in Telegram
TELEGRAM_BOT_TOKEN=1234567890:ABCDefghijklmnopqrstuvwxyz
TELEGRAM_CHAT_ID=123456789
```

> **Telegram setup note:** after creating your bot via @BotFather, you
> **must send it at least one message** (e.g. `/start`) before the
> agent can send to you. A bot that has never received a message will
> silently fail on send.

To find your chat ID: message `@userinfobot` in Telegram and it will
reply with your numeric ID.

### Required for audio (Morning Minute)

```bash
# here.now is a site publisher, not a drive. The API key is all you need.
# DRIVE_ID is not used by the audio publish flow — ignore it if you see it.
HERENOW_API_KEY=hn_xxxxxxx
```

> **Note on here.now:** the audio is uploaded via here.now's publish
> API, which gives a public URL. This URL is sent to Telegram via
> multipart upload — it does **not** need a DRIVE_ID. If you see
> `HERENOW_DRIVE_ID` in older docs or examples, it is legacy and not
> used by the current audio delivery flow.

### Optional integrations

```bash
# Notion
NOTION_API_KEY=...

# GitHub (for tracking, opening issues)
GITHUB_TOKEN=...

# Bluesky (if you publish there)
BLUESKY_HANDLE=...
BLUESKY_APP_PASSWORD=...
```

### Things that are NOT env vars

- **Voice model path** — stored in profile memory, not env. Path is
  machine-specific.
- **Cron schedules** — set via `cronjob(action="create", ...)`,
  stored in the cron registry, not env.
- **Piper binary path** — stored in profile memory.
- **Mnemosyne** — local-first, no key needed.

---

## What's in the repo

```
buildwithjesus-agent/
├── README.md                              ← this file
├── FAMILY.md                              ← the one-page brief for parents and guardians
├── SOUL.md                                ← persona and operating voice
├── COMMANDMENTS.md                        ← the Ten Commandments for AI Agents (the standing standard)
├── AGENTS.md                              ← operating principles
├── profile.yaml                           ← profile descriptor
├── config.yaml                            ← Hermes runtime config
├── .env.example                           ← every variable, with comments
├── .gitignore
├── spend-log.md                           ← the paid-extras ledger (optional monthly cap)
├── LICENSE                                ← MIT
├── bible/                                 ← the Scripture store: KJV, WEB, ASV (PDF)
│   ├── KJV.pdf
│   ├── WEB.pdf
│   ├── ASV.pdf
│   ├── editions.json                       ← freely-licensed language editions (fetched at onboarding)
│   ├── fetch_edition.py                    ← one-shot download for the student's language
│   └── README.md
│
├── essentials/                            ← the Eight Essentials source content
│   ├── 00-introduction/lessons/
│   │   └── christian.md                   ← Introduction
│   ├── 01-silence/
│   │   ├── SKILL.md                       ← agent's teaching notes for this essential
│   │   ├── lessons/
│   │   │   ├── README.md                 ← file schema
│   │   │   └── christian.md               ← Chapter 1
│   │   └── activities/README.md
│   ├── 02-body/        (same structure)
│   ├── 03-skills/      (same structure)
│   ├── 04-digital-self-defence/
│   ├── 05-community/
│   ├── 06-knowledge/
│   ├── 07-nature/
│   ├── 08-faith/
│   │   ├── lessons/
│   │   │   └── christian.md               ← Tested Faith + Christian Customisation
│   │   └── activities/README.md
│   ├── 09-conclusion/lessons/christian.md
│   ├── 10-before-after/lessons/christian.md
│   └── guide-editions.md                  ← the guide online in ten languages
│
├── skills/
│   ├── hermes/                            ← Hermes-curated skills
│   │   ├── agent-onboarding/  ← the orientation
│   │   ├── morning-minute/                ← daily plan + audio
│   │   ├── hermes-mnemosyne/              ← memory provider
│   │   ├── mnemosyne-maintenance/
│   │   └── skill-auditor/
│   └── profile/                       ← the profile's own skills
│       ├── afternoon-checkin/           ← afternoon reflection
│       ├── eight-essentials-curriculum/   ← teaches from the guide
│       ├── essential-deep-dives/          ← summary, lesson, poem formats
│       ├── morning-prayer/                ← optional 6 am prayer (audio + text)
│       ├── night-passage/                 ← optional 8:30 pm Bible reading (audio + text)
│       ├── planning-session/              ← the nightly plan + the Build Round
│       ├── build-coach/                   ← small one-activity builds
│       ├── build-project/                 ← project builds: apps, sites, dashboards, workshops
│       ├── outreach/                      ← finding a real need (community, schools, churches)
│       ├── hard-moments/                   ← hard moments: the role boundary, real people, helplines
│       ├── weekly-review/                 ← the weekly recap (and the gentle comeback)
│       ├── handover/                      ← giving a finished build away
│       └── setup-walkthrough/            ← Piper, Jina, channel setup
│
├── plugins/bwj-commands/                  ← /morning /prayer /checkin /tomorrow /passage /build
├── plugins/hermes-token-router/           ← optional tool-narrowing plugin
├── memories/                              ← generic operating-practice seeds
└── skins/buildwithjesus.yaml                 ← colour theme
```

> **Standard Hermes skills** (web, terminal, github, creative, etc.)
> are pulled in by `hermes update` and are not part of this repo.
> They are listed in the standard library, not here.

---

## Configuration reference

### Model provider (`config.yaml`)

```yaml
model:
  default: deepseek-v4-flash
  provider: openrouter
fallback_providers:
  - provider: opencode
    model: deepseek-v4-flash
```

Change `provider` and `default` to switch. OpenRouter is the default
because a single key opens the widest catalogue — free models, plus
multimodal (image, audio) models — without changing providers. The
fallback chain runs only when the primary is unavailable.

### Toolsets (`config.yaml`)

Every CLI toolset is **enabled by default**. The orientation walks the
student through reviewing each one. To manually disable:

```bash
hermes --profile buildwithjesus-agent tools
# Or start with a specific set:
hermes --profile buildwithjesus-agent chat --toolsets "web,terminal,file,memory"
```

The `tts` toolset must stay on for the Morning Minute.

### Cron jobs

Create via the orientation. To manage manually:

```python
# List
cronjob(action="list")

# Create Morning Minute (UTC schedule — 6am AEST = 20:00 UTC)
cronjob(
    action="create",
    schedule="0 20 * * *",
    name="Morning Minute",
    prompt="""You are running the student's Morning Minute.
    Use the morning-minute skill. Generate the day's plan, run Piper TTS,
    upload to here.now, deliver via multipart upload to Telegram.
    Do not write memories. Deliver only the final voice + text.""",
    skills=["morning-minute"],
    deliver="telegram",
)

# Weekdays only Morning Minute (6am, Mon–Fri)
cronjob(
    action="create",
    schedule="0 20 * * 1-5",
    name="Morning Minute",
    ...
)

# Pause without deleting
cronjob(action="pause", job_id="<id>")

# Resume
cronjob(action="resume", job_id="<id>")

# Remove (requires approval — deletes the schedule permanently)
cronjob(action="remove", job_id="<id>")
```

See `skills/hermes/morning-minute/SKILL.md` for the full Morning
Minute cron contract.

> **Cron delivery:** the TUI/CLI session has no live-delivery channel.
> If you want to be notified when a cron fires, set `deliver="telegram"`
> (or `deliver="all"`) on create. Otherwise outputs are saved locally
> and viewable via `cronjob(action="list")`.

---

## Common pitfalls

| Symptom | Likely cause | Fix |
|---|---|---|
| Piper fails to load | Voice model path wrong, or not downloaded | Re-run the Piper step of the orientation |
| Morning Minute audio is silent or truncated | TTS input text was truncated | Verify the text file is complete before synthesis |
| Telegram send fails with "chat not found" | Bot has never received a message | Open Telegram, find your bot, send it `/start` |
| Telegram audio doesn't render | Using `MEDIA:<url>` with here.now URL | Use multipart upload via `sendVoice` (the skill handles this) |
| Cron fires at the wrong time | UTC confusion | The cron stores UTC. 6am AEST = `0 20 * * *`. 6am EST = `0 11 * * *` |
| Schedule says daily but only fires weekdays | Wrong cron format | `0 6 * * *` = every day. `0 6 * * 1-5` = Mon–Fri |
| Jina search returns nothing | Key not in `.env` or wrong | Test with `curl -H "Authorization: Bearer YOUR_KEY" "https://s.jina.ai/"` |
| Lesson file isn't being read | Missing the lesson MD file | Check `ls essentials/<NN>/lessons/` |

---

## The Token Router plugin (optional)

The Token Router is an optional Hermes plugin that **narrows the tool
surface** shown to the agent — not to the student. When enabled, the
agent sees fewer tools by default, which can reduce token usage and
keep the agent focused on theEight Essentials work.

It does **not** hide features from the student. The student can still
ask anything; the router only affects what the agent chooses from
automatically.

Enable it if:
- You want to keep the agent focused on teaching, not on code or data analysis.
- Token usage is a concern.

Leave it off if:
- The student (or parent) wants the full tool surface available.

To enable: `hermes plugins enable hermes-token-router` (after
`hermes profile use buildwithjesus-agent`).

---

## License

MIT — see `LICENSE`.

The Build with Jesus Agent persona is an original assistant archetype
written for this project. The Eight Essentials guide content is from
the onetoeight *Eight Essentials* Universal Edition V.3.0.0, included
with permission for use inside this profile.
