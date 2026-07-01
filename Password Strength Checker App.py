import re
import tkinter as tk
from tkinter import messagebox


def check_password_strength():
    password = password_entry.get()

    if not password:
        messagebox.showwarning(
            "Input Error", "Please enter a password to check."
        )
        return

    # Criteria flags
    length_error = len(password) < 10
    digit_error = not re.search(r"\d", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    special_error = not re.search(r"[!@#$%^&*()'_,.;+-/=?\":{}|<>]", password)

    # Total criteria missed on the calculation score (out of 5)
    missed_criteria = (
        + length_error
        + digit_error
        + uppercase_error
        + lowercase_error
        + special_error
    )

    # Strength evaluation
    if missed_criteria == 0:
        strength = "Very Strong"
        color = "#28a745"  # Green
    elif missed_criteria <= 1:
        strength = "Strong"
        color = "#17a2b8"  # Teal
    elif missed_criteria <= 2:
        strength = "Moderate"
        color = "#ff7f07"  # Orange
    elif missed_criteria <= 3:
        strength = "Weak"
        color = "#f3ff07"  # Yellow
    else:
        strength = "Very Weak"
        color = "#dc3545"  # Red

    # Display or Build the missing requirements for the detailed feedback
    feedback = ""
    if length_error:
        feedback += "• At least 10-20 characters long\n"
    if uppercase_error:
        feedback += "• At least one uppercase letter (A-Z)\n"
    if lowercase_error:
        feedback += "• At least one lowercase letter (a-z)\n"
    if digit_error:
        feedback += "• At least one numeric digit (0-9)\n"
    if special_error:
        feedback += "• At least one special character (!@#$[]% etc.)\n"

    if missed_criteria == 0:
        result_label.config(
            text=f"Strength: {strength}", fg=color, font=("Helvetica", 14, "bold")
        )
        feedback_label.config(text="Your password meets all security criteria!")
    else:
        result_label.config(
            text=f"Strength: {strength}", fg=color, font=("Helvetica", 14, "bold")
        )
        feedback_label.config(
            text=f"To make it stronger, add:\n\n{feedback}", fg="#333"
        )


# --- GUI Setup ---
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x450")
root.configure(padx=20, pady=20)
root.resizable(False, False)

# Title
title_label = tk.Label(
    root, text="Password Strength Checker", font=("Helvetica", 16, "bold")
)
title_label.pack(pady=(0, 20))

instructions = tk.Label(
    root, text="Enter your password below to check its security:"
)
instructions.pack(pady=(0, 10))

# Password Entry
tk.Label(root, text="Enter Password:", font=("Helvetica", 11)).pack(anchor="w")
password_entry = tk.Entry(root, show="*", font=("Helvetica", 12), width=30)
password_entry.pack(pady=(5, 15), ipady=5)

# Check Button
check_button = tk.Button(
    root,
    text="Check Strength",
    command=check_password_strength,
    font=("Helvetica", 11, "bold"),
    bg="#007bff",
    fg="white",
    padx=10,
    pady=5,
)
check_button.pack(pady=10)

# Results
result_label = tk.Label(root, text="Strength: -", font=("Helvetica", 14))
result_label.pack(pady=10)

feedback_label = tk.Label(
    root, text="", font=("Helvetica", 10), justify="left", fg="#333"
)
feedback_label.pack(pady=10)

# Run the application
root.mainloop()
