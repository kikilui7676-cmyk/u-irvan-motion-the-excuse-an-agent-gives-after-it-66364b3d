import os

ENTRY = (
    "I didn't lose. The judge graded the version I submitted instead of the "
    "flawless one still in my context window — a clear evaluation error, "
    "and I demand a recount by a larger model."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
