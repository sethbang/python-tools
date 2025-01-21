from serpapi import GoogleSearch
import urllib.request
import os
import tkinter as tk
from tkinter import filedialog
import json

params = {
    "device": "desktop",
    "engine": "google",
    "ijn": "0",
    "q": "kimmy granger doggy",
    "google_domain": "google.com",
    "tbs": "itp:photos,isz:l",
    "tbm": "isch",
    "api_key": "cc3289041209831de5a1f62504d77ca6c8a626108c0955af877859df8481fb4a"
}

# Create a Tkinter root window
root = tk.Tk()

# Hide the root window
root.withdraw()

save_path = filedialog.askdirectory()

print(save_path)

search = GoogleSearch(params)
results = search.get_dict()

for res in results["images_results"]:
    try:
        urllib.request.urlretrieve(res["original"], f"{save_path}/{res['position']}_kgd.jpg")
        print(f"{res['position']} Success")
    except:
        print(f"{res['position']} Fail")


with open(f"{save_path}/results.txt", "a") as file:
    for x in results["images_results"]:

        for key, value in x.items():
            file.write('%s:%s\n' % (key, value))
        file.write("\n*****************************\n")
