# 🔐 Password Generator (Python)

A simple and secure **Password Generator** built using **Python**. This application allows users to create strong random passwords by selecting the desired password length and choosing different character types such as uppercase letters, lowercase letters, numbers, and symbols.

The program validates user input, ensures password security by requiring at least two character types, and allows users to generate multiple passwords without restarting the application.

---

# 📌 Features

## ✅ Beginner Tier Features

- Prompt user to enter the desired password length
- Enforces a minimum password length of **8 characters**
- Option to include:
  - 🔠 Uppercase Letters
  - 🔡 Lowercase Letters
  - 🔢 Numbers
  - 🔣 Symbols
- Requires at least **2 character types** to be selected
- Generates a secure random password
- Displays the generated password
- Input validation for:
  - Invalid password length
  - Non-numeric input
  - Less than two character types selected
- Allows users to generate another password without restarting the program

---

# 🛠 Technologies Used

- Python 3
- random module
- string module

---

# 📂 Project Structure

```
Password-Generator/
│
├── password_generator.py
└── README.md
```

---

# 📦 Requirements

No external libraries are required.

This project only uses Python's built-in modules:

- random
- string

---

# ▶ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Password-Generator.git
```

### 2. Navigate to the project folder

```bash
cd Password-Generator
```

### 3. Run the program

```bash
python password_generator.py
```

---

# 🔒 Password Rules

- Minimum password length: **8 characters**
- At least **2 character types** must be selected
- Password can include:
  - Uppercase letters (A–Z)
  - Lowercase letters (a–z)
  - Numbers (0–9)
  - Symbols (!@#$%^&*)

---

# 💻 Sample Output

```
Enter Password Length (Minimum 8): 12

Include Uppercase? (y/n): y
Include Lowercase? (y/n): y
Include Numbers? (y/n): y
Include Symbols? (y/n): n

Generated Password:
Ab7xQm91LpZe

Generate another password? (y/n): y
```

---

# ✅ Feature Checklist

| Feature | Status |
|---------|--------|
| Prompt user for password length | ✅ |
| Minimum 8 characters enforced | ✅ |
| Select uppercase letters | ✅ |
| Select lowercase letters | ✅ |
| Select numbers | ✅ |
| Select symbols | ✅ |
| At least 2 character types required | ✅ |
| Generate secure random password | ✅ |
| Display generated password | ✅ |
| Input validation | ✅ |
| Generate another password without restarting | ✅ |

---

# 🚀 Future Improvements

- Graphical User Interface (Tkinter)
- Copy password to clipboard
- Password strength indicator
- Save password history
- Export passwords to a text file
- Dark mode interface
- Custom character exclusion
- QR code for generated password

---

# 👨‍💻 Author

**Krisha Vaghani**

Python Developer

---

# 📄 License

This project is developed for educational and internship purposes.

Feel free to use, modify, and improve this project.
