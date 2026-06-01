# Personal Quiz Project – Python

## Project Overview

This is a simple Python quiz project.

The program asks the user 3 personal questions:

1. What is your name?
2. What is your age?
3. What is your father name?

The program checks every answer.

If the answer is correct:

- user gets +1 point

If the answer is wrong:

- correct answer is shown
- wrong answer is saved in JSON file

At the end the program shows total score.

---

## Project Features

- User input
- if / else conditions
- score system
- points for correct answers
- save wrong answers in JSON file
- final result message

---

## Questions

### Question 1

What is your name?

Correct answer:

Abdullah

### Question 2

What is your age?

Correct answer:

18

### Question 3

What is your father name?

Correct answer:

Jahangir

---

## Project Folder Structure

```bash
python-quiz-project-4/
│
├── main.py
├── wrong_answers.json
└── README.md
```

---

## Technologies Used

- Python 3
- JSON

---

## How To Run

### Step 1

Open VS Code

### Step 2

Open project folder

### Step 3

Open terminal

### Step 4

Run this command

```bash
python main.py
```

If python command does not work

```bash
python3 main.py
```

---

## Example Output

```text
===================================
 Welcome To Personal Quiz
===================================

1. What is your name?
Abdullah
Correct! +1 point

2. What is your age?
18
Correct! +1 point

3. What is your father name?
Jahangir
Correct! +1 point

Final Score: 3 / 3
Excellent Work!
```

---

## JSON Save Example

If user gives wrong answer

Example:

```json
[
    {
        "question": "What is your name?",
        "your_answer": "Ali",
        "correct_answer": "Abdullah"
    }
]
```

This file saves all wrong answers.

---

## Learning Purpose

This project helps learn:

- Python basics
- user input
- conditions
- score counting
- JSON file handling

---

## Created By

Abdullah
