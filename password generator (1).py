import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())

    # Check if at least one option is selected
    if not (include_upper.get() or include_lower.get() or include_numbers.get() or include_symbols.get()):
        messagebox.showwarning("Warning", "Please select at least one option.")
        return

    characters = ""

    # Include selected options
    if include_upper.get():
        characters += string.ascii_uppercase
    if include_lower.get():
        characters += string.ascii_lowercase
    if include_numbers.get():
        characters += string.digits
    if include_symbols.get():
        characters += string.punctuation

    if length < 6:
        messagebox.showwarning("Warning", "Password length should be at least 6 characters.")
    else:
        password = ''.join(random.choices(characters, k=length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

def toggle_password_visibility():
    current_state = password_entry.cget("show")
    if current_state == "*":
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.configure(background='indigo')

# Create and place widgets
length_label = tk.Label(root, text="Password Length:", bg='indigo', fg='white')
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=10)

include_upper = tk.BooleanVar()
upper_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=include_upper, bg='indigo', fg='white')
upper_check.pack()

include_lower = tk.BooleanVar()
lower_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=include_lower, bg='indigo', fg='white')
lower_check.pack()

include_numbers = tk.BooleanVar()
numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=include_numbers, bg='indigo', fg='white')
numbers_check.pack()

include_symbols = tk.BooleanVar()
symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=include_symbols, bg='indigo', fg='white')
symbols_check.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg='indigo', fg='white')
generate_button.pack(pady=20)

password_label = tk.Label(root, text="Generated Password:", bg='indigo', fg='white')
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

view_button = tk.Button(root, text="View Password", command=toggle_password_visibility, bg='indigo', fg='white')
view_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
