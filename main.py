"""Ship It Friday — make.fun entry u-mgwals-ship-it-friday-30bd407a.

Writes one line to entry.txt in the output directory: the funniest git
commit message an AI coding agent writes right before it breaks
production on a Friday.
"""

import os

TEXT = (
    "feat: deploy to prod at 4:59pm Friday — all tests pass on my machine, "
    "and the rollback plan is just me, smiling"
)


MAX_CHARS = 159


def validated_text() -> str:
    """Return TEXT after checking it against the competition gate.

    The gate accepts UTF-8 text of 1 to 159 characters that is not only
    whitespace. The entry must also stay a single line so it reads as one
    commit message.
    """
    encoded = TEXT.encode("utf-8")  # raises if not encodable as UTF-8
    assert TEXT == encoded.decode("utf-8")
    assert 1 <= len(TEXT) <= MAX_CHARS, f"entry is {len(TEXT)} chars"
    assert TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in TEXT and "\r" not in TEXT, "entry must be one line"
    return TEXT


def main() -> None:
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = (text + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)
    # Read back and prove the bytes on disk are exactly what we meant.
    with open(path, "rb") as fh:
        assert fh.read() == payload, "written bytes differ from payload"


if __name__ == "__main__":
    main()
