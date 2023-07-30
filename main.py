import keyboard
import pyautogui
from mouse import starting_coords, move_right, move_down, calculate_movement_auto
from screen_grab import crop_item, is_cell_empty

from utils import on_press, delete_existing_pngs


def main():
    print("Press F2 to start script...")
    # Wait indefinitely for the F2 key to be pressed
    keyboard.wait('F2')
    # Press 'F3' to stop the script
    keyboard.on_press(callback=on_press('f3'))
    delete_existing_pngs()
    init_coords = starting_coords()
    item_number = 1
    right_px, down_px = calculate_movement_auto()

    for row in range(3):  # 3 rows
        for col in range(11):  # 11 columns

            # Step 2: Check if the grid cell has an item
            if is_cell_empty() == 0:
                # If it's not empty, run test_function() and increment item_number
                crop_item(280, 450, 300, 900, item_number)
                item_number += 1

            # If this is not the last column in the row, move right
            if col != 10:
                move_right(right_px)

        # After going through each cell in a row, return to initial coordinates
        pyautogui.moveTo(init_coords.x, init_coords.y, 0.5)  # Move back to initial coords

        # If this is not the last row, move down once / twice
        if row != 2:
            for i in range(row + 1):
                move_down(down_px)

    # We have now gone through all 33 cells, the script is finished
    print(f"Total non-empty items: {item_number - 1}")


if __name__ == "__main__":
    main()
