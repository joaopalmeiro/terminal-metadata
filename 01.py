import os
import platform
from collections.abc import Callable
from pathlib import Path
from typing import TypeVar

from gaveta.json import ensure_json, read_json, write_json

DATA = Path("data") / "terminals.json"

T = TypeVar("T")


def replace_or_append(
    values: list[T], new_value: T, key: Callable[[T, T], bool]
) -> list[T]:
    for index, value in enumerate(values):
        if key(value, new_value):
            values[index] = new_value
            break
    else:
        values.append(new_value)

    return values


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
