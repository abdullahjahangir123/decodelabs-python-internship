import json

print("===================================")
print(" Welcome To Personal Quiz ")
print("===================================")

score = 0
wrong_answers = []

# Question 1
answer1 = input("1. What is your name? ")

if answer1.lower() == "abdullah":
    print("Correct! +1 point")
    score += 1
else:
    print("Wrong! Correct answer is Abdullah.")
    wrong_answers.append({
        "question": "What is your name?",
        "your_answer": answer1,
        "correct_answer": "Abdullah"
    })

print()

# Question 2
answer2 = input("2. What is your age? ")

if answer2 == "18":
    print("Correct! +1 point")
    score += 1
else:
    print("Wrong! Correct answer is 18.")
    wrong_answers.append({
        "question": "What is your age?",
        "your_answer": answer2,
        "correct_answer": "18"
    })

print()

# Question 3
answer3 = input("3. What is your father name? ")

if answer3.lower() == "jahangir":
    print("Correct! +1 point")
    score += 1
else:
    print("Wrong! Correct answer is Jahangir.")
    wrong_answers.append({
        "question": "What is your father name?",
        "your_answer": answer3,
        "correct_answer": "Jahangir"
    })

# Save JSON file
with open("wrong_answers.json", "w") as file:
    json.dump(wrong_answers, file, indent=4)

print()
print("========================")
print("Final Score:", score, "/3")
print("========================")

if score == 3:
    print("Excellent Work!")
elif score == 2:
    print("Good Job!")
else:
    print("Try Again!")

print("Wrong answers saved in wrong_answers.json")
