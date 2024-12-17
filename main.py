import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import random


class ListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ListsX - List Manager")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        try:
            self.root.iconbitmap("assets/listsX.ico")
        except Exception as e:
            print("Icon not found. Using default icon.")

        # Apply futuristic theme styles
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure(
            "TButton",
            background="#222831",
            foreground="#eeeeee",
            font=("Helvetica", 12, "bold"),
            padding=10,
        )
        self.style.map("TButton", background=[("active", "#393e46")])
        self.style.configure(
            "TLabel",
            background="#222831",
            foreground="#eeeeee",
            font=("Helvetica", 14),
        )
        self.root.configure(bg="#222831")

        # Initialize file paths
        self.list_to_clear_path = None
        self.base_list_path = None
        self.selected_list_path = None

        # Initialize Main Menu
        self.main_menu_ui()

    def clear_ui(self):
        """Clears all widgets from the current UI."""
        for widget in self.root.winfo_children():
            widget.destroy()
        self.copyrights()

    def display_image(self, image_path):
        """Load and display an image in the GUI."""
        try:
            # Load the image using Pillow
            image = Image.open(image_path)
            image = image.resize((150, 150), Image.Resampling.LANCZOS)  # Resize the image
            photo = ImageTk.PhotoImage(image)

            # Add the image to a label
            label = tk.Label(self.root, image=photo, bg="#222831")
            label.image = photo  # Keep a reference to avoid garbage collection
            label.pack(pady=10)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load image: {e}")

    def copyrights(self):
        copyright_label = ttk.Label(self.root, text="Copyrights © 2024 UD", anchor="center", font=("Helvetica", 9))
        copyright_label.pack(side="bottom", fill="x", pady=10)


    def main_menu_ui(self):
        """Main Menu UI."""
        self.clear_ui()

        self.display_image("assets/listsX.png")
        ttk.Label(self.root, text="-- Main Menu --", anchor="center").pack(pady=20)

        ttk.Button(self.root, text="List Cleaner", command=self.list_cleaner_ui).pack(pady=10)
        ttk.Button(self.root, text="Actions", command=self.actions_ui).pack(pady=10)
        ttk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=20)

    def list_cleaner_ui(self):
        """List Cleaner UI."""
        self.clear_ui()

        self.display_image("assets/clean.png")
        ttk.Label(self.root, text="-- List Cleaner --", anchor="center").pack(pady=20)

        ttk.Button(self.root, text="Select List To Clear", width=20, command=self.select_list_to_clear).pack(pady=10)
        ttk.Button(self.root, text="Select The Base List", width=20, command=self.select_base_list).pack(pady=10)
        ttk.Button(self.root, text="Process", command=self.process_lists).pack(pady=20)

        ttk.Button(self.root, text="Back", command=self.main_menu_ui).pack(pady=20)

    def actions_ui(self):
        self.clear_ui()
        self.display_image("assets/actions.png")
        ttk.Label(self.root, text="-- Actions --", anchor="center").pack(pady=20)
        ttk.Button(self.root, text="Select List", width=31, command=self.select_list).pack(pady=10)

        actions_frame = tk.Frame(self.root, bg="#222831")
        actions_frame.pack(pady=10)

        ttk.Button(actions_frame, text="Shuffle", width=13 , command=self.shuffle_list).grid(row=1, column=0, padx=10, pady=10)
        ttk.Button(actions_frame, text="Sort", width=13 ,command=self.sort_list).grid(row=1, column=1, padx=10, pady=10)
        ttk.Button(actions_frame, text="Reverse", width=13 ,command=self.reverse_list).grid(row=2, column=0, padx=10, pady=10)
        ttk.Button(actions_frame, text="RV Duplicates", width=13 ,command=self.remove_duplicates).grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(self.root, text="Back", command=self.main_menu_ui).pack(pady=20)

    def select_list_to_clear(self):
        """Select the 'List to Clear' file."""
        self.list_to_clear_path = filedialog.askopenfilename(title="Select List to Clear (TXT)", filetypes=[("Text Files", "*.txt")])
        if self.list_to_clear_path:
            messagebox.showinfo("File Selected", f"List to Clear file selected:\n{self.list_to_clear_path}")
        else:
            messagebox.showwarning("No File Selected", "Please select a valid file for 'List to Clear'.")

    def select_base_list(self):
        """Select the 'Base List' file."""
        self.base_list_path = filedialog.askopenfilename(title="Select Base List (TXT)", filetypes=[("Text Files", "*.txt")])
        if self.base_list_path:
            messagebox.showinfo("File Selected", f"Base List file selected:\n{self.base_list_path}")
        else:
            messagebox.showwarning("No File Selected", "Please select a valid file for 'Base List'.")

    def process_lists(self):
        """Process the lists and create the cleaned output file."""
        try:
            if not self.list_to_clear_path or not self.base_list_path:
                raise ValueError("Both files must be selected before processing.")

            # Read files
            with open(self.list_to_clear_path, 'r') as file1:
                list_to_clear = set(line.strip() for line in file1)

            with open(self.base_list_path, 'r') as file2:
                base_list = set(line.strip() for line in file2)

            # Remove items from List to Clear that are in Base List
            clear_list = list_to_clear - base_list

            # Ask user to select save path
            output_file = filedialog.asksaveasfilename(
                title="Save Cleaned List As",
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt")],
            )
            if not output_file:
                return  # User cancelled save dialog

            # Write the results
            with open(output_file, 'w') as output:
                output.write("\n".join(sorted(clear_list)))

            messagebox.showinfo("Success", f"File saved as:\n{output_file}")

        except Exception as e:
            messagebox.showerror("Error", str(e))


    def select_list(self):
        self.selected_list_path = filedialog.askopenfilename(title="Select List (TXT)", filetypes=[("Text Files", "*.txt")])
        if self.selected_list_path:
            messagebox.showinfo("File Selected", f"List file selected:\n{self.selected_list_path}")
        else:
            messagebox.showwarning("No File Selected", "Please select a valid file.")

    def shuffle_list(self):
        self.modify_list("shuffle")

    def sort_list(self):
        self.modify_list("sort")

    def reverse_list(self):
        self.modify_list("reverse")

    def remove_duplicates(self):
        self.modify_list("remove_duplicates")

    def modify_list(self, action):
        try:
            if not self.selected_list_path:
                raise ValueError("Please select a list before performing any actions.")

            with open(self.selected_list_path, 'r') as file:
                items = [line.strip() for line in file]

            if not items:
                raise ValueError("The selected list is empty.")

            if action == "shuffle":
                random.shuffle(items)
            elif action == "sort":
                items.sort()
            elif action == "reverse":
                items.reverse()
            elif action == "remove_duplicates":
                items = list(dict.fromkeys(items))

            output_file = filedialog.asksaveasfilename(
                title="Save Modified List As", 
                defaultextension=".txt", 
                filetypes=[("Text Files", "*.txt")]
            )
            if not output_file:
                return

            with open(output_file, 'w') as output:
                output.write("\n".join(items))

            messagebox.showinfo("Success", f"File saved as:\n{output_file}")

        except Exception as e:
            messagebox.showerror("Error", str(e))



if __name__ == "__main__":
    root = tk.Tk()
    app = ListApp(root)
    root.mainloop()
