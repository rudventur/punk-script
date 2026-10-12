#!/usr/bin/env python3
"""
CNC Picture → G-code (pixel language + rules)

Self-contained tool for wood & metal CNC mills/routers.

- Picture / pixel language: loads image, treats brightness as Z-depth (height map)
- Rules: tool diameter, max depth, stepover, feed, plunge, safe Z, units, invert, etc.
- Output: simple raster G-code (GRBL / LinuxCNC compatible)

Usage:
  python3 cnc_picture2gcode.py image.png -o out.nc --width 100 --max-depth 2.0 --feed 800

Requires: Pillow (pip install pillow)
Optional: numpy for faster processing
"""

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow required: pip install pillow")
    sys.exit(1)

def generate_gcode(image_path, width_mm, max_depth_mm, stepover_mm,
                   feed_rate, plunge_rate, safe_z, invert=False,
                   units="mm", tool_diameter=3.0, line_angle=0):
    img = Image.open(image_path).convert("L")  # grayscale
    w_px, h_px = img.size
    scale = width_mm / w_px
    height_mm = h_px * scale

    pixels = list(img.getdata())
    # Normalize 0-255 → depth
    def depth_from_px(px):
        norm = px / 255.0
        if invert:
            norm = 1.0 - norm
        return -max_depth_mm * norm  # negative Z for cutting down

    gcode = []
    gcode.append(f"( Picture2Gcode - {Path(image_path).name} )")
    gcode.append(f"( Size: {width_mm:.2f} x {height_mm:.2f} {units} )")
    gcode.append(f"( Max depth: {max_depth_mm} mm, Tool: {tool_diameter} mm )")
    gcode.append("G21" if units == "mm" else "G20")  # units
    gcode.append("G90")  # absolute
    gcode.append("G17")  # XY plane
    gcode.append(f"G0 Z{safe_z:.3f}")  # safe height
    gcode.append("M3 S10000")  # spindle on (adjust for your machine)

    step_px = max(1, int(stepover_mm / scale))
    y = 0
    direction = 1  # zig-zag

    while y < h_px:
        row_depths = []
        for x in range(0, w_px, step_px):
            idx = y * w_px + min(x, w_px - 1)
            d = depth_from_px(pixels[idx])
            row_depths.append((x * scale, d))

        if direction < 0:
            row_depths.reverse()

        if row_depths:
            first_x, first_d = row_depths[0]
            gcode.append(f"G0 X{first_x:.3f} Y{y * scale:.3f}")
            gcode.append(f"G1 Z{first_d:.3f} F{plunge_rate}")

            for x_mm, d in row_depths[1:]:
                gcode.append(f"G1 X{x_mm:.3f} Y{y * scale:.3f} Z{d:.3f} F{feed_rate}")

            gcode.append(f"G0 Z{safe_z:.3f}")

        y += step_px
        direction *= -1

    gcode.append(f"G0 Z{safe_z:.3f}")
    gcode.append("M5")  # spindle off
    gcode.append("G0 X0 Y0")
    gcode.append("( End )")
    return "\n".join(gcode)

def main():
    parser = argparse.ArgumentParser(description="Picture (pixel) → CNC G-code with rules")
    parser.add_argument("image", help="Input image (PNG/JPG)")
    parser.add_argument("-o", "--output", default="out.nc", help="Output G-code file")
    parser.add_argument("--width", type=float, default=100.0, help="Output width in mm")
    parser.add_argument("--max-depth", type=float, default=2.0, help="Max cutting depth mm")
    parser.add_argument("--stepover", type=float, default=1.0, help="Stepover mm (smaller = finer)")
    parser.add_argument("--feed", type=float, default=800, help="Feed rate mm/min")
    parser.add_argument("--plunge", type=float, default=300, help="Plunge rate mm/min")
    parser.add_argument("--safe-z", type=float, default=5.0, help="Safe Z height")
    parser.add_argument("--tool", type=float, default=3.0, help="Tool diameter mm (for info)")
    parser.add_argument("--invert", action="store_true", help="Invert brightness (dark = shallow)")
    parser.add_argument("--units", choices=["mm", "inch"], default="mm")

    args = parser.parse_args()

    gcode = generate_gcode(
        args.image, args.width, args.max_depth, args.stepover,
        args.feed, args.plunge, args.safe_z, args.invert,
        args.units, args.tool
    )

    Path(args.output).write_text(gcode)
    print(f"Wrote {args.output}  ({len(gcode.splitlines())} lines)")
    print("Preview in CAMotics or your sender before running on metal!")

if __name__ == "__main__":
    main()
