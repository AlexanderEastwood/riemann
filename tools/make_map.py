#!/usr/bin/env python3
"""Render research-map.json as a Mermaid diagram inside RESEARCH_MAP.md.

Usage:  python3 tools/make_map.py

GitHub renders Mermaid natively, so the map is visible in the browser with
no build step. Edit research-map.json and re-run; do not hand-edit the
generated markdown.
"""
import json, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / "research-map.json", ROOT / "RESEARCH_MAP.md"

def _repo_url() -> str:
    """Absolute web URL of the GitHub remote (for Mermaid click targets)."""
    import subprocess, re
    try:
        u = subprocess.run(["git", "remote", "get-url", "origin"], cwd=ROOT,
                           capture_output=True, text=True, check=True).stdout.strip()
        m = re.search(r"github\.com[:/]([^/]+)/([^/.]+)", u)
        if m:
            return f"https://github.com/{m.group(1)}/{m.group(2)}"
    except Exception:
        pass
    return "https://github.com/AlexanderEastwood/riemann"

REPO_URL = _repo_url()

STYLE = {
    "proved":  ("#1b5e20", "#a5d6a7", "proved"),
    "live":    ("#f57f17", "#ffd54f", "live"),      # gold: the routes currently being worked
    "closed":  ("#b71c1c", "#ef9a9a", "closed"),    # red: proved dead ends, kept deliberately
    "blocked": ("#4a148c", "#ce93d8", "blocked"),
    "open":    ("#37474f", "#cfd8dc", "open"),
}
MARK = {"proved": "[x]", "live": "[~]", "closed": "[X]",
        "blocked": "[!]", "open": "[ ]"}

def esc(s: str) -> str:
    return s.replace('"', "'").replace("\n", " ")

def main() -> int:
    doc = json.loads(SRC.read_text())
    nodes = doc["nodes"]
    by_id = {n["id"]: n for n in nodes}
    kids = collections.defaultdict(list)
    for n in nodes:
        kids[n.get("parent")].append(n)

    L = [f"# {doc['title']}", "",
         f"_Generated from `research-map.json` — last updated {doc['updated']}._",
         "_Do not hand-edit: run `python3 tools/make_map.py`._", "", "```mermaid",
         "graph LR"]

    for n in nodes:
        label = esc(n["title"])
        if n.get("prop"):
            label += f"<br/><small>{esc(n['prop'])}</small>"
        ev = n.get("evidence")
        if ev == "MISSING":
            label += "<br/><small>EVIDENCE MISSING</small>"
        elif ev:
            label += f"<br/><small>&#128193; {esc(ev)}</small>"
        L.append(f'  {n["id"]}["{label}"]')
    L.append("")
    for n in nodes:
        if n.get("parent"):
            L.append(f'  {n["parent"]} --> {n["id"]}')
    L.append("")
    # GitHub renders Mermaid in a sandboxed iframe (viewscreen.githubusercontent.com),
    # so a RELATIVE click href resolves against that origin and 404s. Emit absolute
    # repository URLs and open them in a new tab.
    for n in nodes:
        ev = n.get("evidence")
        if ev and ev != "MISSING":
            L.append(f'  click {n["id"]} "{REPO_URL}/tree/main/{ev}/" "evidence: {ev}" _blank')
    L.append("")
    for status, (fg, bg, _) in STYLE.items():
        ids = [n["id"] for n in nodes if n["status"] == status]
        if ids:
            width = "3px" if status == "live" else "1px"
            L.append(f"  classDef {status} fill:{bg},stroke:{fg},stroke-width:{width},color:#000;")
            L.append(f"  class {','.join(ids)} {status};")
    # legend row so the colours are readable without the table below
    L.append('  subgraph Legend')
    L.append('    direction LR')
    L.append('    lg_live["current route (gold)"]:::live')
    L.append('    lg_closed["closed route"]:::closed')
    L.append('    lg_proved["proved"]:::proved')
    L.append('    lg_open["open"]:::open')
    L.append('    lg_blocked["blocked"]:::blocked')
    L.append('  end')
    L += ["```", "", "## Status", ""]

    c = collections.Counter(n["status"] for n in nodes)
    L.append("| status | count | meaning |")
    L.append("|---|---:|---|")
    for s, desc in doc["legend"].items():
        L.append(f"| `{s}` | {c.get(s,0)} | {desc} |")

    L += ["", "## Nodes", ""]

    def walk(parent, depth):
        for n in sorted(kids[parent], key=lambda x: x["title"]):
            bits = []
            if n.get("prop"):
                bits.append(f"`{n['prop']}`")
            if n.get("branch"):
                bits.append(f"`{n['branch']}`")
            ev = n.get("evidence")
            if ev == "MISSING":
                bits.append("**evidence missing**")
            elif ev:
                bits.append(f"evidence: [`{ev}/`]({ev}/)")
            if n.get("note"):
                bits.append(n["note"])
            L.append("  " * depth + f"- {MARK[n['status']]} **{n['title']}**"
                     + (" — " + " · ".join(bits) if bits else ""))
            walk(n["id"], depth + 1)

    walk(None, 0)
    L += ["", "## Reading it", "",
          "Each node is an idea. A node with children is a branch point: the",
          "children are the sub-ideas tried from it. `closed` children are proved",
          "dead ends and are kept deliberately — they are the project's main",
          "output. `live` is the only node currently worth spending on.", "",
          "Nodes marked with a folder icon are clickable in the diagram and link",
          "to the `evidence/vNNN/` directory holding their certificates; the same",
          "links appear in the list above.", ""]

    OUT.write_text("\n".join(L) + "\n")
    print(f"{OUT.name}: {len(nodes)} nodes, {dict(c)}")

    # Also splice the diagram into README.md between markers, so the README
    # renders it directly and cannot drift from research-map.json.
    i, j = L.index("```mermaid"), L.index("```", L.index("```mermaid") + 1)
    diagram = "\n".join(L[i:j + 1])
    readme = ROOT / "README.md"
    start, end = "<!-- research-map:start -->", "<!-- research-map:end -->"
    if readme.exists():
        r = readme.read_text()
        if start in r and end in r:
            a, b = r.index(start) + len(start), r.index(end)
            r = r[:a] + "\n" + diagram + "\n" + r[b:]
            readme.write_text(r)
            print(f"README.md: diagram updated between markers ({j - i + 1} lines)")
        else:
            print("README.md: markers not found; diagram not spliced")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
