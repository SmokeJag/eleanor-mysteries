# 🎨 MANSION MYSTERIES — ASSET HANDOVER LIST (for the M3)
> What's done, what's still placeholder, and what the M3 needs to generate.
> **Last updated:** 19 Aug 2026

---

## ✅ DONE — real art already in the game

| File | Type | Size | Notes |
|------|------|------|-------|
| `backgrounds/bg_mansion_restored.webp` | Background | 1024×576 | Refurbished mansion + rose garden (opening) |
| `backgrounds/bg_hallway.webp` | Background | 1024×576 | Refurbished grand hallway |
| `backgrounds/bg_library.webp` | Background | 1024×576 | Refurbished library, cosy fire |
| `sprites/corvus.png` | Sprite | 576×1024 | The collector (Corvus) |
| `ui/scarab_amulet.png` | UI/Item | 1024×1024 | The Duat's Echo amulet |

---

## ⚠️ STILL PLACEHOLDER — need real art (the M3's job)

These are currently **solid colour blocks** in the game. The M3 should generate
**semi-realistic Daz-style renders** matching the trilogy's look.

### Character sprites (720×1080, white/transparent background)
| Alias | Character | Description |
|-------|-----------|-------------|
| `eleanor_neutral` | Eleanor | Dark-haired woman, late 20s, sharp determined eyes. Victorian detective attire — fitted dark coat, satchel. The trilogy's Eleanor, now a detective. |
| `eleanor_determined` | Eleanor | Same, more intense/ready expression. |
| `neith_neutral` | Neith | The priestess/partner. Warm bronze skin, dark hair bound with gold, kohl-lined eyes. Pale linen + gold, calm ancient stillness. (Reuse the Scales of Ma'at Neith model with tweaks.) |
| `curator` | The Curator | Thin, sharp East End antiquities dealer. Quick watchful eyes, dusty shopkeeper look. |
| `jaguar_spirit` | The Jaguar | The freed jaguar spirit — a great black jaguar, eyes burning, semi-transparent/ghostly. |

### Backgrounds (1920×1080)
| Alias | Scene | Description |
|-------|-------|-------------|
| *(optional)* `bg_curator_shop` | The Curator's shop | Cramped, dusty East End curiosity den — old paper, beeswax, secrets. |

---

## 📐 SIZE / FORMAT SPEC (match the trilogy)
- **Backgrounds:** 1920×1080, export as **WEBP** (quality 90) — keeps the game small.
- **Sprites:** 720×1080, **PNG with transparency** (alpha) for character sprites.
- **Style:** semi-realistic Daz render, Gothic-tinged, gold + obsidian + warm lamplight palette.
- **Consistency:** Eleanor and Neith must match their trilogy models (Eleanor's explorer look; Neith's priestess look) so the series feels continuous.

---

## 🖥️ HOW TO WIRE IN (once the M3 has the art)
Drop the files into `game/images/` (backgrounds → `backgrounds/`, sprites → `sprites/`),
then update the `image` aliases in `game/script.rpy` from `Solid("#...")` to the file path.
I can do this wiring on this machine once the files are synced via git.

---

## ⚠️ NOTE FOR THE M3
**Do NOT run ten generations at once.** Generate in small batches (2–3 at a time),
check each for style consistency, and only proceed once the look is right. The
trilogy's art is the reference — match it.
