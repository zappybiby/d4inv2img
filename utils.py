import os
import time
import random
import glob
import signal


def on_press(stop_key='f3'):
    def _on_press_inner(key):
        if key.name == str(stop_key):
            os.kill(os.getpid(), signal.SIGTERM)

    return _on_press_inner


def random_sleep():
    # Generate a random float number
    sleep_time = random.uniform(0.05, 0.1)
    time.sleep(sleep_time)


def delete_existing_pngs():
    # Get a list of all the PNG files in the 'Inventory' directory
    png_files = glob.glob('Inventory/*.png')

    # Iterate over the list of files and remove each one
    for png_file in png_files:
        try:
            os.remove(png_file)
        except OSError:
            print(f'Error deleting {png_file}')
