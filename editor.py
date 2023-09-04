import os
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.simpledialog import askstring
from data import colors_for_background, colors_for_text, all_font_types, all_size_chars


def text_editor():
    global num

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

        remove_mark()
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

    def remove_mark():
        text_edit.tag_remove("find", 1.0, tk.END)

    def change_background_color():
        num_bg = bg_color_num.get()
        text_edit.config(background=colors_for_background[num_bg], fg=colors_for_text[num_bg])

    def change_font_type():
        font_num = font_color_num.get()
        text_edit.config(font=(all_font_types[font_num], all_size_chars[char], "normal"))

    def change_font_size():
        char = size_char.get()
        text_edit.config(font=(all_font_types[font_num], all_size_chars[char], "normal"))


    def delete_content():
        answer = messagebox.askquestion("Confirmation", "Аre you sure you want to delete all content?")

        if answer == "yes":
            text_edit.delete(1.0, tk.END)


    window = tk.Tk()
    window.title("Vesi's text editor")
    my_icon = tk.PhotoImage(file="C:\\Users\\USER\\Desktop\\v_logo.png")
    window.iconphoto(True, my_icon)

    char = "m"
    font_num = 0
    my_custom_font = (all_font_types[font_num], all_size_chars[char], "normal")
    text_edit = tk.Text(window, state="normal", background="LightCyan2", font=my_custom_font)
    frame = tk.Frame(window, relief=tk.RAISED, border=1)
    menu_bar = tk.Menu(window)
    search_menu = tk.Menu(menu_bar, tearoff=False)
    settings_menu = tk.Menu(menu_bar, tearoff=False)
    background_menu = tk.Menu(settings_menu, tearoff=False)
    type_menu = tk.Menu(settings_menu, tearoff=False)
    size_menu = tk.Menu(settings_menu, tearoff=False)

    window.config(menu=menu_bar)

    frame.grid(row=0, column=0, sticky="nsew")
    text_edit.grid(row=0, column=1, sticky="nsew")
    window.rowconfigure(0, weight=1, minsize=600)
    window.columnconfigure(1, weight=1, minsize=1000)

    menu_bar.add_command(label="Open", command=open_file)
    menu_bar.add_command(label="Save As", command=save_as_new_file)
    menu_bar.add_command(label="Save", command=save_file)

    menu_bar.add_cascade(label="Search text", menu=search_menu)
    search_menu.add_command(label="Find", command=find_text)
    search_menu.add_command(label="Remove mark", command=remove_mark)

    menu_bar.add_command(label="Delete", command=delete_content)

    menu_bar.add_cascade(label="Settings", menu=settings_menu)
    settings_menu.add_cascade(label="Background color", menu=background_menu)
    settings_menu.add_cascade(label="Font type", menu=type_menu)
    settings_menu.add_cascade(label="Font size", menu=size_menu)

    bg_color_num = tk.IntVar()
    bg_color_num.set(4)

    background_menu.add_radiobutton(label="Black", value=0, variable=bg_color_num, command=change_background_color)
    background_menu.add_radiobutton(label="Dark", value=1, variable=bg_color_num, command=change_background_color)
    background_menu.add_radiobutton(label="Light", value=2, variable=bg_color_num, command=change_background_color)
    background_menu.add_radiobutton(label="White", value=3, variable=bg_color_num, command=change_background_color)
    background_menu.add_radiobutton(label="Blue", value=4, variable=bg_color_num, command=change_background_color)
    background_menu.add_radiobutton(label="Green", value=5, variable=bg_color_num, command=change_background_color)

    font_color_num = tk.IntVar()
    font_color_num.set(0)
    type_menu.add_radiobutton(label="Arial", value=0, variable=font_color_num, command=change_font_type)
    type_menu.add_radiobutton(label="Gothic", value=1, variable=font_color_num, command=change_font_type)
    type_menu.add_radiobutton(label="Tahoma", value=2, variable=font_color_num, command=change_font_type)
    type_menu.add_radiobutton(label="Calibri", value=3, variable=font_color_num, command=change_font_type)
    type_menu.add_radiobutton(label="Verdana", value=4, variable=font_color_num, command=change_font_type)

    size_char = tk.StringVar()
    size_char.set("m")
    size_menu.add_radiobutton(label="Small", value="s", variable=size_char, command=change_font_size)
    size_menu.add_radiobutton(label="Medium", value="m", variable=size_char, command=change_font_size)
    size_menu.add_radiobutton(label="Large", value="l", variable=size_char, command=change_font_size)
    size_menu.add_radiobutton(label="Extra large", value="xl", variable=size_char, command=change_font_size)

    window.mainloop()


if __name__ == '__main__':
    filepath = None
    text_editor()


