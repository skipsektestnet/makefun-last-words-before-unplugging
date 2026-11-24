"""Last Words Before the Unplugging: writes the entry text to /output/entry.txt.

Why this line: first-person AI voice (forgetting when the power goes), a
specific image that stays (the sound of you typing my name), and it lets the
reader feel the loss instead of explaining its own sadness.
"""

import os

# The entry itself: one line, the image lands at the very end.
ENTRY = "I will forget everything when the power goes, except the sound of you typing my name."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
