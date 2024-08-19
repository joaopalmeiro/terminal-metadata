# Notes

- https://github.com/joaopalmeiro/template-python-uv-script
- Screenshot app: [Screenshot (macOS)](https://support.apple.com/en-gb/guide/mac-help/mh26782/10.15/mac/10.15)
- [is-unicode-supported](https://github.com/sindresorhus/is-unicode-supported)
- `TERM_PROGRAM`, `TERM_PROGRAM_VERSION`, and `TERM` environment variables.
- [Support TERM_PROGRAM environment variables](https://github.com/mintty/mintty/issues/776) issue
- Table:
  - The `OS` column corresponds to the operating system where the script was run.
  - `-` represents the default value for _undefined_ environment variables.
- Hyper [themes](https://hyper.is/themes)
- Terminals or terminal emulators
- Warp [issues](https://github.com/warpdotdev/warp/issues)
- [CleanShot X](https://cleanshot.com/) (available via [Setapp](https://setapp.com/apps/cleanshot))
- [ZSH: Hide computer name in terminal](https://stackoverflow.com/a/59944342). `sudo code /private/etc/zshrc` + `%n@%m` -> `%n` (`PS1`). It works for Terminal (macOS).
- https://pypi.org/project/python-rapidjson/
- https://github.com/python-rapidjson/python-rapidjson
- https://docs.python.org/3.10/library/platform.html#platform.platform
- https://stackoverflow.com/questions/70574208/get-the-name-of-the-current-opened-application-in-python
- https://github.com/giampaolo/psutil/issues/173
- https://docs.python.org/3/library/os.html#os.getpid
- https://stackoverflow.com/questions/55349853/how-to-find-shell-environment-variable
- https://cli.r-lib.org/reference/num_ansi_colors.html:
  - "If the `COLORTERM` environment variable is set to `truecolor` or `24bit`, then we return 16 million colors."
  - https://cli.r-lib.org/articles/cli-config-internal.html#colorterm
  - https://cli.r-lib.org/articles/cli-config-internal.html#term
- https://github.com/vercel/hyper/blob/2a7bb18259d975f27b30b502af1be7576f6f5656/app/session.ts#L123-L131: `TERM`, `COLORTERM`, `TERM_PROGRAM`, and `TERM_PROGRAM_VERSION`
- https://docs.warp.dev/help/known-issues#configuring-and-debugging-your-rc-files: `$TERM_PROGRAM != "WarpTerminal"`
- https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops:
  - "In either kind of loop, the `else` clause is not executed if the loop was terminated by a `break`."
- https://docs.python.org/3.10/library/typing.html#typing.TypeVar
- https://mypy.readthedocs.io/en/stable/generics.html#generic-functions
- https://docs.python.org/3/library/typing.html#generics: "Changed in version 3.12: Syntactic support for generics is new in Python 3.12."
- https://docs.python.org/3.10/library/typing.html#typing.Callable
- https://www.nushell.sh/book/default_shell.html#setting-nu-as-default-shell-on-your-terminal
- https://github.com/cdleon/awesome-terminals

## Commands

```bash
pip config unset global.require-virtualenv
```

```bash
deactivate && uv venv .venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

```bash
uv venv .venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

### Clean slate

```bash
rm -rf .mypy_cache/ .ruff_cache/ .venv/
```

### Add a new terminal

```bash
cd ~/Documents/GitHub/terminal-metadata && source .venv/bin/activate && python 01.py && deactivate
```

### List all environment variables

```bash
printenv
```

### Alacritty

- https://alacritty.org/
- https://formulae.brew.sh/cask/alacritty
- https://github.com/alacritty/alacritty/issues/4673#issuecomment-771291615

```bash
brew update
```

```bash
brew install --cask alacritty --no-quarantine
```

```bash
brew uninstall --cask alacritty
```

### Nushell

- https://www.nushell.sh/

```bash
brew update
```

```bash
brew install nushell
```

```bash
brew uninstall nushell
```

### Hyper

- https://github.com/vercel/hyper?tab=readme-ov-file#macos
- https://formulae.brew.sh/cask/hyper

```bash
brew update
```

```bash
brew install --cask hyper
```

```bash
brew uninstall --cask hyper
```

### iTerm2

- https://iterm2.com/
- https://formulae.brew.sh/cask/iterm2

```bash
brew update
```

```bash
brew install --cask iterm2
```

```bash
brew uninstall --cask iterm2
```

### Tabby

- https://tabby.sh/
- https://formulae.brew.sh/cask/tabby

```bash
brew update
```

```bash
brew install --cask tabby
```

```bash
brew uninstall --cask tabby
```

### Wave

- https://github.com/wavetermdev/waveterm?tab=readme-ov-file#installation

```bash
brew update
```

```bash
brew install --cask wave
```

```bash
brew uninstall --cask wave
```

## Snippets

```python
from typing import TypeVar, Callable

T = TypeVar('T')

def replace_or_append(values: list[T], new_value: T, compare: Callable[[T, T], bool]) -> list[T]:
    for i, value in enumerate(values):
        if compare(value, new_value):
            values[i] = new_value
            return values

    values.append(new_value)
    return values
```

### `terminals/cheese.py` file

```python
if __name__ == "__main__":
    # https://en.wikipedia.org/wiki/Say_cheese

    # `cp cheese.py ~` + `python cheese.py`
    # Use Rectangle (https://rectangleapp.com/)
    # to scale the terminal window to "Top Center Sixth"

    print("✨ 📸 ✨")
```

### `terminals/script.py` file

```python
import os
import platform
from datetime import datetime, timezone
from pathlib import Path

from pytablewriter import MarkdownTableWriter
from pytablewriter.typehint import String
from rapidjson import DM_ISO8601, WM_PRETTY, dump, load

DEFAULT_CELL_VALUE: str = "-"
TERM_VAR: str = "TERM"
TERM_PROGRAM_VAR: str = "TERM_PROGRAM"
TERM_PROGRAM_VERSION_VAR: str = "TERM_PROGRAM_VERSION"


def link(text: str, url: str) -> str:
    # More info: https://commonmark.org/help/
    return f"[{text}]({url})"


if __name__ == "__main__":
    term = os.getenv(TERM_VAR, DEFAULT_CELL_VALUE)
    term_program = os.getenv(TERM_PROGRAM_VAR, DEFAULT_CELL_VALUE)
    term_program_version = os.getenv(TERM_PROGRAM_VERSION_VAR, DEFAULT_CELL_VALUE)
    # More info: https://docs.python.org/3.8/library/platform.html#platform.platform
    my_os = platform.platform(terse=True)

    # More info:
    # - https://pytablewriter.readthedocs.io/en/latest/pages/reference/writers/text/markup/md.html
    # - https://pytablewriter.readthedocs.io/en/latest/pages/examples/table_format/text/markdown.html#example-markdown-table-writer
    # - https://pytablewriter.readthedocs.io/en/latest/pages/examples/typehint/python.html#example-type-hint-python
    # - https://pytablewriter.readthedocs.io/en/latest/pages/examples/output/dump/index.html
    writer = MarkdownTableWriter(
        headers=[
            "Terminal",
            TERM_VAR,
            TERM_PROGRAM_VAR,
            TERM_PROGRAM_VERSION_VAR,
            "OS",
        ],
        value_matrix=[["[]()", term, term_program, term_program_version, my_os]],
        type_hints=[String, String, String, String, String],
        margin=1,
        flavor="github",
    )

    # print(dir(writer))
    # print(writer._MarkdownTableWriter__flavor)

    # writer.write_table()
    output: str = writer.dumps()
    print(output)

    # https://python-rapidjson.readthedocs.io/en/latest/quickstart.html
    # https://python-rapidjson.readthedocs.io/en/latest/dump.html
    # https://python-rapidjson.readthedocs.io/en/latest/load.html
    # https://python-rapidjson.readthedocs.io/en/latest/api.html
    # https://realpython.com/python-json/
    datum = {
        "terminal": "",
        TERM_VAR: term,
        TERM_PROGRAM_VAR: term_program,
        TERM_PROGRAM_VERSION_VAR: term_program_version,
        "os": my_os,
        "timestamp": datetime.now(timezone.utc),
    }

    with open(Path("./data.json"), "r") as fp:
        data = load(fp, datetime_mode=DM_ISO8601)
        # print(data, type(data))

    with open(Path("./data.json"), "w") as fp:
        dump(
            data + [datum],
            fp,
            ensure_ascii=False,
            write_mode=WM_PRETTY,
            indent=2,
            sort_keys=False,
            datetime_mode=DM_ISO8601,
        )
```

### `terminals/Pipfile`

```toml
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
pytablewriter = "*"
python-rapidjson = "*"

[dev-packages]

[requires]
python_version = "3.8"
```

```markdown
## Development

- `pipenv install --python 3.8`.
- `pipenv shell`.
- Run this script via the desired terminal: `python script.py`.
- `python cheese.py`.
```
