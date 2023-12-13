import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def on_calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        gender = gender_combobox.get()

        bmi = calculate_bmi(weight, height)
        bmi_category = interpret_bmi(bmi)

        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {bmi_category}\nAge: {age}\nGender: {gender}")

    except ValueError:
        result_label.config(text="Invalid input. Please enter numeric values.")

# Create main window
window = tk.Tk()
window.title("BMI Calculator")


# Create a frame
frame = ttk.Frame(window, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Labels and entry fields
ttk.Label(frame, text="Weight (kg):").grid(column=0, row=0, sticky=tk.W)
weight_entry = ttk.Entry(frame)
weight_entry.grid(column=1, row=0, sticky=tk.W)

ttk.Label(frame, text="Height (m):").grid(column=0, row=1, sticky=tk.W)
height_entry = ttk.Entry(frame)
height_entry.grid(column=1, row=1, sticky=tk.W)

ttk.Label(frame, text="Age:").grid(column=0, row=2, sticky=tk.W)
age_entry = ttk.Entry(frame)
age_entry.grid(column=1, row=2, sticky=tk.W)

ttk.Label(frame, text="Gender:").grid(column=0, row=3, sticky=tk.W)
gender_combobox = ttk.Combobox(frame, values=["Male", "Female"])
gender_combobox.grid(column=1, row=3, sticky=tk.W)

# Calculate button
calculate_button = ttk.Button(frame, text="Calculate", command=on_calculate)
calculate_button.grid(column=0, row=4, columnspan=2, pady=10)

# Result label
result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=5, columnspan=2)

# Run the main loop
window.mainloop()
