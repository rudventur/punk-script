# PunkScript Repository Index

> Everything in this repo — the language spec and the prototype apps — in one place.

---

## Files

| File | Type | Description |
|------|------|-------------|
| `PUNKSCRIPT.md` | Spec / Manifesto | The PunkScript language specification v0.2 |
| `groks cam scanner` | Flutter / Dart | Phone-based 3D scanner app (camera + pedometer → .obj mesh) |
| `wifi-room-mapper.html` | HTML / JS | Interactive 3D WiFi signal mapper for rooms |
| `unit_architect.html` | HTML | Unit Architect v1.0 — placeholder/stub |

---

## PUNKSCRIPT.md — The Language

**What it is:** A personally-adaptive symbolic programming language where punctuation IS syntax and the interpreter adapts to the user, not the other way around.

### Core Concepts

| Concept | Summary |
|---------|---------|
| **Punctuation as syntax** | `.` ends statements, `!` executes, `?` is conditional, `...` loops |
| **Emoticon operators** | `:@D` = success, `>:@(` = error, `:/` = warning — first-class operators |
| **Personal dictionary** (`user.dict`) | Maps your own words/symbols to PunkScript operations |
| **User preferences** (`user.preferences`) | Controls fuzzy matching, case sensitivity, custom delimiters |
| **Pattern Watcher** | Interpreter observes your writing patterns and suggests new mappings |
| **Spelling forgiveness** | Fuzzy matching built in — dyslexia is a dialect, not a bug |
| **Custom string delimiters** | Define your own, e.g. `*!' ... '!*` |

### Standard Operators (quick ref)

| Symbol | Meaning | | Symbol | Meaning |
|--------|---------|-|--------|---------|
| `.` | End statement | | `!` | Execute/call |
| `:` | Assign/define | | `?` | If/conditional |
| `...` | Loop | | `-` | Else |
| `&` | And | | `\|` | Or |
| `~` | Not | | `[ ]` | Block/scope |

### Standard Keywords

`say` (print), `add/take/multiply/split` (arithmetic), `beats/under/is/isnt` (comparison), `stop/skip/keep going/give back` (control flow), `zero`–`ten`, `true/false/nothing` (literals).

### Example — FizzBuzz in PunkScript

```
count: zero.
keep going... [
  add one to (count).
  (count) beats one hundred? stop!
  fizz: (count) split by three is zero.
  buzz: (count) split by five is zero.
  (fizz) & (buzz)? say "FizzBuzz"!
  - (fizz)? say "Fizz"!
  - (buzz)? say "Buzz"!
  - say (count)!
]
```

---

## groks cam scanner — 3D Scanner App

**Language:** Dart (Flutter)
**Platform:** Android + iOS, 100% on-device
**File:** Single-file app (`lib/main.dart`)

### What it does

A phone-based 3D scanning app that uses the camera and step counter to generate `.obj` 3D meshes. Designed for scanning large structures like metro tunnels/platforms by walking through them.

### Key Components

| Component | Lines | Role |
|-----------|-------|------|
| **State management** (Riverpod) | 47–55 | Quality, scan mode, images, steps, model file providers |
| **HomeScreen** | 77–127 | Quality picker (Low/Medium/High) + capture mode (Photo/Video) |
| **CameraScreen** | 130–314 | Live camera preview, photo capture, video recording with auto-frame extraction (every 500ms), live step counter |
| **`_generateOnDevice3DStructure()`** | 317–359 | On-device point cloud generation → `.obj` file. Point count scales with quality + steps walked |
| **ModelViewerScreen** | 362–419 | 3D viewer with rotate/zoom/AR via `model_viewer_plus` |

### Quality Modes

| Mode | Points | Use case |
|------|--------|----------|
| Low ("Just Structure") | 800 + steps/10 | Metro tunnels, large sparse spaces |
| Medium | 3500 + steps/5 | General scanning |
| High | 12000 + steps | Detailed objects |

### Dependencies

`camera`, `pedometer`, `path_provider`, `permission_handler`, `video_player`, `model_viewer_plus`, `flutter_riverpod`

---

## wifi-room-mapper.html — WiFi Signal Mapper

**Language:** HTML + vanilla JS + Canvas
**Platform:** Browser (mobile-optimised)
**Size:** ~1370 lines, fully self-contained single file

### What it does

An interactive 3D room modelling tool that maps WiFi signal strength throughout a space. You define a room's dimensions, add walls with materials (concrete, brick, glass, etc.), drop furniture and environment objects, then place signal pins to visualise WiFi coverage as a heatmap.

### Key Features

| Feature | Description |
|---------|-------------|
| **3D room rendering** | Canvas-based 3D projection with rotation, zoom, and pan |
| **2D floor plan view** | Top-down alternative view |
| **Wall materials** | 7 types (concrete, brick, stud, wood, glass, metal, open) with dB attenuation values |
| **Furniture placement** | Desk, bed, shelf, sofa, table — rendered as 3D boxes |
| **Environment objects** | Router, microwave, mirror, aquarium — affect signal modelling |
| **Signal pins** | Drop pins with dBm readings, visualised as colour-coded markers |
| **Signal interpolation** | `interpolateDbm()` — inverse-distance-weighted interpolation between pins |
| **Heatmap overlay** | Signal strength heatmap across the floor plane |
| **Path scrubbing** | Walk-path playback with timeline scrubber |
| **Live WiFi reading** | Uses `navigator.connection` API for real-time signal data |
| **Gyroscope control** | Device orientation controls camera rotation |

### Main Functions

| Function | Role |
|----------|------|
| `project(x,y,z)` | 3D → 2D projection with camera rotation + FOV |
| `draw3D()` | Renders room walls, pins, heatmap, furniture in 3D |
| `draw2D()` | Top-down floor plan renderer |
| `drawFurniture3D(f)` | 3D box rendering for furniture items |
| `drawEnv()` | Renders environment objects with effect radii |
| `dbmColor(dbm)` | Maps signal strength to green/yellow/red colour |
| `interpolateDbm(x,z)` | IDW signal interpolation between placed pins |
| `startLiveReading()` | Polls `navigator.connection` for live signal |
| `handleGyro(e)` | Device orientation → camera rotation |
| `handleClick(cx,cy)` | Processes clicks for pin/furniture/env placement |
| `showScrub()` / `updateScrub()` | Walk-path timeline playback |

### Material Attenuation Table

| Material | dB loss |
|----------|---------|
| Concrete | -12 |
| Brick | -10 |
| Metal | -20 |
| Wood | -5 |
| Stud wall | -3 |
| Glass | -2 |
| Open | 0 |

---

## unit_architect.html — Stub

Placeholder file. Contains minimal HTML boilerplate with a message that the full Unit Architect code should be opened separately.

---

## How It All Connects

These aren't random files. They represent a philosophy: **tools built for people who think differently**.

- **PunkScript** — a language that adapts to how you write, not the other way around
- **3D Scanner** — 3D scanning without cloud services, just your phone and your feet
- **WiFi Mapper** — understanding your physical space through signal, not floor plans

All three share the same DNA: put the human first, keep it on-device, make complex things accessible.

---

*Index generated March 2026*
