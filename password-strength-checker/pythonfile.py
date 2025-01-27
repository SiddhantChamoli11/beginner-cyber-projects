import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    """
    Function to check the strength of a given password.
    :param password: str
    :return: str (password strength)
    """
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        strength += 2
        feedback.append("Length is strong (12+ characters).")
    elif len(password) >= 8:
        strength += 1
        feedback.append("Length is moderate (8-11 characters).")
    else:
        feedback.append("Password is too short (<8 characters).")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
        feedback.append("Contains uppercase letters.")
    else:
        feedback.append("No uppercase letters.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
        feedback.append("Contains lowercase letters.")
    else:
        feedback.append("No lowercase letters.")

    # Check for digits
    if re.search(r'\d', password):
        strength += 1
        feedback.append("Contains numbers.")
    else:
        feedback.append("No numbers.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
        feedback.append("Contains special characters.")
    else:
        feedback.append("No special characters.")

    # Determine strength level
    if strength >= 5:
        feedback.append("Overall strength: Strong")
    elif 3 <= strength < 5:
        feedback.append("Overall strength: Moderate")
    else:
        feedback.append("Overall strength: Weak")

    return "\n".join(feedback)

def evaluate_password():
    password = entry_password.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return
    result = check_password_strength(password)
    messagebox.showinfo("Password Strength Analysis", result)

# Create the main GUI window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

# Add widgets
label_title = tk.Label(root, text="Password Strength Checker", font=("Arial", 16))
label_title.pack(pady=10)

label_password = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*", font=("Arial", 12), width=30)
entry_password.pack(pady=5)

button_check = tk.Button(root, text="Check Strength", font=("Arial", 12), command=evaluate_password)
button_check.pack(pady=10)

# Run the GUI event loop
root.mainloop()
