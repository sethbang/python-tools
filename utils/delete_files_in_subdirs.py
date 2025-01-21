import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def delete_files_in_subdirs():
    """
    "Loop through all subdirectories and files in the root directory and its subdirectories and delete
    all files."

    The first thing we do is create a tkinter window and hide it. We do this so that we can use
    tkinter's filedialog.askdirectory() function to display a folder selection dialog and get the
    selected folder

    Returns:
      A list of tuples. Each tuple contains the directory path, a list of subdirectories, and a list of
    files.
    """

    # Create a tkinter window and hide it
    root = tk.Tk()
    root.withdraw()

    # Use filedialog.askdirectory() to display a folder selection dialog and get the selected folder
    root_dir = filedialog.askdirectory(title="Select the Root Directory")

    # Show a confirmation dialog before deleting files
    confirm_msg = f"Are you sure you want to delete ALL files within {root_dir}?"
    if not messagebox.askyesno("Confirm Deletion", confirm_msg):
        return

    # Loop through all subdirectories and files in the root directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Loop through all files in the current directory
        for filename in filenames:
            # Create the full file path by joining the directory path and file name
            file_path = os.path.join(dirpath, filename)
            # Use os.remove to delete the file at the full file path
            os.remove(file_path)

# Call the function to run the script
# delete_files_in_subdirs()
