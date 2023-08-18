import os
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename


def text_editor():

    def open_file():

        answer = messagebox.askretrycancel("Warning",
                        "When you open other file, if there is any content in current file, it will be deleted.")
        if answer:
            text_edit.delete(1.0, tk.END)

            filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

            if filepath:
                with open(filepath, "r") as new_file:
                    text = new_file.read()
                    text_edit.insert(tk.END, text)
                    name_of_file = os.path.basename(filepath)
                    window.title(f"Edit text in {name_of_file}")

    def save_as_new_file():
        content = text_edit.get(1.0, tk.END)

        if content.strip() == "":
            messagebox.showerror("Error", "There is no content!")

        else:

            filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

            if filepath:
                with open(filepath, 'w') as saved_file:
                    text = text_edit.get(1.0, tk.END)
                    saved_file.write(text)
                    name_of_file = os.path.basename(filepath)

                window.title(f"{name_of_file} edited with Vesi\'s editor")

    def delete_content():

        answer = messagebox.askquestion("Confirmation", "Аre you sure you want to delete all content?")

        if answer == "yes":
            text_edit.delete(1.0, tk.END)

    window = tk.Tk()
    window.title("Vesi's text editor")

    text_edit = tk.Text(window, state="normal", background="lightcyan", font=("Arial", 12))
    frame = tk.Frame(window, relief=tk.RAISED, bd=0)
    menu_bar = tk.Menu(window)

    window.config(menu=menu_bar)

    frame.grid(row=0, column=0, sticky="nsew")
    text_edit.grid(row=0, column=1, sticky="nsew")
    window.rowconfigure(0,  weight=1, minsize=650)
    window.columnconfigure(1, weight=1, minsize=1000)

    menu_bar.add_command(label="Open", command=open_file)
    menu_bar.add_command(label="Save As", command=save_as_new_file)
    menu_bar.add_command(label="Delete", command=delete_content)

    window.mainloop()


if __name__ == '__main__':
    text_editor()

