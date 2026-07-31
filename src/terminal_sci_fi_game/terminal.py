"""Terminal input primitives kept separate from presentation and game logic."""

from __future__ import annotations

import os
import sys
from typing import TextIO


def read_key(stream: TextIO = sys.stdin) -> str:
    """Read one character without requiring Enter on an interactive terminal.

    Redirected streams use their normal one-character read, which keeps the
    behavior deterministic and allows acceptance tests to drive the process.
    """

    if stream is not sys.stdin or not stream.isatty():
        return stream.read(1)

    if os.name == "nt":
        import msvcrt

        return msvcrt.getwch()

    import termios
    import tty

    descriptor = stream.fileno()
    previous_settings = termios.tcgetattr(descriptor)
    try:
        tty.setraw(descriptor)
        return stream.read(1)
    finally:
        termios.tcsetattr(descriptor, termios.TCSADRAIN, previous_settings)
