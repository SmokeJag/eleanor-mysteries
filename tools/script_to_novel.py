#!/usr/bin/env python3
"""Convert a Ren'Py script into novel-style Markdown prose.

Reads script.rpy and produces a readable story document: narration as prose,
character dialogue with names, scene changes as section breaks, and choices
as "You choose:" lists. Ignores code (labels, image defs, transitions, etc.).
"""
import re
import sys
from pathlib import Path

# Character name map (extend as needed)
CHAR_NAMES = {
    "e": "Eleanor",
    "j": "Julian",
    "s": "The Servant",
    "h": "Mistress Harlow",
    "a": "Anubis",
    "n": "Neith",
}

# Scene background -> readable location label
SCENE_LABELS = {
    "bg village": "The Village",
    "bg mansion_ext": "The Mansion, Exterior",
    "bg hallway": "The Grand Hallway",
    "bg corridor_dark": "The Dark Corridor",
    "bg library": "The Library",
    "bg tome": "The Tome",
    "bg jewel": "The Jewel",
    "bg chamber": "The Hidden Chamber",
    "bg shore": "The Shore",
    "bg mansion": "The Mansion",
    "bg title": "Title",
    "bg boat": "The River",
    "bg scales": "The Hall of Two Truths",
    "bg tomb": "The Pyramid's Heart",
    "black": "Black",
}


def strip_tags(text: str) -> str:
    """Remove Ren'Py text tags like {b}, {/b}, {color=#...}, {size=+10}."""
    text = re.sub(r"\{/?[a-zA-Z_]+(?:=[^}]*)?\}", "", text)
    return text.strip()


def parse_script(path: Path):
    """Yield events: ('scene', label), ('dialogue', char, text), ('choice', [opts]), ('label', name)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i].strip()
        # Skip comments and blank lines
        if not line or line.startswith("#"):
            i += 1
            continue

        # scene X
        m = re.match(r"^scene\s+(.+)", line)
        if m:
            yield ("scene", m.group(1).strip())
            i += 1
            continue

        # label X:
        m = re.match(r"^label\s+(\w+)", line)
        if m:
            yield ("label", m.group(1))
            i += 1
            continue

        # menu:
        if line == "menu:":
            # collect option captions (lines like  "Caption":  ) until the
            # indentation returns to the menu's own level (end of block)
            menu_indent = len(lines[i]) - len(lines[i].lstrip())
            opts = []
            i += 1
            while i < n:
                raw = lines[i]
                stripped = raw.strip()
                if not stripped:
                    i += 1
                    continue
                indent = len(raw) - len(raw.lstrip())
                # A caption is a quoted string, optionally followed by a
                # conditional clause ("...\" if cond:"), then a colon
                m = re.match(r'^"([^"]*)"(?:\s+if\s+.+?)?\s*:', stripped)
                if m:
                    opts.append(strip_tags(m.group(1)))
                    i += 1
                    continue
                # Stop when indentation returns to the menu's own level
                # (or less) — the menu block has ended.
                if indent <= menu_indent:
                    break
                # Otherwise skip the indented option body
                i += 1
            if opts:
                yield ("choice", opts)
            continue

        # character dialogue:  e "text"  or  j "text"
        # (exclude Ren'Py keywords that also look like "word \"...\"")
        m = re.match(r"^([a-zA-Z_]+)\s+\"", line)
        if m and m.group(1) not in (
            "if", "elif", "else", "while", "for", "return", "jump", "call",
            "show", "hide", "scene", "with", "pause", "menu", "label",
            "define", "default", "init", "python", "window", "play", "stop",
            "queue", "voice", "centered", "nvl", "extend", "pass", "break",
        ):
            char = m.group(1)
            # gather the quoted text (may span multiple lines)
            text = line[m.end() - 1:]  # from the opening quote
            # find closing quote
            while '"' not in text[1:]:
                i += 1
                if i >= n:
                    break
                text += "\n" + lines[i].strip()
            # extract between first and last quote
            parts = text.split('"')
            if len(parts) >= 3:
                content = parts[1]
            else:
                content = text
            yield ("dialogue", char, strip_tags(content))
            i += 1
            continue

        # centered "text"  -> emphasis
        m = re.match(r'^centered\s+"', line)
        if m:
            text = line
            while '"' not in text[1:]:
                i += 1
                if i >= n:
                    break
                text += "\n" + lines[i].strip()
            parts = text.split('"')
            content = parts[1] if len(parts) >= 3 else text
            yield ("narration", f"*{strip_tags(content)}*")
            i += 1
            continue

        # narration:  "text"
        if line.startswith('"'):
            text = line
            while '"' not in text[1:]:
                i += 1
                if i >= n:
                    break
                text += "\n" + lines[i].strip()
            parts = text.split('"')
            content = parts[1] if len(parts) >= 3 else text
            yield ("narration", strip_tags(content))
            i += 1
            continue

        # anything else (code, show/hide, $, if, jump, etc.) — skip
        i += 1


def render(events):
    out = []
    out.append("# ELEANOR: The Mansion Mysteries")
    out.append("")
    out.append("*A novel-style reading of the game script.*")
    out.append("")
    out.append("---")
    out.append("")

    last_scene = None
    for ev in events:
        kind = ev[0]
        if kind == "label":
            name = ev[1]
            # Only break for major story beats, skip internal labels
            if name in ("start", "ending_redemption", "ending_power"):
                out.append("")
                out.append("---")
                out.append("")
        elif kind == "scene":
            label = SCENE_LABELS.get(ev[1], ev[1])
            if label != last_scene:
                out.append("")
                out.append(f"### {label}")
                out.append("")
                last_scene = label
        elif kind == "narration":
            out.append(ev[1])
            out.append("")
        elif kind == "dialogue":
            char = CHAR_NAMES.get(ev[1], ev[1])
            out.append(f"**{char}:** {ev[2]}")
            out.append("")
        elif kind == "choice":
            out.append("> **You choose:**")
            for opt in ev[1]:
                out.append(f"> - {opt}")
            out.append("")

    return "\n".join(out).strip() + "\n"


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("game/script.rpy")
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("ELEANOR_story.md")
    events = list(parse_script(src))
    md = render(events)
    dst.write_text(md, encoding="utf-8")
    print(f"Wrote {len(md)} chars to {dst}")


if __name__ == "__main__":
    main()
