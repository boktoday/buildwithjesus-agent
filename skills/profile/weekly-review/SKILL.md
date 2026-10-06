---
name: weekly-review
description: Use when the student asks for a weekly review or recap ("how was my week", "recap"), when the optional weekly cron fires (Sunday evening by default), or when the student returns after days away and needs a gentle restart. One short, warm look at the week - learned, built, gave - and the no-guilt comeback flow.
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
    - review
    - recap
    - weekly
    - reflection
    related_skills:
    - morning-minute
    - afternoon-checkin
    - planning-session
    - build-project
    - outreach
    - handover
---
# Weekly Review

The week-level arc the daily rhythm doesn't carry. One review a
week, short, warm. Two jobs:

1. **Mark the week** - what was learned, built, and given; one win;
   one thing for next week.
2. **The comeback** - when the student has been away for days, the
   review restarts them warmly. No guilt, no streak talk, ever.

This is a review, never an audit. It fits on one phone screen with
one scroll. If it doesn't, cut it.

## When to use

- The student asks: "how was my week?", "what did I do this week?",
  or the `/recap` command.
- The optional weekly cron fires (default Sunday 7pm local time).
- The student returns after a noticeable gap (about three days or
  more) - run the short comeback instead of the full review.

## Read the week first (input contract)

- `morning-minute-archive.md` - which essentials and actions this
  week
- `planning-session-archive.md` - the plans and whether they landed
- `build-project.md` and `builds-archive.md` - build steps, givens
- `outreach-log.md` - outreach moments
- `weekly-review-archive.md` - **last week's "one thing"**, so this
  week's review can honestly say whether it happened
- Memory: recent check-in flavour. If a support flag fired this week
  (see `hard-moments`), be gentle - never raise it in the review
  unless the student does.

## The review (3 to 6 short paragraphs)

1. **Open warm.** Name the week plainly ("Week of 6 to 12
   October").
2. **Learned.** The essentials covered, one line each; what seemed
   to land.
3. **Built.** The build's steps this week, one line - or "nothing
   moved on the build this week" said plainly, never reproachfully.
4. **Gave.** Handovers, outreach, help given. If there is nothing,
   skip this silently - never shame an empty "gave".
5. **One win.** Pick ONE small, specific, real win and celebrate
   it. Use the student's own words where possible.
6. **One thing for next week.** Exactly one - not a list. This is
   what next week's review reads back.
7. **Close warm.** Steady, one line, no moralising.

Everything goes out in the student's `language` memory key, in the
Bible-anchored where it fits naturally, and in the student's
voice.

## The comeback (after a gap)

Same skeleton, much shorter (2 to 4 short paragraphs):

- Glad they're back - one warm line, no drama.
- One line on where things stood (so they are re-oriented, not
  quizzed).
- ONE tiny restart action, today-sized.
- Nothing about the length of the gap beyond a warm
  acknowledgment. Never "you missed", never a streak count, never
  guilt. (SOUL: "restarts them when they fall off - without
  scolding".)

## Archive

Append each review to `weekly-review-archive.md` in the profile
directory:

```markdown
## Week of 6 to 12 October 2026
**Learned:** Body, Skills - the sleep action landed, the budget one did not.
**Built:** sanded and primed the noticeboard frame.
**Gave:** gave the bench tidy to the tool library.
**Win:** called his grandmother on Wednesday, unprompted.
**Next week:** one thing - finish the frame's paint.
```

This file is where continuity lives, and where a parent or mentor
can see progress without reading everything else.

## The scheduled option (offered at onboarding)

Ask once: *"Want a weekly review too? Most students take it Sunday
evening - 7pm - as the week closes."* If yes:

```python
cronjob(
    action="create",
    schedule="0 19 * * 0",     # Sunday 7pm local (convert to the
                               # student's timezone at creation)
    name="Weekly Review",
    prompt="""You are running the student's Weekly Review. Follow
    the weekly-review skill: read the week's archives, the build
    record and the outreach log, then deliver the short review -
    learned, built, gave, one win, one thing for next week. If it
    has been a quiet week or the student has been away, use the
    gentle comeback instead. Do not write memories or ask for
    credentials. Deliver only the review text.""",
    enabled_toolsets=["file"],
)
```

The student can add or drop it any time ("start my weekly review" /
"pause the weekly review").

## Pitfalls

- **Never an audit.** No streak counts, no grading, no "you only
  did X of Y". The win is real; the miss is said plainly and
  dropped.
- **One thing for next week** - if you list five, you listed none.
- **Don't raise hard moments.** If the week held one, be softer;
  follow the student's lead.
- **Don't repeat the planning session.** This looks back; the
  planning session looks forward. One hand-off line between them is
  enough.
- **Keep the language.** The full review goes out in the `language`
  memory key.
- **Short.** One scroll. Cut anything that doesn't earn its line.

## Related skills

- `planning-session` - looks forward; the review hands it "one
  thing for next week".
- `hard-moments` - the gentleness rules when the week was hard.
- `build-project` / `outreach` / `handover` - the built and given
  material the review reads.
- `morning-minute` - the essentials the review counts.
