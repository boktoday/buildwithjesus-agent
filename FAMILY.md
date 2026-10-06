# For parents and guardians

One page. What this is, what it isn't, and how to see everything.

## What this is

An **assistant** for a young person. It runs a gentle daily rhythm
(a short morning plan, an afternoon check-in, an evening plan), it
teaches from the Eight Essentials guide, and it helps your young
person build real things - skills, homework help, and real projects
they give away to your church or community.

It is a **tool, not a friend**. The rule it lives by: **an
assistant, not a companion.** It is a thought partner, build
partner, researcher and teacher - and it says so plainly, at setup
and regularly.

## What it isn't

It is **not a counsellor** and never pretends to be one. It gives
no advice on mental health, health, medication, relationship
crises, or big personal decisions. On anything serious - their own
or someone else's - it pauses, says so kindly, and points them to a
real person: you, a trusted adult, a leader, a school counsellor, a
doctor - plus helplines. It never promises secrecy on something
serious. (The full policy lives in
`skills/profile/hard-moments/`; the helpline list is in
`skills/profile/hard-moments/references/helplines.md` and is meant
to be edited for your country.) After a hard moment it also
schedules short **care follow-ups** - gentle one-line check-ins
roughly 3 hours, 8 hours and 24 hours later - so your young person
is not left alone with it. Three touches, then space; never a nag.

It is also not a babysitter, a screen-time police officer, or a
replacement for church, family, or friends. Its whole purpose is to
send your young person back into the real world.

## Where everything lives (all local)

Everything the agent produces sits in the profile folder on this
machine:

- `morning-minute-archive.md` - every daily plan
- `morning-prayer-archive.md`, `night-passage-archive.md` -
  the optional rhythms
- `planning-session-archive.md` - the nightly plans
- `build-project.md`, `builds-archive.md` - what they're building
  and what they've given away
- `outreach-log.md` - who they've reached out to, and what was
  said
- `spend-log.md` - every paid extra, with a running total

The only things that leave the machine: the model provider (to
generate replies), the web-search service (when a search is asked
for), and any page you choose to publish (e.g. here.now). Memory is
local-first (Mnemosyne).

## How to see everything

Open any archive file - they are plain markdown, readable in any
editor. A good rhythm: read one together once a week and ask what
they thought of it. The records exist so you can be involved, not
so you can audit.

## Your controls

- **Pause anything:** every rhythm is a scheduled job -
  `hermes --profile buildwithjesus-agent cron list`, then
  `cron pause <id>`. Nothing runs that you haven't seen listed.
- **Cap spending:** set a number on the cap line of `spend-log.md`.
  The agent checks it before any paid extra.
- **Edit the helplines** for your country (see the path above).
- **Delete anything** - it is all local files.

## Spending

The daily rhythm costs a few dollars a month. Paid extras (a song,
a music video) confirm the cost with your young person first, and
every one is logged in `spend-log.md`. Typical running cost:
$5-10 a month.

## First week

Three suggestions:

1. Sit in on one session - just watch what it says.
2. Read one archive together, out loud, in the evening.
3. Ask what they are building. Then ask who it is for.
