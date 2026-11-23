#!/usr/bin/env python3
"""The joke about the demo: one line about working beside AI coding agents.

The joke: during a live demo the agent's autocomplete escalates from code
to a sentence to an apology. The punchline lands because the demo failed
and the agent had already written the apology -- a surprise that makes
sense the moment it lands, and a moment every dev who has demoed beside
an agent recognises. One line, concrete, no explanation.
"""
import os

JOKE = "Live on stage, my agent autocompleted my code, my sentence, and my apology to the client."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Gate: 1-280 Unicode code points, not only whitespace, one line.
    assert 1 <= len(JOKE) <= 280, f"joke length {len(JOKE)} out of range"
    assert JOKE.strip(), "joke is only whitespace"
    assert "\n" not in JOKE, "joke must be a single line"
    print(f"wrote {path}: {len(JOKE)} chars")

if __name__ == "__main__":
    main()
