# d4inv2img

This is a utility for Diablo 4 that saves all items in your stash as images.

It uses mss for screen capture, OpenCV for detecting the item, and pyautogui for mouse movement.

# How to use
1. **Source**: Install requirements.txt & run main.py. **Precompiled Binary**: Unzip main.7z, run main.exe.
2. Hover over the first item in your stash and press 'F2' (default)
3. The script will go through each item and save the images to the "Inventory" subdirectory.

## Diablo 4 Settings
1. Font scale medium
2. Advanced Tooltips Enabled
3. Hud Centered
4. Colorblind off
5. Designed for fullscreen 1920x1080 monitor, but I've included a function to try to compensate for differing resolutions

## "Will this get me banned?"
- This program does not read the memory of the game. It does not click or otherwise interact with the game in any way other than moving the mouse across the screen. It uses computer vision to detect the items, and uses the `pyautogui` module to move the mouse.  Use at your own risk.

## Troubleshooting:
1. **Item not detected**: You can try altering the `min_width, max_width, min_height, max_height` parameters of crop_image() which are what determines the size of the item box it is looking for. My default values are designed to account for resolutions of up to 1920x1080, but bigger monitors may need to manually adjust this. Also, it's possible for the mouse movement to fail to highlight the item. I've added a 'jiggle' mechanic to mediate this, but you can try adjusting the duration of the mouse movements as well.
2. **Antivirus Note**: This program uses a keyboard hook to listen for "f2" and "f3" to start and stop the script, respectively. Some antivirus programs may warn you about this or require you to run the script with admin rights.
3. **Image not of item**: I tried to prevent erroneous item detection by using color thresholding to detect if the cell is empty, but this is unreliable by nature. If the image only partially contains the item box, try adjusting the parameters of crop_image and make sure your settings match what is listed above.
