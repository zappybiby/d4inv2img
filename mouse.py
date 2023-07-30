import time
import cv2
import pyautogui
import numpy as np


def starting_coords():
    return pyautogui.position()


def calculate_movement_auto():
    """
    Calculate the mouse movement needed for the current screen resolution,
    using the 1920x1080 resolution as the base.

    Returns:
    tuple: The calculated mouse movements as a tuple of (right, down).
    """
    # Get current screen resolution
    resolution = pyautogui.size()

    base_right = 55
    base_down = 80
    base_resolution = (1920, 1080)

    width, height = resolution
    right_movement = width * (base_right / base_resolution[0])
    down_movement = height * (base_down / base_resolution[1])

    return round(right_movement), round(down_movement)  # Round the values to get whole pixel numbers


def get_mouse_color():
    x, y = pyautogui.position()
    r, g, b = pyautogui.pixel(x, y)

    # OpenCV uses BGR color format, so we need to reverse the order of RGB to BGR
    bgr_pixel_color = (b, g, r)

    # Convert the BGR color into an array format
    bgr_pixel_color = np.uint8([[bgr_pixel_color]])

    # Convert the BGR color to HSV color
    hsv_pixel_color = cv2.cvtColor(bgr_pixel_color, cv2.COLOR_BGR2HSV)

    return hsv_pixel_color[0][0]


def move_right(mouse_right_px):
    x, y = pyautogui.position()
    x = x + mouse_right_px  # add to the x coordinate
    pyautogui.moveTo(x, y, 0.2, pyautogui.easeInElastic)
    jiggle_mouse()


def move_down(mouse_down_px):
    x, y = pyautogui.position()
    y = y + mouse_down_px  # add to the y coordinate
    pyautogui.moveTo(x, y, 0.2, pyautogui.easeInElastic)  # move mouse
    jiggle_mouse()


def jiggle_mouse():
    # Get the current position of the mouse
    original_position = pyautogui.position()

    pyautogui.move(-2, 0, 0.1)
    time.sleep(0.05)
    pyautogui.move(3, 0, 0.1)
    time.sleep(0.05)

    pyautogui.moveTo(original_position)
