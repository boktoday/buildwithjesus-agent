"""bwj-commands - guided slash commands for the Build with Jesus Agent.

Sixteen in-session commands, each one starting the matching skill flow in
the live conversation:

    /morning   today's Morning Minute          (morning-minute skill)
    /prayer    today's Morning Prayer          (morning-prayer skill)
    /checkin   today's Afternoon Check-In      (afternoon-checkin skill)
    /tomorrow  tonight's Planning Session      (planning-session skill)
    /passage   tonight's Night Passage         (night-passage skill)
    /build     the Build Round                 (build-project skill)
    /summary   an essential's key points + voice note   (essential-deep-dives, Format 1)
    /lesson    a three-page HTML lesson with a quiz     (essential-deep-dives, Format 2)
    /poem      a rhyming spoken-word poem               (essential-deep-dives, Format 3)
    /song      an original song (~$0.08, spend confirmed first)   (Format 4)
    /video     a music video (~$0.35, spend confirmed first)      (Format 5)
    /question  one of the twenty prompts, to sit with   (prompts.md)
    /ideas     brainstorm things to build or do         (guide activities + build-project)
    /guide     the guide edition link, online + offline pack
    /outreach  find a real need to build for    (outreach skill)
    /recap     the weekly review                (weekly-review skill)

How it works: the handler injects a short user-style instruction into the
current session, so the agent opens the right skill and runs the flow in
the normal way - consent, spend and voice rules all still
apply. The commands are shortcuts only; students can always just ask in a
sentence.

Gateway (Telegram/WhatsApp) injection requires a one-time consent entry
in the profile config:

    plugins:
      entries:
        bwj-commands:
          allow_gateway_injection: true

CLI sessions work without that entry.
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)

_FALLBACK = (
    "I could not start that flow from here just now. "
    "Just ask me in a sentence instead - for example, \"run my Morning Minute\"."
)

# Prompts injected into the session. Written in the student's voice so the
# conversation reads naturally; the skill names make the routing explicit.
_MORNING = (
    "Run today's Morning Minute now, please - follow the morning-minute "
    "skill (pick up from the archive, generate the audio + text, and "
    "deliver both here)."
)
_PRAYER = (
    "Run today's Morning Prayer now, please - follow the morning-prayer "
    "skill and deliver the audio + text here."
)
_CHECKIN = (
    "Run today's Afternoon Check-In now, please - follow the "
    "afternoon-checkin skill."
)
_TOMORROW = (
    "Run tonight's Planning Session now, please - follow the "
    "planning-session skill, and open with the Build Round question."
)
_PASSAGE = (
    "Run tonight's Night Passage now, please - follow the night-passage "
    "skill and deliver the audio + text here."
)

_SUMMARY = (
    "Deep dive time: make me an Essential Summary - the key points plus a "
    "3 to 5 minute voice note. If I have not said which essential, ask me "
    "first. Follow the essential-deep-dives skill, Format 1."
)
_LESSON = (
    "Deep dive time: make me an Essential Lesson - the three-page HTML "
    "lesson with cited sources and a quiz, published and sent as a link. "
    "If I have not said which essential, ask me first. Follow the "
    "essential-deep-dives skill, Format 2."
)
_POEM = (
    "Deep dive time: write me an Essential Poem - a rhyming spoken-word "
    "poem, delivered as a voice note with the text below. If I have not "
    "said which essential, ask me first. Follow the essential-deep-dives "
    "skill, Format 3."
)
_SONG = (
    "Deep dive time: make me a song about an essential. First confirm the "
    "cost with me (about eight cents through OpenRouter) and only then "
    "run it - follow the essential-deep-dives skill, Format 4. If I have "
    "not said which essential, ask me first."
)
_VIDEO = (
    "Deep dive time: make me a music video for an essential. First confirm "
    "the cost with me (about thirty-five cents in total) and only then run "
    "it - follow the essential-deep-dives skill, Format 5. If I have not "
    "said which essential, ask me first."
)

_IDEAS = (
    "Brainstorm with me: give me a few concrete, small ideas - things I "
    "could build or do this week, for me, my community, or my church. "
    "Base them on my interests and the guide's activities "
    "(essentials/<NN>/activities/). If one grabs me, we can take it into "
    "the build-project flow."
)
_GUIDE = (
    "Share my guide: send the link for my language's edition of the "
    "one-to-eight guide - the read-online link and the offline pack. See "
    "essentials/guide-editions.md."
)
_OUTREACH = (
    "Outreach time: walk me through the outreach workflow - follow the "
    "outreach skill. Help me build my target list (community hubs, my "
    "school, our church), draft the first message for an adult to check, "
    "then the discovery questions for whoever I reach. We are offering to "
    "build something small, free, and hand it over as a gift."
)
_RECAP = (
    "Run my Weekly Review now, please - follow the weekly-review skill: "
    "read this week's archives, the build record and the outreach log, "
    "then give me the short recap - what I learned, built and gave, one "
    "win, and one thing for next week. If it has been a quiet week or I "
    "have been away, use the gentle comeback."
)

_BUILD_ALIASES = {
    "start": "start", "new": "start", "idea": "start",
    "keep": "keep", "continue": "keep", "building": "keep", "go": "keep",
    "finish": "finish", "done": "finish", "give": "finish", "giveaway": "finish",
}

_QUESTION_GROUPS = {
    "tired": "tired / low", "low": "tired / low",
    "wired": "wired / curious", "curious": "wired / curious",
    "stuck": "stuck or flat", "flat": "stuck or flat",
    "think": "want to think", "do": "want to do",
}


def _session_key() -> str | None:
    """The live gateway session key, when a gateway bound this handler."""
    try:
        from gateway.session_context import get_session_env
        return get_session_env("HERMES_SESSION_KEY", "") or None
    except Exception:
        return None


def _start(ctx, prompt: str) -> str | None:
    """Inject `prompt` into the live session. None on success (the agent's
    own turn replies); a gentle fallback string when no host accepted it."""
    for session_key in (_session_key(), None):
        try:
            if ctx.inject_message(prompt, session_key=session_key):
                return None
        except Exception:
            logger.warning("bwj-commands: inject_message failed", exc_info=True)
    return _FALLBACK


def _handle_build(ctx, raw_args: str) -> str | None:
    arg = (raw_args or "").strip().lower()
    door = _BUILD_ALIASES.get(arg.split()[0] if arg else "", None)
    if door == "start":
        prompt = ("Build round: I want to start a new project. Follow the "
                  "build-project skill, Door 1 - find the need, choose the "
                  "medium, define done.")
    elif door == "keep":
        prompt = ("Build round: let's keep my project going. Follow the "
                  "build-project skill, Door 2 - read build-project.md, name "
                  "today's step, and let's make it.")
    elif door == "finish":
        prompt = ("Build round: time to finish and give it away. Follow the "
                  "build-project skill, Door 3, then the handover skill.")
    elif arg and not door:
        prompt = ("Build round: I want to start a project - here's the idea: "
                  f"{raw_args.strip()}. Follow the build-project skill, Door 1.")
    else:
        prompt = ("Build round: ask me the question - are we starting "
                  "something new, keeping one going, or finishing and giving "
                  "one away? Then follow the build-project skill for whichever "
                  "I pick.")
    return _start(ctx, prompt)


def _handle_question(ctx, raw_args: str) -> str | None:
    arg = (raw_args or "").strip()
    low = arg.lower()
    if not arg:
        prompt = ("Give me one of the twenty prompts that fits today - read "
                  "essentials/00-introduction/lessons/prompts.md, pick one "
                  "that suits my day, ask it in my voice, and hold space for "
                  "my answer. Follow up with one small action.")
    elif arg.isdigit():
        prompt = (f"Give me prompt number {arg} from the twenty prompts "
                  "(essentials/00-introduction/lessons/prompts.md) - read it "
                  "from the file, ask it in my voice, and hold space for my "
                  "answer.")
    elif low in _QUESTION_GROUPS:
        prompt = (f"Pick a prompt for me from the '{_QUESTION_GROUPS[low]}' "
                  "group in the twenty prompts "
                  "(essentials/00-introduction/lessons/prompts.md), ask it in "
                  "my voice, and hold space for my answer.")
    else:
        prompt = ("Give me a prompt from the twenty prompts "
                  "(essentials/00-introduction/lessons/prompts.md) that fits "
                  f"this: {arg}. Ask it in my voice, and hold space for my "
                  "answer.")
    return _start(ctx, prompt)


def register(ctx) -> None:
    """Register the guided commands."""
    # The day's rhythm
    ctx.register_command(
        "morning", lambda raw: _start(ctx, _MORNING),
        description="Run today's Morning Minute now (audio + text)",
    )
    ctx.register_command(
        "prayer", lambda raw: _start(ctx, _PRAYER),
        description="Run today's Morning Prayer now (audio + text)",
    )
    ctx.register_command(
        "checkin", lambda raw: _start(ctx, _CHECKIN),
        description="Run today's Afternoon Check-In now",
    )
    ctx.register_command(
        "tomorrow", lambda raw: _start(ctx, _TOMORROW),
        description="Run tonight's Planning Session (plans tomorrow)",
    )
    ctx.register_command(
        "passage", lambda raw: _start(ctx, _PASSAGE),
        description="Run tonight's Night Passage now (audio + text)",
    )
    # The build track
    ctx.register_command(
        "build", lambda raw: _handle_build(ctx, raw),
        description="Build round: start, keep going, or finish a project",
        args_hint="<start|keep|finish>",
    )
    # Essential deep dives
    ctx.register_command(
        "summary", lambda raw: _start(ctx, _SUMMARY),
        description="Essential summary: key points + a voice note",
    )
    ctx.register_command(
        "lesson", lambda raw: _start(ctx, _LESSON),
        description="Essential lesson: a three-page page with a quiz",
    )
    ctx.register_command(
        "poem", lambda raw: _start(ctx, _POEM),
        description="Essential poem: a spoken-word poem (audio + text)",
    )
    ctx.register_command(
        "song", lambda raw: _start(ctx, _SONG),
        description="Essential song: an original song (costs ~8c, confirms first)",
    )
    ctx.register_command(
        "video", lambda raw: _start(ctx, _VIDEO),
        description="Essential music video (costs ~35c, confirms first)",
    )
    # Questions and ideas
    ctx.register_command(
        "question", lambda raw: _handle_question(ctx, raw),
        description="One of the twenty prompts, to sit with",
        args_hint="<number|tired|wired|stuck|think|do>",
    )
    ctx.register_command(
        "ideas", lambda raw: _start(ctx, _IDEAS),
        description="Brainstorm things to build or do",
    )
    # The guide itself
    ctx.register_command(
        "guide", lambda raw: _start(ctx, _GUIDE),
        description="Send the guide: read online + offline pack",
    )
    # Finding a need
    ctx.register_command(
        "outreach", lambda raw: _start(ctx, _OUTREACH),
        description="Find a real need to build for (community outreach)",
    )
    # The weekly look-back
    ctx.register_command(
        "recap", lambda raw: _start(ctx, _RECAP),
        description="Your week in review: learned, built, gave",
    )
