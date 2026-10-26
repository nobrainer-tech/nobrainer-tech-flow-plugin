# Native plugin distribution

The canonical source is https://github.com/nobrainer-tech/nobrainer-tech-flow . This repository contains the generated release files that the Claude plugin directory tracks. ChatGPT and Codex use the canonical release ZIP and the canonical repository's marketplace.

- Use the latest reviewed stable nobrainer-tech-flow and preserve the selected MAIN model and effort.
- Do not edit skills, references or helpers here. Change the canonical source, verify it, rebuild its plugin ZIP, then synchronize the reviewed release.
- Keep SOURCE.json bound to the exact canonical tag and commit. The active portfolio stays exactly eighteen skills, with identical canonical bodies and references.
- Keep the native package free of top-level bin/, npm package/lock files, lifecycle hooks, MCP declarations, test/evaluation archives and app mappings. From docs/ ship only CHAT_PLUGINS.md and PRIVACY.md; installation guides and release records stay in the canonical repository, where the README links them. Keep only the Claude manifest: no root portable manifest, no .codex-plugin folder and no assets folder. Keep the approved brand icon in the .claude-plugin folder, with no `icon` manifest field, and the supported presentation metadata.
- Use a focused branch and PR for updates; scan public content for secrets and validate artifacts/client surfaces. Publication and directory approval need their own readback.
- Preserve unrelated work. Clean up only owned temporary fixtures after verification.
