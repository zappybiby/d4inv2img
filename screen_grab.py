import os
import cv2
from mouse import get_mouse_color
import mss
import numpy as np


def grab_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # 1 = First Monitor
        screenshot = sct.grab(monitor)

        # Convert the data to a numpy array and make it OpenCV-compatible
        img = np.array(screenshot)[:, :, 0:3]  # discard alpha channel (if any)
        img_bgr = img[:, :, ::-1]  # convert from RGB to BGR
        return img_bgr


def crop_screen():
    img = grab_screen()
    height, width, channels = img.shape

    # We are cropping the left third part of the image out
    new_width = int(width * 2 / 3)

    # In OpenCV, the image array is accessed as [y: y + h, x: x + w]
    cropped_img = img[:, width - new_width:]
    return cropped_img


def crop_item(min_width, max_width, min_height, max_height, item_number):
    img = crop_screen()
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray, 5, 75, 75)

    # Apply Canny edge detection
    edges = cv2.Canny(blur, 15, 255)

    # Find contours in the edged image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Ensure the "Inventory" directory exists
    if not os.path.exists("Inventory"):
        os.makedirs("Inventory")

    # Iterate over the contours
    for contour in contours:
        # Compute the bounding box for the contour
        x, y, w, h = cv2.boundingRect(contour)

        # If the rectangle meets the size criteria, save the cropped image
        if min_width <= w <= max_width and min_height <= h <= max_height:
            roi = rgb[y:y + h, x:x + w]
            cv2.imwrite(f'Inventory/Item_{item_number}.png', roi)
            print(f'Successfully Saved Item {item_number}')


def is_cell_empty():
    hsv = get_mouse_color()
    # empty cell color
    lower_range = np.array([0, 0, 0])
    upper_range = np.array([179, 150, 17])

    if np.all((hsv >= lower_range) & (hsv <= upper_range)):
        return 1
    else:
        return 0
