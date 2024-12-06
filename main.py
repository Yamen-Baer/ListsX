import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk

class ClearListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ListsX - List Cleaner")
        self.root.geometry("400x300")
        self.root.resizable(False, False)  # Disable resizing
        self.root.iconbitmap("listsX.ico")

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

        # UI Components
        ttk.Label(self.root, text="List Cleaner", anchor="center").pack(pady=20)

        ttk.Button(root, text="Select List To Clear", command=self.select_list_to_clear).pack(pady=10)
        ttk.Button(root, text="Select The Base List", command=self.select_base_list).pack(pady=10)
        ttk.Button(root, text="Process", command=self.process_lists).pack(pady=20)

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

            # Write the results to Clear_List.txt
            output_file = "Clear_List.txt"
            with open(output_file, 'w') as output:
                output.write("\n".join(sorted(clear_list)))

            messagebox.showinfo("Success", f"Clear_List.txt has been created successfully!")

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = ClearListApp(root)
    root.mainloop()
