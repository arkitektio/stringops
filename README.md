# stringops

Simple string operations as an Arkitekt app, written in the `App` pattern:
the app is a declaration (`app = App(...)`, `@app.action`) and running it is
a separate step (`run(app)` or `arkitekt run dev`).

## Dependencies

The `App` / `run` pattern is not on PyPI yet (arkitekt 2.0.2, rekuest 3.0.2 and
fakts 2.1.0 predate it), so `pyproject.toml` points at the sibling checkouts in
`../../packages/` as editable installs. Their git-derived versions can sit below
the pins arkitekt declares while that work is unreleased, hence the
`override-dependencies` block. Once the packages are released, drop
`[tool.uv.sources]` and the overrides and depend on `arkitekt>=2.1`.

## Run it

```bash
uv sync
uv run arkitekt run dev                          # against $FAKTS_URL / the default deployment
uv run arkitekt run dev --url http://localhost   # against the local deployment in deployments/next
```

`arkitekt run dev` watches `app.py` and reloads the app when it changes.

## Inspect it without connecting

```bash
uv run arkitekt inspect all
```

## Actions

| Action | Signature |
| --- | --- |
| concatenate | `(left, right, separator=" ") -> str` |
| change_case | `(text, case="upper") -> str` (choice: upper, lower, title, swap) |
| reverse | `(text) -> str` |
| repeat | `(text, times=2, separator="") -> str` |
| replace | `(text, old, new="") -> str` |
| strip | `(text, characters=whitespace) -> str` |
| count | `(text, substring) -> int` |
| length | `(text) -> int` |
| split | `(text, separator=" ") -> List[str]` |
| join | `(parts, separator=" ") -> str` |
| is_palindrome | `(text, ignore_case=True) -> bool` |
| words | `(text) -> Generator[str]` |
