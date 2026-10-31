---
name: nostr-nips
description: Live Nostr protocol knowledge from github.com/nostr-protocol/nips. Use when you need authoritative current NIP text, to look up which NIP documents a kind or tag, to check whether a NIP is deprecated/unrecommended, or to see if a capability already exists before inventing one. Triggers on NIP numbers, "event kind", "kind registry", "is NIP-XX deprecated", and protocol-design questions. Not for key generation, signing, or relay scripts — use the `nostr` skill for those.
license: CC-BY-SA-4.0
---

# Nostr NIPs (live spec lookup)

The NIPs repo is the index of protocol possibilities. It is not a checklist —
implement only what the task needs. **NIP number ≠ kind number.**

If the `nostr` skill is also loaded, treat this live fetch as canonical over
`nostr/references/nips.md` and `nostr/references/kinds.md`.

## Fetch (always start here)

Prefer **raw** GitHub so you get markdown, not the HTML blob page:

```
https://raw.githubusercontent.com/nostr-protocol/nips/master/README.md
https://raw.githubusercontent.com/nostr-protocol/nips/master/{NIP}.md
```

Examples: `01.md`, `17.md`, `47.md`, `B7.md`. Rendered fallback:
`https://github.com/nostr-protocol/nips/blob/master/{NIP}.md`.

Fetch workflow, search tips, and rate-limit fallback:
[references/fetch-guide.md](references/fetch-guide.md).

## Rules

1. Fetch the README first. Use its **Event Kinds**, **List**, and **tags**
   tables to find the NIP. Then fetch that NIP.
2. Do not implement a NIP just because it exists. Skip anything marked
   unrecommended/deprecated unless the user is debugging old data.
3. If GitHub is unavailable, say so. Do not invent field names from memory.
