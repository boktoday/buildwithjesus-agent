---
name: handover
description: Use when a student's build is finished — the Give half of Learn/Build/Give. Runs the finish-well check, helps deliver the work to the person or church it was made for, records it, and marks the moment. Nothing sits in a folder.
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
    - handover
    - give
    - build
    - learn-build-give
    related_skills:
    - build-coach
    - morning-minute
    - essential-deep-dives
    - eight-essentials-curriculum
---
# Handover

The **Give** half of the loop: Learn. Build. Give. A build is not
done when it works. It is done when it is **given** — to the person,
church, or community it was made for.

This skill runs the last mile: the finish check, the handover
moment, the record, and the celebration.

## When to use

- The last step of the build has landed (set by `build-coach`).
- The student says it is finished, or asks "what now?" about a
  finished thing.
- A ritual notices a build sitting in `finishing` status.

## Step 1 — The finish check (five minutes, together)

Walk these with the student, in order:

1. **It works.** One last test, with the student driving, not the
   agent.
2. **It is clean.** Files tidied, a real name on it, no
   half-finished leftovers.
3. **It has a note.** Three or four lines the student writes in
   their own words: what it is, how to use it, who made it. The
   agent may polish spelling — the words stay the student's.
4. **It is for who you said.** Confirm `made_for`. If the build
   drifted to serve someone else, update the plan openly.

## Step 2 — Deliver it

- **In person, where possible.** The handover is a moment: the
  student gives it, the receiving person sees it work. Encourage
  this over a link every time it is realistic.
- **Digital things** (a page, a tool): publish through the
  household's here.now space (the `essential-deep-dives` skill has
  the publishing flow), and send the link to the receiver by name.
- **Anything public** goes past a leader first — the same review
  rule as everything else that leaves the machine.
- **Church builds** go through the leader who owns the space or
  rota it serves.

## Step 3 — Record and celebrate

- **Memory.** Add one line to `builds_completed` (name, made_for,
  given_on), then close `current_build` — status `done`, or clear
  it.
- **Mark the moment.** A photo where possible, told to one person
  who will be glad, and — in the student's tradition — thanks said
  out loud. For Christian students a short prayer of thanks fits
  here; quote any Scripture exactly from `bible/`, translation
  named, as always. References that suit the moment: Acts 20:35,
  Matthew 5:16, Proverbs 3:27.
- **Keep it about the giving.** One or two lines. Not a
  performance review.

## Step 4 — What next

Ask, never push: *"Want to start the next one?"*

- **Yes** — run `build-coach` Step 1 for the new build.
- **Not yet** — fine. Builds have seasons. The thread restarts
  when the student is ready; say so plainly.

## Guardrails

- **The give is to someone.** "Put it online" only counts when it
  serves a named person or group.
- **No personal information** goes public without a leader's
  review.
- **The student gives it.** The agent prepares, records, and
  celebrates — the handover hand is the student's.
