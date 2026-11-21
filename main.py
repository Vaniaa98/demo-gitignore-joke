"""The joke about the demo.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. No network, no input, deterministic.
"""

import os

JOKE = (
    "My coding agent fixed the demo by adding it to .gitignore. "
    "It works on every machine now, because none of them has it."
)


def main():
    text = JOKE
    # The entry must be 1-280 Unicode code points of UTF-8 text.
    # Verified: this joke is 118 code points, one line, no trailing newline.
    assert 1 <= len(text) <= 280, f"entry is {len(text)} code points"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
