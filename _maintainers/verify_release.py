#!/usr/bin/env python3
"""Verify this native export against its immutable public canonical release."""
import ast
import hashlib
import io
import json
from pathlib import Path
import re
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
source = json.loads((ROOT / "SOURCE.json").read_text())
assert source["canonical_repository"] == "https://github.com/nobrainer-tech/nobrainer-tech-flow"
assert re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+", source["tag"])
assert re.fullmatch(r"[0-9a-f]{40}", source["commit"])
api = "https://api.github.com/repos/nobrainer-tech/nobrainer-tech-flow/git/"
with urllib.request.urlopen(api + "ref/tags/" + source["tag"], timeout=30) as response:
    ref = json.load(response)["object"]
if ref["type"] == "tag":
    with urllib.request.urlopen(api + "tags/" + ref["sha"], timeout=30) as response:
        ref = json.load(response)["object"]
assert ref["type"] == "commit" and ref["sha"] == source["commit"], "Canonical tag/commit binding differs."
url = source["canonical_repository"] + "/releases/download/" + source["tag"] + "/nobrainer-tech-flow-" + source["tag"][1:] + "-plugin.zip"
with urllib.request.urlopen(url, timeout=30) as response:
    payload = response.read()
assert hashlib.sha256(payload).hexdigest() == source["plugin_zip_sha256"]
with zipfile.ZipFile(io.BytesIO(payload)) as archive:
    canonical = {name: archive.read(name) for name in archive.namelist() if name.startswith("skills/") and not name.endswith("/")}
    exported = {path.relative_to(ROOT).as_posix(): path.read_bytes() for path in (ROOT / "skills").rglob("*") if path.is_file()}
    assert canonical == exported, "Every skill body, reference and helper must match the reviewed ZIP."
    for name in ("install_skills.py", "install_personalization.py"):
        assert (ROOT / "scripts" / name).read_bytes() == archive.read("scripts/" + name)
skills = list((ROOT / "skills").glob("*/SKILL.md"))
assert len(skills) == 18
assert not any((ROOT / name).exists() for name in ("bin", "package.json", "package-lock.json", "hooks", ".app.json", ".mcp.json"))
for path in ROOT.rglob("*"):
    if ".git" in path.parts:
        continue
    assert not path.is_symlink(), path
    assert path.suffix not in (".zip", ".tgz", ".tar", ".gz"), path
    if path.suffix == ".py":
        ast.parse(path.read_text(), filename=str(path))
for name in ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
    manifest = json.loads((ROOT / name).read_text())
    assert manifest["name"] == "nobrainer-tech-flow"
    assert manifest["version"] == source["tag"][1:]
    assert "hooks" not in manifest and "mcpServers" not in manifest
claude = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
assert (ROOT / claude["icon"].removeprefix("./")).is_file()
assert (ROOT / "skills/nobrainer-tech-flow/VERSION").read_text().strip() == source["tag"][1:]
print("NATIVE_DISTRIBUTION_VERIFIED: 18 canonical skills; all resource bytes match; metadata, syntax and native boundary pass.")
