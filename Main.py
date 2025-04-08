import keyboard
import os
import time
from datetime import datetime
from PIL import ImageGrab
from pathlib import Path

PathFolder = Path.home() / "Pictures" / "Screenshots"
PathFolder.mkdir(parents=True, exist_ok=True)

# [AltScreen] 2025-04-08 (3).png
def getNextFileName():
    ToDay = datetime.now().strftime("%Y-%m-%d")
    Perfix = f"[AltScreen] {ToDay}"
    Counter = []
    for file in PathFolder.iterdir():
        if file.is_file() and file.name.startswith(Perfix) and file.suffix.lower() == ".png":
            try:
                number_part = file.stem.split("(")[-1].split(")")[0]
                number = int(number_part)
                Counter.append(number)
            except:
                pass
    NextNumber = max(Counter, default=0) + 1
    FileName = f"{Perfix} ({NextNumber}).png"
    

    print(FileName)
    return PathFolder / FileName



while True:
    if keyboard.is_pressed('alt') and keyboard.is_pressed('print screen'):
        time.sleep(0.2)

        Image = ImageGrab.grabclipboard()
        if isinstance(Image, ImageGrab.Image.Image):
            ImagePath = getNextFileName()
            Image.save(ImagePath)
            print(f"✅ Saved: {ImagePath}")
        else:
            print("⚠️ No image found in clipboard. Try again.")

        # Prevent duplicate captures on single press
        while keyboard.is_pressed('print screen'):
            time.sleep(0.1)
