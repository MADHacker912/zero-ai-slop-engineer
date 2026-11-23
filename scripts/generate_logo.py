import sys
from PIL import Image, ImageDraw

def create_pixel_logo():
    # 64x64 pixel art grid
    W, H = 64, 64
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Color palette
    BG_DARK = (10, 15, 29, 255)       # #0a0f1d
    BG_CARD = (15, 23, 42, 255)       # #0f172a
    BORDER = (56, 189, 248, 255)      # #38bdf8 cyan
    BORDER_DIM = (30, 58, 138, 255)   # #1e3a8a deep blue
    
    DESK = (51, 65, 85, 255)          # #334155
    DESK_TOP = (71, 85, 105, 255)     # #475569
    
    # Computer colors
    PC_CASE = (30, 41, 59, 255)       # #1e293b
    PC_FRAME = (51, 65, 85, 255)      # #334155
    SCREEN_BG = (8, 47, 73, 255)      # #082f49
    SCREEN_GLOW = (14, 165, 233, 255) # #0ea5e9
    CODE_GREEN = (52, 211, 153, 255)  # #34d399 emerald
    CODE_AMBER = (251, 191, 36, 255)  # #fbbf24 amber
    CODE_WHITE = (241, 245, 249, 255) # #f1f5f9
    KB_BASE = (30, 41, 59, 255)
    KB_KEY = (148, 163, 184, 255)
    
    # Humanised Agent colors
    SKIN = (255, 205, 165, 255)       # Warm skin
    SKIN_SHADOW = (225, 165, 125, 255)
    HAIR = (45, 25, 20, 255)          # Dark brown hair
    HAIR_HI = (120, 70, 50, 255)
    HOODIE = (16, 185, 129, 255)      # Emerald/Teal cyber hoodie
    HOODIE_DARK = (5, 150, 105, 255)
    HOODIE_INNER = (4, 120, 87, 255)
    HEADSET = (99, 102, 241, 255)     # Indigo/cyber purple headset
    MIC_GLOW = (56, 189, 248, 255)    # Cyan glow mic
    CYBER_EYE = (56, 189, 248, 255)   # Cyan AR monocle / cyber eye
    EYE_BLACK = (15, 23, 42, 255)
    HEART_GLOW = (244, 63, 94, 255)   # Rose red (human soul / empathy)

    # 1. Background rounded rectangle
    for y in range(2, 62):
        for x in range(2, 62):
            # Rounded corners
            if (x in (2, 3) and y in (2, 3)) or (x in (60, 61) and y in (2, 3)) or \
               (x in (2, 3) and y in (60, 61)) or (x in (60, 61) and y in (60, 61)):
                continue
            draw.point((x, y), fill=BG_DARK)

    # Outer border
    for x in range(4, 60):
        draw.point((x, 2), fill=BORDER_DIM)
        draw.point((x, 61), fill=BORDER_DIM)
    for y in range(4, 60):
        draw.point((2, y), fill=BORDER_DIM)
        draw.point((61, y), fill=BORDER_DIM)
    
    # Corner brackets / tech accents
    corners = [(3, 3), (4, 3), (3, 4), (59, 3), (60, 3), (60, 4),
               (3, 59), (3, 60), (4, 60), (60, 59), (59, 60), (60, 60)]
    for pt in corners:
        draw.point(pt, fill=BORDER)

    # 2. Desk Surface (y = 44 to 47)
    for y in range(44, 48):
        for x in range(6, 58):
            draw.point((x, y), fill=DESK_TOP if y == 44 else DESK)

    # 3. Computer Monitor (Left side: x = 8 to 30, y = 18 to 38)
    # Monitor Stand
    for y in range(38, 44):
        for x in range(17, 21):
            draw.point((x, y), fill=PC_FRAME)
    # Stand Base
    for x in range(14, 24):
        draw.point((x, 43), fill=PC_CASE)

    # Monitor Bezel
    for y in range(18, 39):
        for x in range(8, 31):
            draw.point((x, y), fill=PC_CASE)

    # Monitor Screen (x = 10 to 28, y = 20 to 36)
    for y in range(20, 37):
        for x in range(10, 29):
            draw.point((x, y), fill=SCREEN_BG)

    # Screen Code Lines & Terminal
    # Prompt line 1: ">_ ZERO"
    draw.point((12, 22), fill=CODE_AMBER)
    draw.point((13, 22), fill=CODE_AMBER)
    draw.point((14, 23), fill=CODE_AMBER)
    draw.point((13, 24), fill=CODE_AMBER)
    draw.point((12, 24), fill=CODE_AMBER)
    
    for x in range(16, 27):
        draw.point((x, 23), fill=CODE_GREEN)

    # Line 2: SLOP = 0
    for x in range(12, 20):
        draw.point((x, 26), fill=SCREEN_GLOW)
    for x in range(22, 26):
        draw.point((x, 26), fill=CODE_WHITE)

    # Line 3: Clean Arch blocks
    for x in range(12, 17):
        draw.point((x, 29), fill=CODE_GREEN)
    for x in range(19, 27):
        draw.point((x, 29), fill=SCREEN_GLOW)

    # Line 4: Cursor blink
    for x in range(12, 23):
        draw.point((x, 32), fill=CODE_WHITE)
    draw.point((25, 32), fill=BORDER) # Cursor block
    draw.point((26, 32), fill=BORDER)

    # Status LED on monitor
    draw.point((19, 37), fill=CODE_GREEN)

    # Keyboard & Mouse
    for y in range(41, 44):
        for x in range(11, 23):
            draw.point((x, y), fill=KB_BASE)
    # Key dots
    for x in range(12, 22, 2):
        draw.point((x, 42), fill=KB_KEY)
    # Mouse
    draw.point((25, 42), fill=KB_KEY)
    draw.point((25, 43), fill=KB_BASE)

    # 4. Humanised Agent (Right side: center ~ x=42)
    # Agent Body / Hoodie (y = 35 to 49, x = 32 to 54)
    for y in range(36, 49):
        for x in range(34, 53):
            # Taper shoulders
            if y == 36 and (x < 39 or x > 47):
                continue
            if y == 37 and (x < 37 or x > 49):
                continue
            draw.point((x, y), fill=HOODIE)

    # Hoodie collar & inner detail
    for y in range(36, 42):
        draw.point((43, y), fill=HOODIE_INNER)
        draw.point((42, y), fill=HOODIE_DARK)

    # Glowing Human Heart / Core Badge (Empathy + Senior Integrity)
    draw.point((40, 41), fill=HEART_GLOW)
    draw.point((41, 41), fill=HEART_GLOW)
    draw.point((39, 40), fill=HEART_GLOW)
    draw.point((42, 40), fill=HEART_GLOW)

    # Left arm reaching to keyboard
    for y in range(39, 44):
        draw.point((33, y), fill=HOODIE)
        draw.point((32, y), fill=HOODIE_DARK)
    # Hand on keyboard
    draw.point((30, 42), fill=SKIN)
    draw.point((31, 42), fill=SKIN)
    draw.point((30, 43), fill=SKIN_SHADOW)

    # Right arm / hand gesturing or coding
    for y in range(39, 44):
        draw.point((53, y), fill=HOODIE)
    draw.point((54, 41), fill=SKIN)
    draw.point((54, 42), fill=SKIN)

    # Head / Face (x = 38 to 48, y = 22 to 34)
    # Neck
    for y in range(33, 36):
        for x in range(41, 46):
            draw.point((x, y), fill=SKIN_SHADOW if y == 35 else SKIN)

    # Face base
    for y in range(23, 33):
        for x in range(38, 48):
            draw.point((x, y), fill=SKIN)

    # Hair (Top & sides)
    for y in range(17, 24):
        for x in range(37, 49):
            if y == 17 and (x < 40 or x > 46):
                continue
            draw.point((x, y), fill=HAIR)
    # Hair bangs / texture
    draw.point((39, 23), fill=HAIR)
    draw.point((40, 24), fill=HAIR)
    draw.point((44, 23), fill=HAIR_HI)
    draw.point((47, 23), fill=HAIR)
    draw.point((48, 24), fill=HAIR)
    draw.point((37, 24), fill=HAIR)

    # Left eye (Human, warm, smart)
    draw.point((40, 27), fill=EYE_BLACK)
    draw.point((40, 26), fill=EYE_BLACK)
    draw.point((41, 26), fill=SKIN_SHADOW)

    # Right eye (Cyber HUD monocle / AR glasses)
    # Frame
    draw.point((44, 26), fill=BORDER)
    draw.point((45, 26), fill=BORDER)
    draw.point((46, 26), fill=BORDER)
    draw.point((44, 27), fill=BORDER)
    draw.point((46, 27), fill=BORDER)
    draw.point((45, 27), fill=CYBER_EYE) # Glowing lens
    draw.point((47, 26), fill=BORDER) # Monocle bridge

    # Friendly confident smile
    draw.point((41, 30), fill=SKIN_SHADOW)
    draw.point((42, 31), fill=SKIN_SHADOW)
    draw.point((43, 31), fill=SKIN_SHADOW)
    draw.point((44, 30), fill=SKIN_SHADOW)

    # Cyber Headset with Mic
    # Headband
    for x in range(38, 48):
        draw.point((x, 19), fill=HEADSET)
    # Earcups
    draw.point((36, 24), fill=HEADSET)
    draw.point((36, 25), fill=HEADSET)
    draw.point((36, 26), fill=HEADSET)
    draw.point((49, 24), fill=HEADSET)
    draw.point((49, 25), fill=HEADSET)
    draw.point((49, 26), fill=HEADSET)
    # Mic arm
    draw.point((36, 27), fill=HEADSET)
    draw.point((37, 28), fill=HEADSET)
    draw.point((38, 29), fill=MIC_GLOW) # Glowing mic tip!

    # 5. Floating pixel spark / AI sparks (Top Right & Left)
    spark_cyan = [(54, 12), (53, 13), (55, 13), (54, 14)]
    for pt in spark_cyan:
        draw.point(pt, fill=BORDER)
    
    spark_amber = [(12, 11), (11, 12), (13, 12), (12, 13)]
    for pt in spark_amber:
        draw.point(pt, fill=CODE_AMBER)

    spark_green = [(57, 24), (58, 25)]
    for pt in spark_green:
        draw.point(pt, fill=CODE_GREEN)

    # 6. Bottom Banner / Tech Badge: "ZERO SLOP"
    # Plate background
    for y in range(50, 57):
        for x in range(10, 54):
            draw.point((x, y), fill=BG_CARD)
    # Plate borders
    for x in range(10, 54):
        draw.point((x, 50), fill=BORDER_DIM)
        draw.point((x, 56), fill=BORDER_DIM)
    draw.point((10, 50), fill=BORDER)
    draw.point((53, 50), fill=BORDER)
    draw.point((10, 56), fill=BORDER)
    draw.point((53, 56), fill=BORDER)

    # Micro text in pixels: "ZERO SLOP"
    # Z
    for x in (14, 15, 16): draw.point((x, 52), fill=CODE_WHITE); draw.point((x, 54), fill=CODE_WHITE)
    draw.point((15, 53), fill=CODE_WHITE)
    # E
    for y in (52, 53, 54): draw.point((18, y), fill=CODE_WHITE)
    draw.point((19, 52), fill=CODE_WHITE); draw.point((19, 53), fill=CODE_WHITE); draw.point((19, 54), fill=CODE_WHITE)
    # R
    for y in (52, 53, 54): draw.point((21, y), fill=CODE_WHITE)
    draw.point((22, 52), fill=CODE_WHITE); draw.point((22, 53), fill=CODE_WHITE); draw.point((22, 54), fill=CODE_WHITE)
    # O
    for y in (52, 53, 54): draw.point((24, y), fill=CODE_WHITE); draw.point((26, y), fill=CODE_WHITE)
    draw.point((25, 52), fill=CODE_WHITE); draw.point((25, 54), fill=CODE_WHITE)

    # Star / Dot divider
    draw.point((29, 53), fill=BORDER)

    # S
    draw.point((32, 52), fill=CODE_GREEN); draw.point((33, 52), fill=CODE_GREEN)
    draw.point((32, 53), fill=CODE_GREEN); draw.point((33, 54), fill=CODE_GREEN); draw.point((32, 54), fill=CODE_GREEN)
    # L
    for y in (52, 53, 54): draw.point((35, y), fill=CODE_GREEN)
    draw.point((36, 54), fill=CODE_GREEN)
    # O
    for y in (52, 53, 54): draw.point((38, y), fill=CODE_GREEN); draw.point((40, y), fill=CODE_GREEN)
    draw.point((39, 52), fill=CODE_GREEN); draw.point((39, 54), fill=CODE_GREEN)
    # P
    for y in (52, 53, 54): draw.point((42, y), fill=CODE_GREEN)
    draw.point((43, 52), fill=CODE_GREEN); draw.point((43, 53), fill=CODE_GREEN)

    # Status pulse dot on right of banner
    draw.point((48, 53), fill=CODE_GREEN)
    draw.point((49, 53), fill=MIC_GLOW)

    # Save original 64x64
    img.save("/home/obito/zero-ai-slop-engineer/assets/logo_64.png")
    
    # Upscale 8x using NEAREST neighbor to preserve razor sharp pixels -> 512x512
    img_512 = img.resize((512, 512), Image.Resampling.NEAREST)
    img_512.save("/home/obito/zero-ai-slop-engineer/assets/logo.png")
    img_512.save("/home/obito/zero-ai-slop-engineer/logo.png")
    print("PNG logos generated successfully: 64x64 and 512x512")

    # Generate crisp SVG representation
    svg_lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" shape-rendering="crispEdges" width="512" height="512">'
    ]
    for y in range(H):
        for x in range(W):
            r, g, b, a = img.getpixel((x, y))
            if a > 0:
                hex_col = f"#{r:02x}{g:02x}{b:02x}"
                opacity = f' fill-opacity="{a/255.0:.2f}"' if a < 255 else ''
                svg_lines.append(f'  <rect x="{x}" y="{y}" width="1" height="1" fill="{hex_col}"{opacity}/>')
    svg_lines.append('</svg>')
    
    with open("/home/obito/zero-ai-slop-engineer/assets/logo.svg", "w") as f:
        f.write("\n".join(svg_lines))
    print("SVG logo generated successfully.")

if __name__ == "__main__":
    create_pixel_logo()
