import tkinter as tk
from tkinter import messagebox
from database import save_record, get_records


def calculate_bmi():
    try:
        name = name_entry.get().strip()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if not name:
            messagebox.showerror("Error", "Please enter your name.")
            return

        if weight <= 0 or height <= 0:
            messagebox.showerror(
                "Error",
                "Weight and height must be positive."
            )
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

        save_record(name, weight, height, bmi, category)

        messagebox.showinfo(
            "Success",
            "BMI record saved successfully!"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numeric values."
        )


def view_history():
    records = get_records()

    history_window = tk.Toplevel(root)
    history_window.title("BMI History")
    history_window.geometry("600x400")

    tk.Label(
        history_window,
        text="BMI History",
        font=("Arial", 18, "bold")
    ).pack(pady=15)

    if not records:
        tk.Label(
            history_window,
            text="No records found."
        ).pack()
        return

    for record in records:
        name, weight, height, bmi, category = record

        tk.Label(
            history_window,
            text=f"Name: {name} | Weight: {weight} kg | "
                 f"Height: {height} m | BMI: {bmi:.2f} | "
                 f"Category: {category}"
        ).pack(pady=5)


# Main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x450")

title_label = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Label(root, text="Height (meters):").pack()
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi
)
calculate_button.pack(pady=15)

history_button = tk.Button(
    root,
    text="View History",
    command=view_history
)
history_button.pack(pady=5)

result_label = tk.Label(
    root,
    text="Enter your details",
    font=("Arial", 14)
)
result_label.pack(pady=15)

root.mainloop()