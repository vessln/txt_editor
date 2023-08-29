import os
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.simpledialog import askstring


def text_editor():

    def open_file():
        global filepath

        answer = messagebox.askquestion("Delete", "Do you want to delete all content in current file?")
        if answer == "yes":
            text_edit.delete(1.0, tk.END)

        filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if filepath:
            with open(filepath, "r") as new_file:
                text = new_file.read()
                text_edit.insert(tk.END, text)
                name_of_file = os.path.basename(filepath)
                window.title(f"Edit text in {name_of_file}")

    def save_as_new_file():
        global filepath

        content = text_edit.get(1.0, tk.END)

        if content.strip() == "":
            messagebox.showerror("Error", "Empty file!")

        else:
            filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

            if filepath:
                with open(filepath, "w") as saved_file:
                    text = text_edit.get(1.0, tk.END)
                    saved_file.write(text)
                    name_of_file = os.path.basename(filepath)

                window.title(f"{name_of_file} edited with Vesi\'s editor")

    def save_file():
        global filepath
        content = text_edit.get(1.0, tk.END)

        if content.strip() == "":
            messagebox.showerror("Error", "Empty file!")

        else:
            if filepath:
                with open(filepath, "w") as saved_file:
                    text = text_edit.get(1.0, tk.END)
                    saved_file.write(text)
                    messagebox.showinfo("Info", "The file was saved.")
            else:
                save_as_new_file()

    def find_text():

        searching_text = askstring("Find", "Enter search text:")

        text_edit.tag_remove("find", 1.0, tk.END)
        index = 1.0

        while True:
            index = text_edit.search(searching_text, index, nocase=1, stopindex=tk.END)

            if not index:
                break

            last_index = "%s+%dc" % (index, len(searching_text))
            text_edit.tag_add("find", index, last_index)
            index = last_index

        if searching_text.lower() not in text_edit.get(1.0, tk.END).lower():
            messagebox.showerror("Error", "Nothing found!")

        else:
            text_edit.tag_config("find", foreground="red")

    def delete_content():

        answer = messagebox.askquestion("Confirmation", "Аre you sure you want to delete all content?")

        if answer == "yes":
            text_edit.delete(1.0, tk.END)


    window = tk.Tk()
    window.title("Vesi's text editor")

    text_edit = tk.Text(window, state="normal", background="LightCyan2", font=("Arial", 12))
    frame = tk.Frame(window, relief=tk.RAISED, border=0)
    menu_bar = tk.Menu(window)

    window.config(menu=menu_bar)

    frame.grid(row=0, column=0, sticky="nsew")
    text_edit.grid(row=0, column=1, sticky="nsew")
    window.rowconfigure(0, weight=1, minsize=600)
    window.columnconfigure(1, weight=1, minsize=1000)

    menu_bar.add_command(label="Open", command=open_file)
    menu_bar.add_command(label="Save As", command=save_as_new_file)
    menu_bar.add_command(label="Save", command=save_file)
    menu_bar.add_command(label="Find", command=find_text)
    menu_bar.add_command(label="Delete", command=delete_content)

    window.mainloop()


if __name__ == '__main__':
    filepath = None
    text_editor()

