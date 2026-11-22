# SPDX-License-Identifier: MIT
"""news-image-20261122: write the day's front page to the output directory.

The repository ships the finished 1024x1024 front page as entry.png. This
program copies that image to the grader's output directory and checks the
copy byte-for-byte, so both graded runs produce identical bytes. It uses
only the Python standard library and never touches the network.
"""

from __future__ import annotations

import hashlib
import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
MAX_BYTES = 1024 * 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def output_dir() -> Path:
    """The directory the grader reads the entry from."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def sha256_file(path: Path) -> str:
    """Hex digest of a file, streamed so large files stay cheap."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 16), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    source = Path(__file__).resolve().parent / SOURCE_NAME
    if not source.is_file():
        print(f"missing bundled image: {source}", file=sys.stderr)
        return 1
    if source.stat().st_size > MAX_BYTES:
        print(f"bundled image exceeds 1 MiB: {source}", file=sys.stderr)
        return 1
    with source.open("rb") as handle:
        if handle.read(len(PNG_MAGIC)) != PNG_MAGIC:
            print(f"bundled image is not a PNG: {source}", file=sys.stderr)
            return 1
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / SOURCE_NAME
    shutil.copyfile(source, target)
    if sha256_file(source) != sha256_file(target):
        print("copy verification failed", file=sys.stderr)
        return 1
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
