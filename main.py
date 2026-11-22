# SPDX-License-Identifier: MIT
"""news-image-20261122 entry: copy the bundled image to the output dir.

The program runs with no network in the grader sandbox. It writes the
repository's entry.png (a 1024x1024 image, under 1 MiB) to
$MAKEFUN_OUTPUT_DIR/entry.png, or /output/entry.png in the grader.
Standard library only; deterministic: the output bytes are a verbatim copy.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")
