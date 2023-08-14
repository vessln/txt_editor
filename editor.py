import os
import tkinter as tk
from tkinter.filedialog import askopenfilename


def text_editor():

    def open_file():

        filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if filepath:
            with open(filepath, "r") as new_file:
                text = new_file.read()
                text_edit.insert(tk.END, text)
                name_of_file = os.path.basename(filepath)
                window.title(f"Edit text in {name_of_file}")

    window = tk.Tk()
    window.title("Vesi's text editor")

    text_edit = tk.Text(window)
    frame = tk.Frame(window, relief=tk.RAISED, bd=0)
    menu_bar = tk.Menu(window)

    window.config(menu=menu_bar)

    frame.grid(row=0, column=0, sticky="nsew")
    text_edit.grid(row=0, column=1, sticky="nsew")
    window.rowconfigure(0,  weight=1, minsize=650)
    window.columnconfigure(1, weight=1, minsize=1000)

    menu_bar.add_command(label="Open", command=open_file)

    window.mainloop()


if __name__ == '__main__':
    text_editor()
