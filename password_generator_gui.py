import tkinter as tk
from tkinter import messagebox
import random
import string

# Generate Password Function
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Password must be at least 4 characters")
            return

        characters = ""

        if var_letters.get():
            characters += string.ascii_letters
        if var_digits.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one option")
            return

        # Remove confusing characters (Customization)
        exclude_chars = "O0l1"
        characters = ''.join(c for c in characters if c not in exclude_chars)

        # Strong password rule
        password = []

        if var_letters.get():
            password.append(random.choice(string.ascii_letters))
        if var_digits.get():
            password.append(random.choice(string.digits))
        if var_symbols.get():
            password.append(random.choice(string.punctuation))

        # Fill remaining characters
        while len(password) < length:
            password.append(random.choice(characters))

        random.shuffle(password)
        password = ''.join(password)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

# Copy to Clipboard
def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Clear fields
def clear_fields():
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# UI Setup
root = tk.Tk()
root.title("Dhamodharan Password Generator 🔐")
root.geometry("420x450")
root.config(bg="#1e1e2f")

# Title
tk.Label(root, text="🔐 Password Generator",
         font=("Arial", 18, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=15)

# Frame
frame = tk.Frame(root, bg="#2c2c3e")
frame.pack(pady=10, padx=20, fill="both")

# Length Input
tk.Label(frame, text="Password Length",
         bg="#2c2c3e", fg="white").pack(pady=5)

length_entry = tk.Entry(frame, font=("Arial", 12), justify="center")
length_entry.pack(pady=5)

# Options
var_letters = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar()
var_symbols = tk.BooleanVar()

tk.Checkbutton(frame, text="Include Letters",
               variable=var_letters,
               bg="#2c2c3e", fg="white",
               selectcolor="#1e1e2f").pack()

tk.Checkbutton(frame, text="Include Numbers",
               variable=var_digits,
               bg="#2c2c3e", fg="white",
               selectcolor="#1e1e2f").pack()

tk.Checkbutton(frame, text="Include Symbols",
               variable=var_symbols,
               bg="#2c2c3e", fg="white",
               selectcolor="#1e1e2f").pack()

# Generate Button
tk.Button(frame, text="Generate Password",
          font=("Arial", 12, "bold"),
          bg="#6c5ce7", fg="white",
          command=generate_password).pack(pady=10)

# Output Field
password_entry = tk.Entry(root, font=("Arial", 14), justify="center", width=25)
password_entry.pack(pady=15)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Copy 📋",
          bg="#00b894", fg="white",
          command=copy_password).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Clear 🧹",
          bg="#d63031", fg="white",
          command=clear_fields).grid(row=0, column=1, padx=10)

# Footer
tk.Label(root, text="Strong Password Generator | Python Tkinter",
         bg="#1e1e2f", fg="gray").pack(pady=10)

root.mainloop()