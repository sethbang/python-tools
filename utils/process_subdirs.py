import os
import tkinter as tk
from tkinter import filedialog
from file_rename import find_and_rename_largest_file


def process_subdirectories(directory, func):
    for subdir, dirs, files in os.walk(directory):
        if subdir != directory:  # Exclude the root directory
            func(subdir)


def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    selected_directory = filedialog.askdirectory(title="Select a directory")
    if selected_directory:
        process_subdirectories(
            selected_directory, find_and_rename_largest_file)
    else:
        print("No directory selected.")


if __name__ == "__main__":
    main()
