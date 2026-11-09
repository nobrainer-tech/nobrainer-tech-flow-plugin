# Native plugin distribution

The canonical source is https://github.com/nobrainer-tech/nobrainer-tech-flow . This repository contains the generated release files that the Claude plugin directory tracks. ChatGPT and Codex use the canonical release ZIP and the canonical repository's marketplace.

- Use the latest reviewed stable nobrainer-tech-flow and preserve the selected MAIN model and effort.
- Do not edit skills or references here. Change the canonical source, verify it, rebuild its plugin ZIP, then export the reviewed release with the canonical `scripts/export_native.py`.
- Keep SOURCE.json bound to the exact canonical tag and commit. The active portfolio stays exactly eighteen skills. Every skill file of an allowed type is kept, byte-identical to the canonical release; the canonical `scripts/verify_native_export.py` checks this in CI.
- Ship only Markdown, plain text, JSON, YAML and PNG, JPEG, GIF, WebP or ICO images: no script or program anywhere (none under `skills/*/scripts/`, `scripts/` or `_maintainers/`), no file that starts with `#!`, no package-manager file. The Claude directory accepts anything else only from Verified organizations.
- Keep the native package free of top-level bin/, npm package/lock files, lifecycle hooks, MCP declarations, test/evaluation archives and app mappings. From docs/ ship only CHAT_PLUGINS.md and PRIVACY.md; installation guides and release records stay in the canonical repository, where the README links them. Keep only the Claude manifest: no root portable manifest, no .codex-plugin folder and no assets folder. Keep the approved brand icon in the .claude-plugin folder, with no `icon` manifest field, and the supported presentation metadata.
- Use a focused branch and PR for updates; scan public content for secrets and validate artifacts/client surfaces. Publication and directory approval need their own readback.
- Preserve unrelated work. Clean up only owned temporary fixtures after verification.
