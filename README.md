# nostr-nips-skill

Kimi/Claude-style agent skill: live Nostr protocol knowledge via the [NIPs repository](https://github.com/nostr-protocol/nips).

Teaches the agent to:

- Fetch **raw** NIP markdown (`https://raw.githubusercontent.com/nostr-protocol/nips/master/{FILE}.md`) — not GitHub blob HTML
- Apply filename rules: `01.md`–`09.md` zero-padded; hex NIPs (`A3`, `B7`, `C7`, `EE`) as in the repo
- Use the NIPs README "Event Kinds" table to find which NIP documents a given kind (NIP number ≠ kind number)
- Discover existing capabilities before implementing — check standardized tags and existing NIPs first

## Why `nostr-nips`?

This skill was originally named `nostr` in the source collection. It was renamed to avoid a conflict with the existing [nostr skill](https://github.com/NostrDanish/nostr-skill) (keys, BIP340 signing, NIP-19/44, relay ops). The two complement each other: `nostr` is the offline toolkit, `nostr-nips` is the live spec-lookup companion.

## Install

Upload `SKILL.md` as a `.skill` package to your agent's skill library, or clone this repo into your skills directory.

## Source

Extracted from the [nostr-skills](https://github.com/NostrDanish/nostr-skills-registry) collection.

## License

CC-BY-SA-4.0
