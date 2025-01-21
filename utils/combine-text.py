import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

# prompt the user to select the directory containing the txt files
Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
directory = askdirectory()  # show an "Open" dialog box and return the path to the selected directory

# the name of the combined txt file
combined_txt_file = 'combined.txt'

# create an empty list to store the contents of the individual txt files
contents = []

# iterate through the files in the directory
for filename in os.listdir(directory):
  # only process txt files
  if filename.endswith('.txt'):
    # open the txt file and read its contents
    with open(os.path.join(directory, filename), 'r') as f:
      contents.append(f.read())

# combine the contents of the txt files into a single string
combined_contents = '\n\n\n\n\n\n\n\n'.join(contents)

# write the combined contents to the combined txt file
with open(os.path.join(directory, combined_txt_file), 'w') as f:
  f.write(combined_contents)
