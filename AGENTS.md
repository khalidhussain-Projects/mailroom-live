# AGENTS.md — mailroom-live

## What this project is

A learning project. The code in this repo is being built incrementally while
learning programming fundamentals from the Panaversity "Agent Factory"
curriculum, Chapter 13 — Programming Fundamentals in the AI Era:
https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/

The eventual subject matter is a "mailroom" (processing/sorting mail), but
right now the project is mainly a vehicle for practicing programming
fundamentals in Python, one concept at a time.

## Current concept level — IMPORTANT, read before writing any code

The learner has completed lessons **13.1 through 13.7**, plus **reading
files** (13.8) and **reading `sys.argv` command-line arguments** (introduced
ad hoc to build the `subscribers` command — not a numbered lesson in the
course, but taught in plain terms before use). Any code written in this
repo, by a human or an AI assistant, **must only use concepts covered
through this point**:

Allowed so far:
- Values, types, and variables (13.3)
- `if` / `elif` / `else`, `and` / `or`, truthy/falsy empty values (13.4, 13.5)
- `while` loops and `for` loops (13.4, 13.5)
- Functions: defining them, parameters, return values, reading a function
  signature as a "contract" (13.6)
- Lists and dictionaries: creation, indexing, lookups, missing keys, sorting
  (13.7)
- Reading files: `open()`, `.read()` (13.8)
- Command-line arguments: `import sys`, `sys.argv` as a list of the words
  typed after the program name

Explicitly **not yet covered — do not use until the learner has done the
corresponding lesson**:
- Writing files (13.8 covers reading; writing hasn't been taught yet)
- Working with dates (13.9)
- try/except error handling (not yet covered — 13.10 is about *reading*
  errors/tracebacks, not handling them)
- Classes / OOP (not covered anywhere in Chapter 13)
- Third-party packages / imports beyond the Python standard library basics
  already implied by the lessons above

As the learner progresses through later lessons, update this section to
reflect the new ceiling.

## How to teach / how to work on this project

- **Teach-first rule:** if a task requires a concept not yet covered above,
  explain that concept first, in plain terms, before writing or showing code
  that uses it. Don't silently introduce new syntax.
- **Method: PRIMM-AI** (Predict → Run → Investigate → Modify → Make, with AI
  assistance). For any new or non-trivial piece of code:
  1. **Predict** — ask what the learner thinks will happen before running it.
  2. **Run** — actually run it.
  3. **Investigate** — look at the real output together and explain it.
  4. **Modify** — make a small, deliberate change to deepen understanding.
  5. **Make** — have the learner build something new using the concept.
- Do **not** connect to or use the AgentFactory MCP connector for this
  project — the learner has explicitly opted out of it for this work.
- Keep code simple and readable over clever. No premature abstractions,
  no classes, no error handling beyond what's been taught.

## Tooling

- **Package/project manager:** [uv](https://docs.astral.sh/uv/). Do not use
  bare `pip` or `venv` directly — use `uv` commands instead:
  - `uv run main.py` — run the program (creates/uses `.venv` automatically)
  - `uv add <package>` — add a dependency
  - `uv sync` — install dependencies from the lock file
- **Python version:** 3.14 (latest stable at project creation), pinned in
  `.python-version` and `pyproject.toml` (`requires-python = ">=3.14"`).
- **Entry point:** `main.py`, with a `main()` function guarded by
  `if __name__ == "__main__":`.

## Project structure

The project root **is** this `mailroom` folder (not a nested subfolder) —
`.git` and the uv project both live here directly:

```
mailroom/                (a.k.a. mailroom-live project root)
├── main.py            # entry point; imports from mailroom.py
├── mailroom.py         # subscriber-counting functions (read_subscribers, count_emails, count_group)
├── check.py            # standalone tests for the subscriber-counting logic
├── pyproject.toml      # project metadata + dependencies (managed by uv)
├── uv.lock             # exact locked dependency versions (do not hand-edit)
├── .python-version     # pins the Python version for uv
├── .gitignore
├── README.md
└── AGENTS.md           # this file
```

## Git / GitHub

- Repo is public on GitHub under the `khalidhussain-Projects` account,
  pushed via the `gh` CLI.
- Commit normally as work progresses; no special branching strategy yet
  (solo learning project, work directly on `main` unless told otherwise).
