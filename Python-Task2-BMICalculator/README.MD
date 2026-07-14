# 🏥 Advanced BMI Calculator (Python Tkinter)

An Advanced BMI (Body Mass Index) Calculator built using **Python**, **Tkinter**, **SQLite**, and **Matplotlib**.

This application allows multiple users to calculate and save their BMI, maintain historical records, and visualize BMI trends using graphs.

---

# 📌 Features

## ✅ Beginner Features

- Graphical User Interface (GUI) using Tkinter
- Input fields for:
  - User Name
  - Weight (kg)
  - Height (cm)
- Calculate BMI with one click
- Displays BMI value
- Colour-coded BMI category:
  - 🔵 Underweight
  - 🟢 Normal
  - 🟠 Overweight
  - 🔴 Obese
- Input validation
- Error handling for invalid input

---

## ✅ Advanced Features

### 👤 Multi User Support

- Supports multiple users.
- Saves BMI separately for each person using their name.

---

### 📜 View History

Displays previously saved BMI records including:

- User Name
- BMI
- Date
- Time

---

### 📈 BMI Trend Graph

Displays a line graph showing the BMI history of the entered user using Matplotlib.

---

### ⚠ Database Error Handling

Handles database exceptions such as:

- Database connection failure
- Read errors
- Write errors

Shows user-friendly error messages.

---

### 🧹 Clear Button

Clears:

- Name
- Weight
- Height
- Result

---

### ❌ Exit Button

Safely closes the application.

---

# 🛠 Technologies Used

- Python 3
- Tkinter
- SQLite3
- Matplotlib
- Datetime
---

# 📦 Required Libraries

Install Matplotlib before running.

```bash
pip install matplotlib
```

SQLite and Tkinter are included with standard Python installation.

---

# ▶ How to Run

Clone the repository

```bash
git clone https://github.com/yourusername/BMI-Calculator.git
```

Go to project folder

```bash
cd BMI-Calculator
```

Run the project

```bash
python main.py
```

---

# 🧮 BMI Formula

```
BMI = Weight (kg) / Height² (m²)
```

---

# 📊 BMI Categories

| BMI Range | Category |
|------------|-----------|
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Normal |
| 25 – 29.9 | Overweight |
| 30 and Above | Obese |

---

# ✅ Feature Checklist

| Feature | Status |
|---------|--------|
| GUI built with Tkinter | ✅ |
| Weight & Height input fields | ✅ |
| Calculate button | ✅ |
| Colour-coded BMI result | ✅ |
| Multi-user support | ✅ |
| Historical records stored | ✅ |
| SQLite database | ✅ |
| Graph view using Matplotlib | ✅ |
| Database read/write error handling | ✅ |
| Clear button | ✅ |
| Exit button | ✅ |

---


# 👨‍💻 Author

**Krisha Vaghani**

Python | Tkinter | SQLite | Matplotlib

---

# 📄 License

This project is created for educational and internship purposes.

Free to use and modify.
