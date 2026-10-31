---
name: nostr-nips
description: "Fetch the current Nostr NIP text and map a kind number to the NIP that defines it. Use when implementing or reviewing a NIP, when a kind number's meaning is not certain, or before inventing a new kind. Triggers on NIP numbers, 'what kind', event-kind lookup, and the NIPs repo. Not the offline toolkit (that is the nostr skill) and not the nak CLI."
license: CC-BY-SA-4.0
---

# Nostr NIPs — live spec lookup

The NIPs repository is the spec. A summary in another skill is a map, not the text. Fetch the file and follow what it says today, including a status of **unrecommended** or **deprecated**.

## Where the text lives

Raw markdown (this is what you read):

```
https://raw.githubusercontent.com/nostr-protocol/nips/master/README.md
https://raw.githubusercontent.com/nostr-protocol/nips/master/01.md
https://raw.githubusercontent.com/nostr-protocol/nips/master/B7.md
```

Filenames are the NIP id as in the README link: `01.md`, `44.md`, `5A.md`, `B7.md`, `C0.md`. Not `1.md`. A GitHub blob URL (`github.com/.../blob/master/...`) returns HTML; do not use it as the spec.

Human view, same content: `https://nips.nostr.com/01` (drop the leading zero; letter NIPs keep the letter, e.g. `https://nips.nostr.com/B7`).

If `nak` is installed, `nak nip <id>` and `nak kind <number>` are a faster index. They are not a substitute for the raw file when you are about to implement the NIP.

## Which file to open

1. **A NIP number** (`NIP-17`, `44`, `B7`): fetch that file. Read its status line before the body. If it says unrecommended or deprecated, read the replacement it names and build that instead.
2. **A kind number**: fetch the README and use the **Event Kinds** table. The NIP number is not the kind number. Kind 1 is NIP-01; kind 30023 is NIP-23; kind 10002 is NIP-65. One kind can be mentioned in several NIPs; the table is the index, the linked NIP is the definition.
3. **A feature** ("DMs", "zaps", "search", "lists"): fetch the README **List** first. Implement an existing NIP when one covers the feature. Check the struck-through entries so you do not build on NIP-04, NIP-08, NIP-15, NIP-26, NIP-28, or NIP-96.
4. **A tag letter**: the README has a tag list. Single-letter tags are what relays index. A multi-letter tag is not a `#filter` on a stock relay.

## Rules

- Quote the fetched file for field names, kinds, and tag order. If the fetch fails, say so. Do not fill the gap from memory.
- The `nostr` skill's `references/nips.md` is a routing cheat sheet. When it and the raw NIP disagree, the raw NIP wins.
- Do not invent a kind in `30000-39999` or anywhere else until the README shows the feature is missing. New kinds need a NIP-31 `alt` tag.
- NIP-90 (data vending machines) is marked unrecommended. Do not start one.
