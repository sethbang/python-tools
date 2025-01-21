import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from file_utilities import *


def prefix_rename(ps, top_window):
    """
    It takes a string as an argument, uses that string to rename all files in a selected directory, and
    then closes the window.

    Args:
      ps: The prefix string that the user entered in the entry box.
      top_window: The window that we want to close.

    Returns:
      None
    """

    # Assigning the value of the variable `ps` to the variable `prefix_string`.
    prefix_string = ps

    # Use filedialog.askdirectory() to display a folder selection dialog and get the selected folder
    root_dir = get_root_dir()

    # Show a confirmation dialog before deleting files
    confirm_msg = f"Are you sure you want to rename ALL files within {root_dir}?"
    if not messagebox.askyesno("Confirm Selection", confirm_msg):
        return

    # Loop through all subdirectories and files in the root directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Loop through all files in the current directory
        for filename in filenames:
            # Create the full file path by joining the directory path and file name
            file_path = os.path.join(dirpath, filename)
            # Use os.remove to delete the file at the full file path
            os.rename(file_path, os.path.join(
                dirpath, (prefix_string + filename)))

    # Showing a message box with the title "Prefix" and the message "Prefix has been applied to
    # files!"
    messagebox.showinfo("Prefix", "Prefix has been applied to files!")

    # Closing the window.
    top_window.destroy()
