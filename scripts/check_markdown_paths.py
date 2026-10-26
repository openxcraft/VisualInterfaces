#!/usr/bin/env python3
"""Check repository-local paths mentioned in Markdown inline code spans."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = ROOT.rglob("*.md")
PATH_SUFFIXES = {
    ".md", ".json", ".html", ".css", ".js", ".mjs", ".cjs", ".ts", ".tsx",
    ".jsx", ".py", ".yml", ".yaml", ".toml", ".rs", ".txt", ".sh", ".svg",
    ".png", ".jpg", ".jpeg", ".webp", ".lock", ".sql", ".xml",
}
INLINE_CODE = re.compile(r"(?<!`)`([^`]+)`(?!`)")

def without_fenced_code(text: str) -> str:
    """Remove fenced code blocks so examples are not treated as path references."""
    kept = []
    fence_char = None
    fence_length = 0
    for line in text.splitlines():
        stripped = line.lstrip()
        marker = stripped[:1]
        if marker in ("`", "~") and len(stripped) >= 3 and stripped.startswith(marker * 3):
            run_length = len(stripped) - len(stripped.lstrip(marker))
            if fence_char is None:
                fence_char, fence_length = marker, run_length
            elif marker == fence_char and run_length >= fence_length:
                fence_char, fence_length = None, 0
            continue
        if fence_char is None:
            kept.append(line)
    return "\n".join(kept)

def is_path_reference(value: str) -> bool:
    value = value.strip()
    if not value or any(char in value for char in "<>{}*"):
        return False
    if "://" in value or value.startswith(("#", "mailto:", "tel:")):
        return False
    if value.endswith("/"):
        return True
    return Path(value.split("#", 1)[0]).suffix.lower() in PATH_SUFFIXES

def resolve_reference(markdown_file: Path, reference: str) -> Path:
    if reference.startswith("/"):
        return (ROOT / reference.lstrip("/")).resolve()
    # Paths containing directories are documented from the repository root;
    # simple filenames and explicit ./ or ../ paths are relative to the document.
    if "/" in reference and not reference.startswith(("./", "../")):
        return (ROOT / reference).resolve()
    return (markdown_file.parent / reference).resolve()

def main() -> int:
    failures = []
    markdown_files = sorted(
        path for path in MARKDOWN
        if path.relative_to(ROOT).as_posix() != "roadmap.md"
        and not any(part in {".git", "node_modules", ".venv", "target"} for part in path.parts)
    )
    # The roadmap intentionally lists future files, so it is not a current-path gate.
    for markdown_file in markdown_files:
        text = without_fenced_code(markdown_file.read_text(encoding="utf-8"))
        for match in INLINE_CODE.finditer(text):
            reference = match.group(1).strip()
            if not is_path_reference(reference):
                continue
            reference = reference.split("#", 1)[0]
            if not reference:
                continue
            target = resolve_reference(markdown_file, reference)
            try:
                target.relative_to(ROOT)
            except ValueError:
                failures.append(f"{markdown_file.relative_to(ROOT)}: path escapes repository: {reference}")
                continue
            if not target.exists():
                failures.append(f"{markdown_file.relative_to(ROOT)}: missing path reference: {reference}")

    if failures:
        print("\n".join(failures), file=sys.stderr)
        print(f"Found {len(failures)} broken Markdown path reference(s).", file=sys.stderr)
        return 1
    print(f"Checked {len(markdown_files)} Markdown files; all current local path references exist.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
