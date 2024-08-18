import os
import platform
from pathlib import Path

from gaveta.json import ensure_json, read_json, write_json
from gaveta.seq import replace_or_append

DATA = Path("data") / "terminals.json"


def compare_terminals(terminal, new_terminal) -> bool:
    return (
        terminal["TERM_PROGRAM"] == new_terminal["TERM_PROGRAM"]
        and terminal["os"] == new_terminal["os"]
    )


if __name__ == "__main__":
    ensure_json(DATA)
    terminal_data = read_json(DATA)

    new_terminal = {
        "COLORTERM": os.getenv("COLORTERM"),
        "TERM": os.getenv("TERM"),
        "TERM_PROGRAM": os.getenv("TERM_PROGRAM"),
        "TERM_PROGRAM_VERSION": os.getenv("TERM_PROGRAM_VERSION"),
        "os": platform.platform(aliased=False, terse=False),
    }

    terminal_data = replace_or_append(terminal_data, new_terminal, compare_terminals)

    write_json(terminal_data, DATA)
