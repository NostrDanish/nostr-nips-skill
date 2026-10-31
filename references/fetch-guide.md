# Fetching NIPs

## URLs

| What | Raw (preferred) | Rendered |
|---|---|---|
| Index | `https://raw.githubusercontent.com/nostr-protocol/nips/master/README.md` | blob `/README.md` |
| One NIP | `https://raw.githubusercontent.com/nostr-protocol/nips/master/{NIP}.md` | blob `/{NIP}.md` |

`{NIP}` is the filename stem: `01`, `46`, `B7`, `C7`. Not the kind number.

## Kind → NIP

1. Fetch the README.
2. Find the **Event Kinds** table.
3. Note the NIP column (may be more than one; may be an external spec).
4. Fetch that file. If the README says unrecommended, stop unless asked to
   debug legacy events.

## Tag / message type → NIP

Same README: **Message Types** (EVENT/REQ/CLOSE/AUTH/COUNT) and the tag
conventions scattered in individual NIPs. NIP-01 is the wire protocol.

## If GitHub fails

1. Retry the raw URL once.
2. Try the rendered blob URL.
3. If still failing, use the offline snapshot in the `nostr` skill
   (`references/nips.md`, `references/kinds.md`) and **label it stale**.
   Do not invent tags or kinds that are not in either source.

## Do not

- Guess a NIP from a kind (`kind 17` is not NIP-17).
- Treat a PR or gist as merged until it is in `master`.
- Cache NIP text across sessions as if it cannot change.
