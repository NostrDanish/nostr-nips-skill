---
name: nostr-nips
description: "Fetch the current Nostr NIP text and find which NIP defines an event kind. Use when implementing or reviewing a NIP number, checking whether a NIP is deprecated, or mapping a kind number to its spec. Triggers on NIP-01, NIP numbers, 'what kind is', and 'is this NIP still valid'. This is the live spec lookup. The nostr skill is the offline toolkit (keys, signing, relays)."
license: CC-BY-SA-4.0
---

# Nostr NIPs (live spec)

The NIPs repository is the spec. This skill's job is to make you read that spec instead of remembering it.

NIP number is not the kind number. Kind 1 is NIP-01 and NIP-10. Kind 0 is replaceable metadata, not "NIP-0".

## Do this

| Need | Command |
|---|---|
| The text of a NIP | `python3 scripts/nip.py get 01` (also `90`, `B7`, `A0`) |
| Which NIP documents kind `N` | `python3 scripts/nip.py kind N` |
| The index (kinds, tags, messages) | `python3 scripts/nip.py readme` |
| Parser still works, no network | `python3 scripts/nip.py selftest` |

Source of every fetch: `https://raw.githubusercontent.com/nostr-protocol/nips/master/`. `github.com/.../blob/...` pages are HTML. Do not implement from them.

If `kind` prints `NO ROW`, the kind is not in the README table. Say so. Do not invent a NIP, a tag layout, or a kind number to fill the gap.

## Rules

1. Quote behavior from the file you just fetched. A NIP's status line matters: `draft`, `mandatory`, `optional`, `unrecommended`. NIP-90 is unrecommended. NIP-04, NIP-08, NIP-15, NIP-26, NIP-28 and NIP-96 are not the current way to build that feature (see the `nostr` skill's deprecated list, then confirm in the fetched file).
2. When the README and the NIP disagree, the NIP file you fetched wins for that feature, and you say they disagree.
3. Kind ranges from NIP-01: regular = 1, 2, 4–44, and 1000–9999. Replaceable = 0, 3, and 10000–19999. Ephemeral = 20000–29999. Addressable = 30000–39999 and needs a `d` tag. Kind 2 and 41 are regular.
4. Filter values for `ids`, `authors`, `#e` and `#p` are exact 64-character lowercase hex. Relays index single-letter tags only.
5. After you know which NIP, implement with the `nostr` skill's libraries and scripts. Do not hand-roll Schnorr.

## When the README table is not enough

Some features are not a single kind row: Blossom is BUD documents (the `blossom` skill), NIP-90 job kinds live in `nostr-protocol/data-vending-machines` (the `nostr-dvm` skill). Fetch those repos the same way, raw markdown, and do not treat this skill's examples as the spec.
