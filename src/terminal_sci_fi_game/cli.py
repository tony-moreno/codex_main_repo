"""Application boundary for the initial terminal greeting use case."""

from __future__ import annotations

import sys
from collections.abc import Callable
from typing import TextIO

from terminal_sci_fi_game.splash import GREETING, PROMPT, SPLASH
from terminal_sci_fi_game.terminal import read_key


def run(
    *,
    output: TextIO = sys.stdout,
    wait_for_key: Callable[[], str] = read_key,
) -> int:
    """Render the static greeting and wait for one uninterpreted keypress."""

    print(SPLASH, file=output)
    print(file=output)
    print(GREETING, file=output)
    print(PROMPT, file=output, flush=True)
    wait_for_key()
    return 0


def main() -> int:
    """Run the command-line application."""

    try:
        return run()
    except (EOFError, KeyboardInterrupt):
        return 0
