"""bwj-commands - guided-ritual slash commands for the Build with Jesus Agent.

Six in-session commands, each one starting the matching skill flow in the
live conversation:

    /morning   today's Morning Minute          (morning-minute skill)
    /prayer    today's Morning Prayer          (morning-prayer skill)
    /checkin   today's Afternoon Check-In      (afternoon-checkin skill)
    /tomorrow  tonight's Planning Session      (planning-session skill)
    /passage   tonight's Night Passage         (night-passage skill)
    /build     the Build Round                 (build-project skill)

How it works: the handler injects a short user-style instruction into the
current session, so the agent opens the right skill and runs the flow in
the normal way - consent, tradition and voice rules all still apply. The
commands are shortcuts only; students can always just ask in a sentence.

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
    "skill and deliver the audio + text here. If my tradition is not "
    "Christian, say so gently instead."
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

_BUILD_ALIASES = {
    "start": "start", "new": "start", "idea": "start",
    "keep": "keep", "continue": "keep", "building": "keep", "go": "keep",
    "finish": "finish", "done": "finish", "give": "finish", "giveaway": "finish",
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


def register(ctx) -> None:
    """Register the six guided commands."""
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
    ctx.register_command(
        "build", lambda raw: _handle_build(ctx, raw),
        description="Build round: start, keep going, or finish a project",
        args_hint="<start|keep|finish>",
    )
