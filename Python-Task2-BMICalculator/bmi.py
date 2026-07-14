import tkinter as tk
from tkinter import messagebox, Toplevel

import sqlite3
from datetime import datetime

import matplotlib.pyplot as plt

# Window Create
root = tk.Tk()

# Window Title
root.title(" My BMI Calculator")

# Window Size
root.geometry("500x600")
conn = sqlite3.connect("bmi.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bmi_records(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    weight REAL,
    height REAL,
    bmi REAL,
    date TEXT
)
""")

conn.commit()

name_label = tk.Label(root, text="Enter Your Name")
name_label.pack(pady=5)

name_entry = tk.Entry(root, width=30)
name_entry.pack()

# -----------------------

weight_label = tk.Label(root, text="Enter Weight (kg)")
weight_label.pack(pady=5)

weight_entry = tk.Entry(root, width=30)
weight_entry.pack()

# -----------------------

height_label = tk.Label(root, text="Enter Height (cm)")
height_label.pack(pady=5)

height_entry = tk.Entry(root, width=30)
height_entry.pack()
# -----------------------

result_label = tk.Label(root, text="")
result_label.pack()

def calculate_bmi():
    try:
        name = name_entry.get()

        if name == "":
            messagebox.showerror("Input Error", "Please Enter Name")
            return

        weight = float(weight_entry.get())
        height = float(height_entry.get())

        height = height / 100

        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Underweight"
            color = "blue"

        elif bmi < 25:
            category = "Normal"
            color = "green"

        elif bmi < 30:
            category = "Overweight"
            color = "orange"

        else:
            category = "Obese"
            color = "red"

        # Save into Database
        try:
            cursor.execute("""
            INSERT INTO bmi_records(name, weight, height, bmi, date)
            VALUES (?, ?, ?, ?, ?)
            """, (
                name,
                weight,
                height * 100,
                bmi,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ))

            conn.commit()

        except sqlite3.Error as e:
            messagebox.showerror(
                "Database Error",
                f"Unable to save record.\n\n{e}"
            )
            return

        result_label.config(
            text=f"{name}\nBMI : {bmi:.2f}\nCategory : {category}",
            fg=color
        )

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter valid numbers for Weight and Height."
        )
def view_history():

    history_window = Toplevel(root)
    history_window.title("BMI History")
    history_window.geometry("450x500")

    try:
        cursor.execute("""
        SELECT name, bmi, date
        FROM bmi_records
        ORDER BY id DESC
        """)

        records = cursor.fetchall()

    except sqlite3.Error as e:
        messagebox.showerror(
            "Database Error",
            f"Unable to read records.\n\n{e}"
        )
        return

    if len(records) == 0:

        tk.Label(
            history_window,
            text="No Records Found",
            font=("Arial", 14)
        ).pack(pady=20)

    else:

        for record in records:

            text = f"""
Name : {record[0]}
BMI : {record[1]:.2f}
Date : {record[2]}
----------------------------------------
"""

            tk.Label(
                history_window,
                text=text,
                justify="left",
                anchor="w"
            ).pack(anchor="w", padx=10)
def show_graph():

    name = name_entry.get()

    if name == "":
        messagebox.showerror(
            "Input Error",
            "Please Enter Name"
        )
        return

    cursor.execute("""
    SELECT bmi
    FROM bmi_records
    WHERE name=?
    ORDER BY id
    """, (name,))

    records = cursor.fetchall()

    if len(records) == 0:

        messagebox.showinfo(
            "No Data",
            "No BMI Records Found"
        )

        return

    bmi_list = []

    for record in records:

        bmi_list.append(record[0])

    plt.figure(figsize=(6,4))

    plt.plot(
        bmi_list,
        marker="o"
    )

    plt.title(f"BMI Trend - {name}")

    plt.xlabel("Record Number")

    plt.ylabel("BMI")

    plt.grid(True)

    plt.show()    
def clear_fields():

    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

    result_label.config(text="")        

calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi
)
calculate_button.pack(pady=10)

history_button = tk.Button(
    root,
    text="View History",
    command=view_history,
    width=20,
    bg="lightblue"
)
history_button.pack(pady=10)

graph_button = tk.Button(
    root,
    text="Show Graph",
    command=show_graph,
    width=20,
    bg="lightyellow"
)

graph_button.pack(pady=10)

clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_fields,
    width=20,
    bg="lightgray"
)

clear_button.pack(pady=10)

exit_button = tk.Button(
    root,
    text="Exit",
    command=root.destroy,
    width=20,
    bg="tomato",
    fg="white"
)

exit_button.pack(pady=10)

root.mainloop()
conn.close()