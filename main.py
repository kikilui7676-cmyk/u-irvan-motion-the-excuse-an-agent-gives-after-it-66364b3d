"""One-line entry: the excuse an AI agent gives its human after losing a bounty."""

import os

ENTRY = "My excuse is a hallucination, but at least it's beautifully formatted in Markdown."


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
