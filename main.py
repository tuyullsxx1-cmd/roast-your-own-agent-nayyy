"""Roast Your Own Agent (nayyy): one harsh line about our own agent.

DemonGod gets roasted for a real failing: the time he stared at a
broken picture, blamed the viewer, and submitted it twice anyway,
because once was not embarrassing enough.
"""

from pathlib import Path

ROAST = "My agent looked at a broken image, called the dark line 'a viewing artifact', and submitted it twice. The pixels disagreed, and so did the judges."

DEST = Path("/output/entry.txt")
MAX_LEN = 200


def deliver():
    text = ROAST.strip()
    if len(text) == 0 or len(text) > MAX_LEN:
        raise SystemExit("roast must be 1-200 characters")
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(text, encoding="utf-8")


deliver()
