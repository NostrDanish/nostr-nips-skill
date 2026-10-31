---
name: nostr-nips
description: "Fetch the current Nostr NIP markdown before implementing protocol behavior. Use when a task names a NIP, needs the spec for an event kind, or must know whether a NIP is still active. Triggers on NIP numbers and 'what does the spec say'. Do not use for signing, keys, or relay I/O (nostr skill) or the nak CLI (nak skill)."
license: CC-BY-SA-4.0
---

# Nostr NIPs (live spec)

This skill fetches the spec. It does not replace it with memory. The NIP number is not the event kind number.

## Fetch raw markdown

GitHub blob pages are HTML. Fetch the raw file:

```
https://raw.githubusercontent.com/nostr-protocol/nips/master/<FILE>.md
```

- Numeric NIPs are zero-padded to two digits: NIP-01 is `01.md`, NIP-19 is `19.md`.
- Letter NIPs keep their id: `B7.md`, `C7.md`.
- The index, event-kind table, tag table, and status column are in `README.md` at that same raw prefix.

If the file 404s, fetch the raw README and search it. The NIP may have been renamed, folded into another NIP, or rejected. Say that the fetch failed rather than inventing requirements.

## Which file

| Need | Fetch |
|---|---|
| A named NIP | `master/<FILE>.md` as above |
| Which NIP defines kind N | Raw `README.md`, Event Kinds table. Then fetch that NIP. |
| Is this tag standard? | Raw `README.md` tag table, then the NIP it cites |
| Is this NIP deprecated? | README status for that row. If the README and a cached note disagree, the README wins |

## After the spec is in hand

Implement with the `nostr` skill (libraries, signing, outbox, deprecated-NIP list). Use `nak` only when the task is the CLI. Do not publish, sign, or choose a relay from this skill alone.
