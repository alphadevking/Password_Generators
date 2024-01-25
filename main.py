import tkinter as tk
from tkinter import ttk, messagebox
import os
import base64
import pyperclip


# Function to generate the password hash
def generate_password_hash():
    try:
        bits = int(bit_size_entry.get())
        if bits <= 0:
            messagebox.showerror("Error", "Please enter a positive integer.")
            return
        hash_bytes = (bits + 7) // 8
        password_hash = base64.b64encode(os.urandom(hash_bytes)).decode()
        hash_output_text.config(state=tk.NORMAL)
        hash_output_text.delete('1.0', tk.END)
        hash_output_text.insert(tk.END, password_hash)
        hash_output_text.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter an integer.")


# Function to copy the hash to the clipboard
def copy_to_clipboard():
    hash_text = hash_output_text.get('1.0', tk.END).strip()
    if hash_text:
        pyperclip.copy(hash_text)
        copied_label.config(text="Copied!")
        # Clear the copied message after 1500 milliseconds (1.5 seconds)
        root.after(1500, lambda: copied_label.config(text=""))


# Create the main window
root = tk.Tk()
root.title("Password Hash Generator")

# Create and place the label and entry widget for the bit size
bit_size_label = ttk.Label(root, text="Bit Size for Password Hash:")
bit_size_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

bit_size_entry = ttk.Entry(root)
bit_size_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Generate button
generate_button = ttk.Button(root, text="Generate Hash", command=generate_password_hash)
generate_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")

# Text widget to display the generated hash with wrapping
hash_output_text = tk.Text(root, height=4, width=50, wrap=tk.WORD, state=tk.DISABLED)
hash_output_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Copy button
copy_button = ttk.Button(root, text="Copy Hash", command=copy_to_clipboard)
copy_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")

# Label to display the copied message
copied_label = ttk.Label(root, text="")
copied_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Configure the grid
root.columnconfigure(1, weight=1)

# Start the application
root.mainloop()
