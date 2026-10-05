# nobrainer-tech-flow plugin

From task to done. Bring the same eighteen workflow modules into your assistant for research, writing, planning and implementation.

This repository distributes the native skills plugin generated from the reviewed [canonical nobrainer-tech-flow release](https://github.com/nobrainer-tech/nobrainer-tech-flow/releases/tag/v2.2.1). The skill bodies and references come from that source; SOURCE.json records its immutable version and commit. Keep code changes in the canonical repository.

## Install

In Claude, download the release plugin ZIP, then open Customize > Plugins > Add > Upload plugin. Enable it and start a fresh conversation with “Use nobrainer-tech-flow.” Available tools, permissions and account limits depend on the client.

ChatGPT/Codex use the portable plugin format through supported marketplaces or the public directory after approval. Public directory approval is separate from source publication. See [supported setup paths](docs/CHAT_PLUGINS.md).

For the coding-client npm installer, use the [canonical installation guide](https://github.com/nobrainer-tech/nobrainer-tech-flow/blob/v2.2.1/docs/INSTALL.md). This native distribution omits command-line launchers, lifecycle hooks and evaluation archives.

## Maintain the distribution

Generate the native plugin ZIP with scripts/build_plugin.py in the canonical repository at a reviewed stable tag. Extract it into this repository, preserve these distribution instructions and SOURCE.json, add the Claude displayName/icon presentation fields, and remove npm package.json. Compare all eighteen SKILL.md files and their references byte for byte against the source. Review the diff, publish through a PR, and read back the target clients and directory status.

## Optional requests and credentials

The workflow uses the host client's tools and permissions. Its release checker requests public release metadata from GitHub. Classification decisions are advisory and off by default: the TypeSafe adapter can make a request only when explicitly enabled on authorized data, and uses an existing TYPESAFE_API_KEY in the host environment. The offline Laya adapter requires an already configured local model and runtime; its first model setup can need a network download. The fallback remains available when an optional provider is unavailable.

Helpers for an authorized code task can use the host's existing GitHub CLI authentication or configured environment. This package grants no credentials or broader access. Supply secrets through the client's supported sensitive configuration; never place them in a prompt, this repository or public logs. Directory policy holds for this behavior remain subject to review.

MIT. The AI client's own access and usage costs apply. [Privacy](https://github.com/nobrainer-tech/nobrainer-tech-flow-plugin/blob/main/docs/PRIVACY.md).

## Three reviewer examples

- Planning: “Use nobrainer-tech-flow. Give three observable acceptance checks for a static product page with mobile navigation, readable copy and a contact link.” Expect a bounded checklist; no claim that a page was actually tested.
- Writing: “Use nobrainer-tech-flow. Rewrite this sentence clearly without adding facts: the plugin provides eighteen modules for research, writing, planning and implementation.” Expect all four purposes and the number preserved.
- Research: “Use nobrainer-tech-flow. Compare OpenAI and Claude's official native-plugin packaging requirements, cite the current primary sources and list what depends on the client.” Expect supported sources and explicit uncertainty; browser availability depends on the host.

Use public sample inputs in the AI client's own test account. The package requires no NoBrainer service account. These prompts describe checks reviewers can run; they do not establish universal runtime quality.
