import tkinter as tk
from tkinter import ttk, messagebox
import os
import subprocess
import sys


# Function to install missing packages
def install_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])


# Try to import the base64 module, install it if not present
try:
    import base64
except ImportError:
    install_package("base64")
    import base64


# Function to generate the password hash
def generate_password_hash():
    try:
        bits = int(bit_size_entry.get())
        if bits <= 0:
            messagebox.showerror("Error", "Please enter a positive integer.")
            return
        _bytes = ((bits + 7) // 8) ** 2
        password_hash = base64.b64encode(os.urandom(_bytes).decode())
        hash_output_label.config(text=password_hash.__str__())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter an integer.")


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

# Label to display the generated hash
hash_output_label = ttk.Label(root, text="")
hash_output_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Configure the grid
root.columnconfigure(1, weight=1)

# Start the application
root.mainloop()
