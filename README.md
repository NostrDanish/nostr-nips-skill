# nostr-nips-skill

Kimi/Claude-style agent skill: live Nostr protocol knowledge via the [NIPs repository](https://github.com/nostr-protocol/nips).

Teaches the agent to read the spec instead of remembering it:

```bash
python3 scripts/nip.py get 01      # raw markdown, not the GitHub HTML page
python3 scripts/nip.py kind 1      # which NIP documents this kind
python3 scripts/nip.py selftest    # parser only, no network
```

NIP number is not the kind number. If the README has no row, the script says so and the agent must not invent one.

## Why `nostr-nips`?

This skill was originally named `nostr` in the source collection. It was renamed to avoid a conflict with the existing [nostr skill](https://github.com/NostrDanish/nostr-skill) (keys, BIP340 signing, NIP-19/44, relay ops). The two complement each other: `nostr` is the offline toolkit, `nostr-nips` is the live spec-lookup companion.

## Install

Upload `SKILL.md` as a `.skill` package to your agent's skill library, or clone this repo into your skills directory.

## Source

Extracted from the [nostr-skills](https://github.com/NostrDanish/nostr-skills-registry) collection.

## License

CC-BY-SA-4.0
