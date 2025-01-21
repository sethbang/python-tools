import os
import tkinter as tk
from tkinter import filedialog


def find_and_rename_largest_file(directory):
    """
    It iterates through the files in a directory, finds the largest file, and renames it to the name of
    the directory

    Args:
      directory: The directory to search for files.
    """
    largest_file = None
    largest_file_size = 0

    # Iterate through the files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Check if the current file is a regular file (not a directory)
        if os.path.isfile(filepath):
            file_size = os.path.getsize(filepath)

            # Update largest_file and largest_file_size if a larger file is found
            if file_size > largest_file_size:
                largest_file = filepath
                largest_file_size = file_size

    if largest_file:
        # Get the parent directory name
        parent_directory = os.path.basename(directory)

        # Create the new file name and path
        new_filename = f"{parent_directory}{os.path.splitext(largest_file)[1]}"
        new_filepath = os.path.join(directory, new_filename)

        # Rename the largest file
        os.rename(largest_file, new_filepath)
        print(f"Renamed '{largest_file}' to '{new_filepath}'")
    else:
        print("No files found in the directory.")


def main():
    # Create a Tkinter root window (it won't be displayed)
    root = tk.Tk()
    root.withdraw()

    # Open a file dialog window to select the directory
    directory_path = filedialog.askdirectory(title="Select a directory")

    if directory_path:
        find_and_rename_largest_file(directory_path)
    else:
        print("No directory selected.")


if __name__ == "__main__":
    main()
