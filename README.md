🧮 Python Calculator — Lambda Functions

A basic calculator built using Python's lambda functions for each arithmetic operation, connected to a realistic keypad-style web interface via Flask.

Features:
Five operations: Addition, Subtraction, Multiplication, Division, Exponentiation
Core logic written entirely with lambda expressions
Real calculator-style UI — full number keypad, decimal point, AC, backspace
Supports chained calculations (e.g. 5 + 3 × 2, evaluated left to right, same as a physical calculator)
Keyboard input supported alongside on-screen clicks
Divide-by-zero and invalid input handled gracefully, shown on screen.

Tech Stack:
Layer	Tools
Logic	Python (lambda functions)
Backend	Flask
Frontend	HTML, CSS, JavaScript (vanilla)

Project Structure:
├── calculator.py          # Core calculator logic (lambda functions) + CLI version
├── app_calculator.py      # Flask server — connects calculator.py to the frontend
├── index.html             # Calculator UI
├── style.css               # Styling
└── .gitignore

How It Works:
calculator.py defines each operation as a lambda, dispatched through a calculator(choice, x, y) function. It also runs standalone as a terminal calculator if executed directly.
app_calculator.py imports calculator() directly — no logic is duplicated — and exposes a /calculate endpoint.
The frontend keypad sends the chosen operation and operand values as JSON; the backend runs the same function used by the terminal version and returns the result.

Setup & Run
bash
# 1. Install Flask
pip install flask

# 2. Start the server
python app_calculator.py

# 3. Open in browser
http://127.0.0.1:5000/
Using It

Type numbers using the on-screen keys or your keyboard, press an operator, type the next number, and press =. Press AC to reset, ⌫ to delete the last digit.


Author
Rashi Jain — BCA student, AI/ML enthusiast
