# Verify the native distribution

Run `_maintainers/verify_release.py` from this repository. It checks canonical release provenance, every skill file, metadata, required paths, Python syntax and the native package boundary.

The full source suite belongs to the [immutable canonical v2.2.1 testing documentation](https://github.com/nobrainer-tech/nobrainer-tech-flow/blob/v2.2.1/docs/TESTING.md). This repository deliberately omits npm/client-adapter manifests, lifecycle hooks and evaluation archives; it is not a source-development checkout.

Separate generated-file validation, client import/enabling, a fresh-task run and public directory approval. Configuration and another agent's report alone do not prove runtime or publication.
