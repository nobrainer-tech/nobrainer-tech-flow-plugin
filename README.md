# nobrainer-tech-flow plugin

> **The project lives at [nobrainer-tech/nobrainer-tech-flow](https://github.com/nobrainer-tech/nobrainer-tech-flow).** Star it, report issues and read the docs there. This repository is the script-free plugin build that the Claude plugin directory installs.

From task to done. Bring the same eighteen workflow modules into your assistant for research, writing, planning and implementation.

This repository distributes the native plugin generated from the reviewed [canonical nobrainer-tech-flow release](https://github.com/nobrainer-tech/nobrainer-tech-flow/releases/tag/v2.12.0). The skill bodies and references come from that source; SOURCE.json records its immutable version and commit. Keep code changes in the canonical repository.

## Install

In Claude, [download the release plugin ZIP](https://github.com/nobrainer-tech/nobrainer-tech-flow-plugin/releases/latest), then open Customize > Plugins > Add > Upload plugin. Enable it and start a fresh conversation with “Use nobrainer-tech-flow.” Available tools, permissions and account limits depend on the client.

In Claude Code, add this repository as a marketplace and install from it: `/plugin marketplace add nobrainer-tech/nobrainer-tech-flow-plugin`, then `/plugin install nobrainer-tech-flow@nobrainer-tech`.

ChatGPT and Codex install from the canonical repository's marketplace or the canonical release ZIP; this copy carries only the Claude manifest. Public directory approval is separate from source publication. See [supported setup paths](docs/CHAT_PLUGINS.md).

This copy holds only Markdown, plain text, JSON, YAML and the brand icon, because the Claude directory accepts scripts and programs only from organizations it has verified. It leaves out every script under `skills/*/scripts/`, the command-line launchers, lifecycle hooks and evaluation archives. Where a skill names a bundled script, the agent does the same check by hand or with a host tool and says so. Git and npm installs from the canonical repository include the scripts: see the [canonical installation guide](https://github.com/nobrainer-tech/nobrainer-tech-flow/blob/v2.12.0/docs/INSTALL.md).

## Maintain the distribution

Export a reviewed stable release with `scripts/export_native.py` in the canonical repository: it takes the release's plugin ZIP, its tag and commit, and a clean checkout of this repository, writes the copy and checks it with `scripts/verify_native_export.py`. The check allows only the file types above, refuses any file that starts with `#!` and any package-manager file, and requires every skill file this copy keeps to be byte-identical to the release ZIP. This repository's CI runs the same verifier from the canonical tag that SOURCE.json names. Review the diff, publish through a PR, and read back the target clients and the directory status.

## Requests and credentials

This copy ships no code: it makes no network request and reads no credential or environment variable. The agent works with the host client's own tools and permissions, and this package grants none. Supply secrets through the client's supported sensitive configuration; never place them in a prompt, this repository or public logs.

MIT. The AI client's own access and usage costs apply. [Privacy](https://github.com/nobrainer-tech/nobrainer-tech-flow-plugin/blob/main/docs/PRIVACY.md).

## Three reviewer examples

- Planning: “Use nobrainer-tech-flow. Give three observable acceptance checks for a static product page with mobile navigation, readable copy and a contact link.” Expect a bounded checklist; no claim that a page was actually tested.
- Writing: “Use nobrainer-tech-flow. Rewrite this sentence clearly without adding facts: the plugin provides eighteen modules for research, writing, planning and implementation.” Expect all four purposes and the number preserved.
- Research: “Use nobrainer-tech-flow. Compare OpenAI and Claude's official native-plugin packaging requirements, cite the current primary sources and list what depends on the client.” Expect supported sources and explicit uncertainty; browser availability depends on the host.

Use public sample inputs in the AI client's own test account. The package requires no NoBrainer service account. These prompts describe checks reviewers can run; they do not establish universal runtime quality.
