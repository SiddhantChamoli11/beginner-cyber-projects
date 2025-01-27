import os
import json
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

HASH_FILE = "file_hashes.json"


# Save hashes to file
def save_hashes(hashes):
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)


# Calculate hash of a file
def calculate_hash(filepath, algorithm="sha256"):
    try:
        hash_func = getattr(hashlib, algorithm)()
        with open(filepath, "rb") as f:
            chunk = f.read(8192)
            while chunk:
                hash_func.update(chunk)
                chunk = f.read(8192)
        return hash_func.hexdigest()
    except FileNotFoundError:
        return None


# Add file to the hash database
def add_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        hash_value = calculate_hash(filepath)
        if hash_value:
            hashes[filepath] = hash_value
            save_hashes(hashes)
            listbox.insert(tk.END, filepath)


# Check file integrity
def check_integrity():
    filepath = filedialog.askopenfilename()
    if filepath:
        hash_value = calculate_hash(filepath)
        if hash_value:
            if filepath in hashes:
                if hashes[filepath] == hash_value:
                    messagebox.showinfo("Integrity Check", "File is unchanged and verified!")
                else:
                    messagebox.showerror("Integrity Check", "File integrity check failed!")
            else:
                messagebox.showwarning("Integrity Check", "File not found in hash database!")
        else:
            messagebox.showerror("Integrity Check", "Could not calculate hash of the selected file!")


# GUI Setup
window = tk.Tk()
window.title("File Integrity Checker")
window.geometry("500x400")

hashes = {}
if os.path.exists(HASH_FILE):
    with open(HASH_FILE, "r") as f:
        hashes = json.load(f)

frame = tk.Frame(window)
frame.pack(pady=20)

add_button = tk.Button(frame, text="Add File", command=add_file)
add_button.pack(side=tk.LEFT, padx=10)

check_button = tk.Button(frame, text="Check Integrity", command=check_integrity)
check_button.pack(side=tk.LEFT, padx=10)

listbox = tk.Listbox(window, width=60, height=15)
listbox.pack(pady=10)

for filepath in hashes.keys():
    listbox.insert(tk.END, filepath)

window.mainloop()
