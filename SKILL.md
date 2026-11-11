---
name: nostr-nips
description: Research current Nostr Implementation Possibilities (NIPs) from the canonical upstream repository. Use when asked what a NIP currently specifies, whether a NIP is draft/final/unrecommended, which NIP defines an event kind or tag, or whether an existing NIP covers a proposed feature. Do not use as the primary implementation or relay-operations guide; use the nostr skill for implementation work.
---

# Nostr NIPs — source-first specification research

## Activation and non-activation

Use this skill for current NIP text, status, event-kind ownership, standardized tags, protocol capability discovery and standards-gap research.

Do not rely on this skill's cached knowledge for a current status question. Do not treat an open pull request, discussion or implementation convention as an accepted entry in the canonical NIPs repository. For implementation and operations, hand off to the nostr skill after the relevant requirements have been verified.

## Canonical source

The authoritative public repository is https://github.com/nostr-protocol/nips

Start every current research task by fetching:
1. The repository README, especially the NIP list, event-kinds table, message types and status markers.
2. The individual NIP file(s) relevant to the question.
3. The commit SHA and commit date for the branch or revision actually read.

Useful sources:
- README: https://github.com/nostr-protocol/nips/blob/master/README.md
- NIP files: https://github.com/nostr-protocol/nips/blob/master/{NIP}.md
- Commit history: https://github.com/nostr-protocol/nips/commits/master/

The source revision used when this skill was updated was b587c619c2ea662d40b40976aeccf6ac8d6ba9eb (2026-11-07). This is provenance for this update only, not a claim that the branch will remain unchanged.

## Research procedure

1. Resolve the NIP number or feature against the current README. Remember that NIP number and event kind are different namespaces.
2. Open the individual NIP from the same repository revision. Read the full relevant normative section and its metadata/status labels.
3. Record the commit SHA and commit timestamp. If a page is fetched through a browser or API that follows a moving branch, identify the commit that was current when fetched.
4. Classify the specification exactly as upstream does: draft, final, optional, unrecommended, deprecated/replaced, or absent from the accepted list. Several labels can apply simultaneously.
5. If the NIP is struck through or marked unrecommended, read the reason and stated replacement. Do not describe it as nonexistent; implementations may still need legacy compatibility.
6. Check whether the feature is defined by the NIP itself, merely mentioned in an example, or left to implementation policy.
7. Identify normative language (MUST/SHOULD/MAY) and preserve its strength. Do not upgrade recommendations to requirements.
8. Compare any related implementation or PR only as secondary evidence. State clearly when behavior is implementation-specific or experimental.
9. For conflicting sources, present the conflict and its revisions; do not silently choose the newest blog post or infer consensus.
10. Return a concise finding with source links and retrieval provenance.

## Status and wording rules

- A NIP number does not imply acceptance, maturity or mandatory support.
- “Final” describes the repository's status marker; it does not mean every client or relay implements it.
- “Unrecommended” is an upstream warning. Explain the reason and replacement when the README provides one.
- “Draft” means the proposal can change. Do not present it as a stable universally deployed requirement.
- “Not listed” is not proof that no implementation exists or that no PR/discussion exists.
- “Deprecated/replaced” is more precise than calling a specification “dead”. Explain the compatibility implications.
- Nostr software implements subsets of the NIPs relevant to its use case; never imply that every NIP is mandatory.

## Event kinds and tags

Use the README's event-kinds table first, then read the referenced NIP. Never infer an event kind from the NIP number. Check current tag conventions and whether a tag is standard, optional, application-specific or merely used by an example.

## Report format

For each relevant NIP, report:
- NIP number and title
- upstream status labels
- source revision and retrieval date
- normative requirements relevant to the question
- explicit limitations, deprecation notices or replacements
- implementation-specific caveats
- links to README and the individual NIP

## Handoff

Once the specification has been checked, pass implementation tasks to the nostr skill with the verified source revision and the exact relevant normative clauses. Never invent protocol behavior or new event kinds/tags from an implementation's local conventions.
