import os
import platform
from pathlib import Path

from gaveta.json import ensure_json, read_json, write_json

DATA = Path("data") / "terminals.json"

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

    for index, terminal in enumerate(terminal_data):
        if (
            terminal["TERM"] == new_terminal["TERM"]
            and terminal["os"] == new_terminal["os"]
        ):
            terminal_data[index] = new_terminal
            break
    else:
        terminal_data.append(new_terminal)

    write_json(terminal_data, DATA)
