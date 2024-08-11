import random
import os

randomWallpaper = random.randint(0, 3)

wallpapers = [
    [0, "~/wallpapers/gruvbox.png"],
    [1, "~/wallpapers/gruvbox2.jpg"],
    [2, "~/wallpapers/gruvbox3.png"],
    [3, "~/wallpapers/gruvbox4.png"]
]

currentWallpaper = wallpapers[randomWallpaper][1]
expandedWallpaperPath = os.path.expanduser(currentWallpaper)

script = f"""preload = {expandedWallpaperPath}

wallpaper=eDP-1,{expandedWallpaperPath}
"""

configPath = os.path.expanduser("~/.config/hypr/hyprpaper.conf")
with open(configPath, "w") as hyprpaper:
    hyprpaper.write(script)