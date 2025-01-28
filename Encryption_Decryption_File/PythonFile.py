import os
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    if os.path.exists(KEY_FILE):
        return open(KEY_FILE, "rb").read()
    else:
        return generate_key()

def encrypt_file():
    key = load_key()
    fernet = Fernet(key)

    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    with open(file_path, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_path + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    messagebox.showinfo("Success", "File Encrypted Successfully!")

def decrypt_file():
    key = load_key()
    fernet = Fernet(key)

    file_path = filedialog.askopenfilename(filetypes=[("Encrypted Files", "*.enc")])
    if not file_path:
        return

    with open(file_path, "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    try:
        decrypted = fernet.decrypt(encrypted)
        original_path = file_path.replace(".enc", "")
        with open(original_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted)
        messagebox.showinfo("Success", "File Decrypted Successfully!")
    except:
        messagebox.showerror("Error", "Decryption Failed. Wrong Key or Corrupted File!")

# GUI Setup
root = tk.Tk()
root.title("File Encryption & Decryption")

tk.Label(root, text="File Encryption Tool", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="Encrypt File", command=encrypt_file).pack(pady=5)
tk.Button(root, text="Decrypt File", command=decrypt_file).pack(pady=5)

root.mainloop()
