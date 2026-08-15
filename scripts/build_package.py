#!/usr/bin/env python3
"""Validate and package the scoped SiYuan plugin."""

from __future__ import annotations

import hashlib
import json
import re
import struct
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
PACKAGE = DIST / "package.zip"
SOURCE_HASH = "d66237ba0ef1aadbd1d0fb5a07dc822ffe6915145e074d3b3ac63461e2c5674c"
REQUIRED = (
    "plugin.json", "index.js", "index.css", "icon.png", "preview.png",
    "README.md", "README.zh-CN.md", "CHANGELOG.md", "LICENSE",
    "assets/kami-work-notes.typora.css",
)


def png_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if len(data) != 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{path.name} is not a valid PNG")
    return struct.unpack(">II", data[16:24])


def validate() -> dict[str, object]:
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    if missing:
        raise FileNotFoundError(f"Missing required files: {', '.join(missing)}")
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    if manifest["name"] != ROOT.name:
        raise ValueError("plugin.json name must match the repository directory")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest["version"])):
        raise ValueError("plugin.json version must use semantic versioning")
    source_hash = hashlib.sha256((ROOT / "assets/kami-work-notes.typora.css").read_bytes()).hexdigest()
    if source_hash != SOURCE_HASH:
        raise ValueError("The preserved Typora Kami source CSS was modified")
    icon, preview = png_size(ROOT / "icon.png"), png_size(ROOT / "preview.png")
    if icon != (160, 160) or preview != (1024, 768):
        raise ValueError(f"Invalid image dimensions: icon={icon}, preview={preview}")
    css = (ROOT / "index.css").read_text(encoding="utf-8")
    for marker in ("ying-kami-markdown-enabled", "#ffffff", "NodeCodeBlock", "tbody tr:hover"):
        if marker not in css:
            raise ValueError(f"index.css missing marker: {marker}")
    return {"name": manifest["name"], "version": manifest["version"], "sourceSHA256": source_hash}


def build() -> None:
    result = validate()
    DIST.mkdir(exist_ok=True)
    if PACKAGE.exists():
        PACKAGE.unlink()
    with zipfile.ZipFile(PACKAGE, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name in REQUIRED:
            archive.write(ROOT / name, arcname=name)
    print(json.dumps({**result, "package": str(PACKAGE)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    build()
