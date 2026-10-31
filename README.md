# nostr-nips-skill

Kimi/Claude-style agent skill: live Nostr protocol knowledge via the [NIPs repository](https://github.com/nostr-protocol/nips).

Teaches the agent to:

- Fetch raw NIP markdown (`https://raw.githubusercontent.com/nostr-protocol/nips/master/01.md`), not the GitHub HTML page
- Zero-pad numeric NIP filenames (`01.md`) and keep letter ids (`B7.md`)
- Use the raw README Event Kinds table to find which NIP documents a given kind (NIP number ≠ kind number)
- Stop and say so when a fetch 404s, instead of inventing spec text

## Why `nostr-nips`?

This skill was originally named `nostr` in the source collection. It was renamed to avoid a conflict with the existing [nostr skill](https://github.com/NostrDanish/nostr-skill) (keys, BIP340 signing, NIP-19/44, relay ops). The two complement each other: `nostr` is the offline toolkit, `nostr-nips` is the live spec-lookup companion.

## Install

Upload `SKILL.md` as a `.skill` package to your agent's skill library, or clone this repo into your skills directory.

## Source

Extracted from the [nostr-skills](https://github.com/NostrDanish/nostr-skills-registry) collection.

## License

CC-BY-SA-4.0
