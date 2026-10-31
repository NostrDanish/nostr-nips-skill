#!/usr/bin/env python3
"""Fetch live NIP text and resolve a kind number to the NIP that defines it.

  python3 scripts/nip.py selftest
  python3 scripts/nip.py get 01
  python3 scripts/nip.py get 90
  python3 scripts/nip.py kind 1
  python3 scripts/nip.py readme

Always prints the upstream markdown. It does not guess a NIP that is not in
the file it just fetched. Raw URLs only — github.com blob pages are HTML.
"""
import re
import sys
import urllib.request

RAW = "https://raw.githubusercontent.com/nostr-protocol/nips/master/"


def fetch(name):
    req = urllib.request.Request(
        RAW + name,
        headers={"User-Agent": "nostr-nips-skill", "Accept": "text/plain"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def nip_filename(token):
    token = token.strip().removesuffix(".md")
    if token.isdigit():
        token = f"{int(token):02d}"
    if not re.fullmatch(r"[0-9A-Za-z]{2,4}", token):
        raise SystemExit(f"not a NIP id: {token}")
    if any(c.isalpha() for c in token):
        return token.upper() + ".md"
    return token + ".md"


def kind_rows(markdown):
    """Return (kind cell, description, nip cell) from README tables."""
    rows = []
    header = None
    for line in markdown.splitlines():
        if not line.startswith("|"):
            header = None
            continue
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if not cells or set("".join(cells)) <= set("-: "):
            continue
        low = [c.lower() for c in cells]
        if "kind" in low[0] or low[0] == "kind":
            header = low
            continue
        if header is None:
            continue
        kind, desc, nip = cells[0], cells[1] if len(cells) > 1 else "", cells[-1]
        rows.append((kind, desc, nip))
    return rows


def _kind_matches(cell, kind):
    cell = cell.replace(" ", "")
    if cell == str(kind):
        return True
    for part in re.split(r"[,/]|and", cell):
        part = part.strip()
        m = re.fullmatch(r"(\d+)\s*[-–]\s*(\d+)", part)
        if m and int(m.group(1)) <= kind <= int(m.group(2)):
            return True
        if part == str(kind):
            return True
    return False


def nip_ids(cell):
    found = re.findall(r"\[([0-9A-Za-z]{1,4})\]\([^)]+\)", cell)
    out = []
    for token in found:
        if token.upper().startswith("NKBIP"):
            continue
        if token not in out:
            out.append(token)
    return out


def lookup_kind(markdown, kind):
    hits = [row for row in kind_rows(markdown) if _kind_matches(row[0], kind)]
    return hits


FIXTURE = """
| kind | description | NIP |
|------|-------------|-----|
| `0`  | Metadata    | 01 |
| `1`  | Short note  | 01, 10 |
| 5000-5999 | job request | 90 |
| 4–44 | regular     | 01 |
"""


def selftest():
    ok = True

    def check(name, cond):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + name)
        ok = ok and bool(cond)

    check("file-01", nip_filename("1") == "01.md")
    check("file-b7", nip_filename("b7") == "B7.md")
    rows = lookup_kind(FIXTURE, 1)
    check("kind-1", rows and rows[0][2] == "01, 10")
    check("kind-range", lookup_kind(FIXTURE, 5050)[0][2] == "90")
    check("kind-dash", lookup_kind(FIXTURE, 41)[0][2] == "01")
    check("kind-miss", lookup_kind(FIXTURE, 99999) == [])
    check("nip-link", nip_ids("[10](10.md)") == ["10"])
    check("nip-two", nip_ids("[51](51.md), [58](58.md)") == ["51", "58"])
    check("nip-skip-ref", nip_ids("[NKBIP-03]") == [])
    return ok


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "selftest":
        sys.exit(0 if selftest() else 1)
    if cmd == "get" and len(sys.argv) > 2:
        print(fetch(nip_filename(sys.argv[2])))
        return
    if cmd == "readme":
        print(fetch("README.md"))
        return
    if cmd == "kind" and len(sys.argv) > 2:
        kind = int(sys.argv[2])
        md = fetch("README.md")
        hits = lookup_kind(md, kind)
        if not hits:
            print(f"NO ROW for kind {kind} in the NIPs README.", file=sys.stderr)
            print("Do not invent a NIP. Run `nip.py readme` or check", file=sys.stderr)
            print("https://github.com/nostr-protocol/registry-of-kinds", file=sys.stderr)
            sys.exit(1)
        for kind_cell, desc, nip in hits:
            print(f"kind {kind_cell}: {desc}")
            ids = nip_ids(nip)
            if ids:
                print("NIP " + ", ".join(ids))
                for token in ids:
                    print(f"fetch: {RAW}{nip_filename(token)}")
            else:
                print(f"NIP cell: {nip or '(empty)'}")
        return
    print(__doc__)
    sys.exit(1)


if __name__ == "__main__":
    main()
