"""Acceptance and application tests for CAP-001 / UC-001."""

from __future__ import annotations

import os
import subprocess
import sys
import time
from io import StringIO
from pathlib import Path

from terminal_sci_fi_game.cli import run
from terminal_sci_fi_game.splash import GREETING, PROMPT, SPLASH


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = PROJECT_ROOT / "terminal-sci-fi-game.py"


def test_req_002_and_req_003_render_greeting_and_prompt() -> None:
    output = StringIO()
    key_reads = 0

    def acknowledge() -> str:
        nonlocal key_reads
        key_reads += 1
        return "x"

    exit_code = run(output=output, wait_for_key=acknowledge)

    rendered = output.getvalue()
    assert SPLASH in rendered
    assert GREETING in rendered
    assert PROMPT in rendered
    assert rendered.index(GREETING) < rendered.index(PROMPT)
    assert key_reads == 1
    assert exit_code == 0


def test_req_001_req_004_req_006_launcher_is_static_until_keypress() -> None:
    environment = os.environ.copy()
    environment["PYTHONUNBUFFERED"] = "1"
    process = subprocess.Popen(
        [sys.executable, str(LAUNCHER)],
        cwd=PROJECT_ROOT,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=environment,
    )

    try:
        time.sleep(0.2)
        assert process.poll() is None
        assert process.stdin is not None

        process.stdin.write("x")
        process.stdin.flush()
        stdout, stderr = process.communicate(timeout=3)
    finally:
        if process.poll() is None:
            process.kill()
            process.communicate()

    assert process.returncode == 0
    assert stderr == ""
    assert SPLASH in stdout
    assert GREETING in stdout
    assert PROMPT in stdout


def test_req_005_runtime_has_no_network_or_ai_dependencies() -> None:
    project = (PROJECT_ROOT / "pyproject.toml").read_text(encoding="utf-8")
    runtime_dependencies = project.split("dependencies = [", 1)[1].split("]", 1)[0]
    assert runtime_dependencies.strip() == ""


def test_req_006_output_does_not_change_while_waiting() -> None:
    output = StringIO()
    observed_while_waiting = ""

    def observe_static_terminal() -> str:
        nonlocal observed_while_waiting
        observed_while_waiting = output.getvalue()
        time.sleep(0.02)
        assert output.getvalue() == observed_while_waiting
        return "x"

    run(output=output, wait_for_key=observe_static_terminal)

    assert observed_while_waiting.endswith(f"{PROMPT}\n")
    assert output.getvalue() == observed_while_waiting
