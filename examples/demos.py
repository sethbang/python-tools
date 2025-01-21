import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from delete_files_in_subdirs import delete_files_in_subdirs
from prefix_rename import prefix_rename


colors = {
    "TEAL": "#2596be",
    "PURPLE": "#6c25be",
    "GOLD": "#bea925",
    "IRON": "#D8D9DA",
    "BOULDER": "#7D7D7D"
}


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # setting the title of the main window
        self.title("Demos")
        # set the size and position of the window
        self.geometry("300x600+650+250")
        # disabling the resizable option
        self.resizable(0, 0)
        # setting the background color to #D8E9E6
        self.configure(bg=colors["PURPLE"])

        self.header_frame = tk.Frame(self, bg=colors["PURPLE"],
                                     borderwidth=3, relief="solid")
        self.buttons_frame = tk.Frame(
            self, bg=colors["PURPLE"], borderwidth=3, relief="solid")

        # using the pack() method to place the frames in the window
        self.header_frame.pack(fill="both")
        self.buttons_frame.pack(expand=True, fill="both")

        # creating a label using the Label() widget
        self.header_label = tk.Label(
            self.header_frame,
            text="Script Demos",
            font=("arial bold", "36"),
            fg=colors["IRON"],
            bg=colors["TEAL"],
            borderwidth=6,
            relief="solid"
        )

        # using the pack() method to place the label in the window
        self.header_label.pack(expand=True, fill="both", pady=8,
                               padx=8, ipady=10)

        # Button that calls the delete_files_in_subdirs() function
        self.del_in_subdirs_button = tk.Button(
            self.buttons_frame,
            text="Delete All Files in Subdirs",
            font=("arial bold", "18"),
            bg=colors["IRON"],
            fg=colors["TEAL"],
            activeforeground=colors["PURPLE"],
            relief="groove",
            command=delete_files_in_subdirs
        )

        self.del_in_subdirs_button.pack(pady=10)

        # Button that calls the delete_files_in_subdirs() function
        self.prefix_button = tk.Button(
            self.buttons_frame,
            text="Prefix all Files in Directory",
            font=("arial bold", "18"),
            bg=colors["IRON"],
            fg=colors["TEAL"],
            activeforeground=colors["PURPLE"],
            relief="groove",
            command=self.open_prefix_window
        )

        self.prefix_button.pack(pady=10)

    def open_prefix_window(self):
        pre_win = tk.Toplevel()
        string_var = tk.StringVar()

        pre_win.title("Set Prefix String")

        pre_label = tk.Label(pre_win, text="Enter a prefix string:")
        pre_label.grid(column=0, row=0)

        pre_entry = tk.Entry(pre_win, textvariable=string_var)
        pre_entry.grid(column=0, row=1)

        pre_button = tk.Button(
            pre_win,
            text="Set Prefix String and Pick Dir",
            command=lambda: prefix_rename(string_var.get(), pre_win)
        )

        pre_button.grid(column=0, row=2)

        pre_win.mainloop()


if __name__ == "__main__":
    app = App()
    app.mainloop()
