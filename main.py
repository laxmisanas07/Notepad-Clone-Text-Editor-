import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("ProPad - Python Text Editor")
        self.root.geometry("800x600")

        # --- Text Area & Scrollbar ---
        # Text widget jahan hum likhenge
        self.text_area = tk.Text(self.root, font=("Arial", 12), undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        # Scrollbar
        scrollbar = tk.Scrollbar(self.text_area)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_area.yview)

        # --- Menu Bar ---
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # 1. File Menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open...", command=self.open_file)
        file_menu.add_command(label="Save As...", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        # 2. Edit Menu
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=lambda: self.root.focus_get().event_generate('<<Cut>>'))
        edit_menu.add_command(label="Copy", command=lambda: self.root.focus_get().event_generate('<<Copy>>'))
        edit_menu.add_command(label="Paste", command=lambda: self.root.focus_get().event_generate('<<Paste>>'))

        # 3. Help Menu
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    # --- Functions ---
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.root.title("New File - ProPad")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.root.title(f"{file_path} - ProPad")
            self.text_area.delete(1.0, tk.END)
            with open(file_path, "r") as file:
                self.text_area.insert(1.0, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(initialfile="Untitled.txt",
                                                 defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"{file_path} - ProPad")

    def show_about(self):
        messagebox.showinfo("About ProPad", "ProPad - A Simple Text Editor\nBuilt with Python & Tkinter\nBy Laxmi Sanas")

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()