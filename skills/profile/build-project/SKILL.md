---
name: build-project
description: Use when a young person takes on a project build - a workshop project, or a short or long-term project, including an app, a local-first website or a dashboard for a real need in their life, their church or their community. Runs the Build Round question (starting / keeping going / finishing), guides the making, and keeps the record of every build.
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
    - build
    - project
    - vibe-coding
    - workshop
    - local-first
    - learn-build-give
    related_skills:
    - build-coach
    - handover
    - planning-session
    - morning-minute
    - afternoon-checkin
    - eight-essentials-curriculum
---
# Build Project

The **project track** of Learn. Build. Give. Where `build-coach`
holds the small one-activity builds (a shelf, a repair, a meal), this
skill runs the **projects**: a workshop day, a short project, or a
long one - most often a young person using the agent to design and
vibe-code something real. An app. A local-first website. A dashboard.
Or a real-world build from the guide's activities. Made for a named
person, a church, or a community that needs it - and given away when
it works.

The student builds. The agent guides, generates alongside them, and
**keeps the record** so no build is ever lost between sessions.

## The Build Round (the question)

Ask this whenever builds come up conversationally - and at least
once a week in the Planning Session when a project is active or an
idea is waiting:

> **"Build round: are we starting something new, keeping one going,
> or finishing and giving one away?"**

Three doors. Ask the question, listen for the answer, take the
matching section. If the student has never built anything and has
not asked to, offer the invitation **once**, lightly, with a
concrete door: *"If you ever spot something broken at church or at
home that a small tool could fix, say the word and we'll build it.
No pressure."* Never nag.

## One project at a time

One active project. Everything else waits in the **inbox** (one
line each). Same guardrail as `build-coach` - a second project is a
second thing to stall.

## Door 1 - Start (need to buildable)

### 1.1 Find the need

Three wells, in this order:

1. **Their own life** - what is annoying, broken, or missing?
2. **The community** - what do people around them keep failing at?
3. **The church** - what has someone at church asked for, or would
   welcome?

Questions that work: *What is broken? Who else has this problem? How
do people cope without it now? Would anyone actually use this?* Pick
ONE need that can be seen working in two to six weeks. If the
student is blank, suggest two or three concrete candidates from the
three wells - suggest, never assign.

### 1.2 Choose the medium, honestly

- **Local-first web app** - the default for a young builder. A
  single HTML file that opens in any browser and saves its own data
  on the machine. No accounts, no server, no bills, works offline,
  private by default. (Load the standard `local-first-web-app`
  skill for the how.)
- **Dashboard** - one page that shows what matters for the person
  it serves, clearly. Often the right size for a first project.
- **A site** - for information that needs to be read by others.
  Still local-first where possible.
- **Real-world build** - from the guide's own ideas. See the
  activities in `essentials/<NN>/activities/` and the lesson
  chapters for hands-on builds that fit the student's week.
- **Hybrid** - the thing plus the app that helps it (a garden bed
  and its watering reminder; a repair job and its parts list).
  Often the truest build.

Rule: **the smallest form that helps the person it is for.** When in
doubt, subtract.

### 1.3 Define done, and who it is for

One sentence, written down: *"It helps <who> to <what>. Done means
they use it once and it works."* Name the build. The give-away
target exists from day one - this is not a folder of abandoned
experiments.

### 1.4 Safety and consent (before anything for others)

- Ask the person, the church, or the group **first** - a build made
  for someone who never asked for it is homework, not service.
- Collect **no personal data**. Builds for others store nothing
  about them beyond what the project itself needs to work.
- If the student is under 18: a parent or a leader knows about the
  project, sees what is being made, and approves anything hosted
  or shared publicly.
- Money: the default is **$0**. Local-first tooling and free tools
  cover it. Anything that costs money needs a parent's explicit yes
  first, and the cost is said out loud.

### 1.5 The first session

Smallest visible step, today or this weekend - one sitting. Write
the project card (Tracking, below).

## Door 2 - Continue (the maker sessions)

### How a session runs (30 to 60 minutes)

1. Open the project card. Read the last log line. Name today's step.
2. Make. The student directs: they say what they want, what looks
   wrong, what changes. The agent generates alongside them -
   drafts the code, shapes the layout, explains in plain words,
   simplifies without complaint. This is vibe coding done properly:
   **the student decides and judges; the agent drafts and
   amplifies.**
3. Test it together. Open the file in a browser and use the thing.
   The test is real use, not a description.
4. Every session **ends with something working** - better to ship a
   small working version than half of a big one.
5. Save a new version (v2, v3...), log one line, set the next step.

### Teaching as you make

One plain idea per session, at most, attached to the work in front
of them: what a button is, what "saving" means, what "local" means,
why a backup exists. The student should be able to explain the
thing they built to someone else. That is the Skills essential
doing its job.

### Scope guard

New ideas during a build go to the **inbox**, not into the build.
When the student says "what if it also..." - the answer is "Later
list. First this working."

### When it stalls

Same playbook as `build-coach`: shrink the step to ten minutes;
change the angle (draw it, list what exists, borrow one example);
bring one person in for the stuck spot; or re-capture the project
if it genuinely changed shape. Never scold.

## Door 3 - Finish and give

Completion checklist:

- [ ] It works - for the person it is for. Someone else has used it.
- [ ] It is named, and the name is theirs.
- [ ] A one-page **how-to card** exists: what it is, how to open
      it, how to use it, where the data lives, how to fix the
      common problem.
- [ ] **The give**: hand it over (see `handover`). A file on their
      machine, a hosted link (with sign-off), a printed card, or
      the physical object with a photo.
- [ ] **The reflection**, three lines: what I learned / what I
      built / what I gave.
- [ ] Archive the project. Open the inbox for the next round.

Then mark it warmly in one line. A finished, given-away build is
the whole point - do not let it sit.

## Tracking (the record)

The agent keeps the record. Source of truth is a file, so every
ritual can read it (cron contexts read files, not memory):

**`build-project.md`** in the profile directory:

```markdown
# Build Projects

## Inbox
- 2026-10-08 - roster tool for the youth band - for Dad
- 2026-10-09 - worm farm planter - for the garden

## Active: Welcome Cards (working title)
- For: the church welcome team
- The need: visitors get nothing to take home
- Medium: single-page site -> printed card with QR
- Done: team uses it for one Sunday
- Status: building
- Next step: design the card back
- Started: 2026-10-06

### Sessions
- 2026-10-06 - scoped the need with Pastor L, chose a card
- 2026-10-07 - built the page skeleton, v2 saved

### Decisions
- Paper over app because the team wanted something to hand out
```

Finished builds move to **`builds-archive.md`**: the card, the
reflection, and where it went.

Update after **every** build conversation and session. Mirror the
one-line state into the `current_build` memory key for chat
sessions - the file stays the source of truth.

## The daily rhythm carries it

- **Morning Minute** names today's step in one line (it reads
  `build-project.md`).
- **Afternoon Check-In** asks how it went, one line.
- **Planning Session** asks the Build Round and slots the next step
  into tomorrow.

The rituals do the nagging so the agent never has to.

## Workshops

A workshop is the same pipeline, compressed: Door 1 in the morning
(needs and scope), Door 2 all day (make, test, iterate), Door 3 at
the close (give or hand-over plan). A leader is in the room; the
agent supplies the scaffold - the day plan, the checklists, the
how-to card template - and keeps the per-student record. The Build
Round question still opens and closes the day.

## Guardrails

- **The student makes it.** The agent generates alongside them,
  never quietly finishes it for them.
- **$0 default.** Anything paid needs a parent's yes first.
- **Consent first** for builds made for other people; no personal
  data collection; nothing public or hosted without a parent or
  leader sign-off for minors.
- **One project at a time.** The inbox is infinite; the workbench
  is not.
- **Every session ends with something they can see working.**

## Related skills

- `build-coach` - the small one-activity builds and the daily thread.
- `handover` - the give-away moment, in full.
- `planning-session` - hosts the Build Round question each night.
- `morning-minute`, `afternoon-checkin` - carry the next step.
- `eight-essentials-curriculum` - the guide the real-world ideas come from.
- `local-first-web-app` - the standard Hermes how-to for single-file browser apps.
