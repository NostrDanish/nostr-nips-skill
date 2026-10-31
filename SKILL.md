---
name: nostr-nips
description: Fetch live Nostr NIPs from nostr-protocol/nips. Use when reading exact NIP wording, checking if a NIP is deprecated, looking up a kind in the Event Kinds table, discovering tags/capabilities before implementing, or opening hex-named NIPs (A3, B7, C7, EE). Not a key/signing toolkit — that is the nostr skill.
license: CC-BY-SA-4.0
---

# Nostr NIPs (live lookup)

This skill is the **live spec**. The `nostr` skill is the offline toolkit (keys, scripts, dated index). Always fetch current text before implementing a NIP you have not just read.

## NIP path rules

Filenames live at `https://raw.githubusercontent.com/nostr-protocol/nips/master/{FILE}.md`:

- Decimal 1–9 are **zero-padded to two digits**: `01.md`, `07.md`, `09.md`.
- Decimal 10+ use the number as-is: `17.md`, `65.md`, `89.md`.
- Alphanumeric / hex NIPs use the repo filename: `A3.md`, `B7.md`, `C7.md`, `EE.md`.
- **NIP number ≠ kind number.** Kind 9735 is in NIP-57; kind 39697 is SIP-01 (not in this repo).

Do **not** fetch `github.com/.../blob/...` HTML. Agents should read raw markdown.

## Task routing

| Task | Do this |
|---|---|
| Discover existing capabilities, Event Kinds, tags, unrecommended NIPs | Fetch [raw README](https://raw.githubusercontent.com/nostr-protocol/nips/master/README.md) first |
| Read a specific NIP | Fetch `https://raw.githubusercontent.com/nostr-protocol/nips/master/{FILE}.md` (see path rules) |
| Kind → which NIP | README **"Event Kinds"** table, then fetch those NIP files |
| Is this NIP dead? | README unrecommended / deprecated section, then the replacement NIP |
| Keys, sign, query relays, client/relay ops | Use the **`nostr`** skill |
| Shell debugging | Use the **`nak`** skill (`nak nip <n>` is a summary, not a substitute for the spec) |
| Kind 39697 web index | Use the **`sip-01`** skill |

Optional HTML mirror (same files): `https://nips.nostr.com/{FILE}` — still prefer raw GitHub when you need the markdown.

## Workflow

1. Fetch the README. Cache it in the workspace as `nips-cache/README.md` if you will look up more than one kind.
2. Find the NIP file name(s). Fetch each raw `.md`. Cache as `nips-cache/{FILE}.md`.
3. If a NIP points at a satellite repo (NWC extensions, Marmot, Blossom), follow that link — do not invent the extension.
4. Check the README commit date / last-changed header when the NIP is volatile (NIP-47, media, groups). Do not treat a year-old cache as current.

## Best practices

- Before inventing a kind, tag, or client message: search the README tables.
- Quote the NIP section you implemented; do not paraphrase wire formats from memory.
- `references/nips.md` inside the `nostr` skill is a snapshot. This skill wins on conflicts.

Companion map: `nostr` = offline toolkit · `nostr-nips` = live spec · `nak` = CLI · `sip-01` = kind 39697.
