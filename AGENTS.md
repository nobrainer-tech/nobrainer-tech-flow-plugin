# Native plugin distribution

The canonical source is https://github.com/nobrainer-tech/nobrainer-tech-flow . This repository contains generated release files for native ChatGPT/Codex and Claude plugins.

- Use the latest reviewed stable nobrainer-tech-flow and preserve the selected MAIN model and effort.
- Do not edit skills, references or helpers here. Change the canonical source, verify it, rebuild its plugin ZIP, then synchronize the reviewed release.
- Keep SOURCE.json bound to the exact canonical tag and commit. The active portfolio stays exactly eighteen skills, with identical canonical bodies and references.
- Keep the native package free of top-level bin/, npm package/lock files, lifecycle hooks, MCP declarations, test/evaluation archives and app mappings. From docs/ ship only CHAT_PLUGINS.md and PRIVACY.md; installation guides and release records stay in the canonical repository, where the README links them. Preserve the approved 512px brand icon (assets/plugin-logo.png, copied byte for byte to .claude-plugin/icon.png for the Claude directory, with no `icon` manifest field) and supported presentation metadata.
- Use a focused branch and PR for updates; scan public content for secrets and validate artifacts/client surfaces. Publication and directory approval need their own readback.
- Preserve unrelated work. Clean up only owned temporary fixtures after verification.
