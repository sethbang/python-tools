import os
import tkinter as tk
from tkinter import filedialog


def get_file_list(the_folder):
    """
    > It takes a folder name as input, and returns a dictionary with two keys: "files" and "count". The
    "files" key contains a list of the files in the folder, and the "count" key contains the number of
    files in the folder

    Args:
      the_folder: The folder to get the file list from.

    Returns:
      A dictionary with two keys: files and count.
    """

    the_files = os.listdir(os.path.abspath(the_folder))

    return {"files": the_files, "count": len(the_files)}


def get_root_dir():
    """
    It opens a file dialog box and returns the path of the directory selected by the user

    Returns:
      The root directory path
    """

    root_path = filedialog.askdirectory(title="Select the Directory")

    return root_path


def get_file_path():
    """
    It opens a file dialog box and returns the path of the file selected by the user

    Returns:
      The file path of the file that the user selected.
    """

    file_path = filedialog.askopenfilename(title="Select the File")

    return file_path


def get_file_paths():
    """
    It opens a file dialog box and allows the user to select multiple files

    Returns:
      A tuple of file paths
    """

    file_paths = filedialog.askopenfilenames(title="Select the Files")

    return file_paths


# def get_file_type(file):
