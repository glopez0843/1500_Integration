# Glenn Lopez
# My Integration Project
# Source used:
# https://pythoninstitute.org/certification/pcep-certification-entry-level/pcep-exam-syllabus/

print("Hello!")
name = input("What's your name? ")
print("Welcome to my integration project,", name+"!")

print("\nThis program will quiz you and prepare you for the PCEP Exam.")
print("Only type the letter or number as your answer unless otherwise indicated.")

# The quiz will being with topics listed in the first exam block of the PCEP Exam Syllabus.
print("\nLet's start with Exam Block #1: Basic Concepts")

print("\nQuestion 1: What does the function 'print()' do?")
print("A) Displays the phrase in the parentheses")
print("B) Displays the phrase in the parentheses and has the user input a response")
print("C) Prints the program")
answer1 = input("\nAnswer: ")
if answer1 == "A":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is A.")

print("\nQuestion 2: What does the function 'input()' do?")
print("A) Asks for the user to rate the program")
print("B) Displays the phrase in the parentheses")
print("C) Displays the phrase in the parentheses and has the user input a response")
answer2 = input("\nAnswer: ")
if answer2 == "C":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is C.")

print("\nQuestion 3: What symbol allows for someone to multiply?")
print("A) *")
print("B) x")
print("C) **")
print("D) %")
answer3 = input("\nAnswer: ")
if answer3 == "A":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is A.")

print("\nQuestion 4: What symbol allows for someone to divide with the outcome not being rounded?")
print("A) /")
print("B) //")
print("C) --")
print("D) %")
answer4 = input("\nAnswer: ")
if answer4 == "A":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is A.")

print("\nQuestion 5: What symbol allows for someone to divide with the outcome only being the remainder?")
print("A) //")
print("B) %")
print("C) /")
print("D) --")
answer5 = input("\nAnswer: ")
if answer5 == "B":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is B.")

# This question asks for an answer that is rounded after dividing.
print("\nQuestion 6: Solve 134 // 10")
answer6 = 134 // 10
answer_6 = int(input("\nAnswer: "))
if answer_6 == answer6:
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is", answer6)

# This question integrates different mathematical symbols used by Python.
# The user will input their answer into the program to see if they're correct.
print("\nQuestion 7: Solve 50 - 130 // 10 + 8 ** 2")
answer7 = 50 - 130 // 10 + 8 ** 2
answer_7 = int(input("\nAnswer: "))
if answer_7 == answer7:
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is", answer7)

print("\nQuestion 7: Solve 50 - 130 // 10 + 8 ** 2")
answer7 = 50 - 130 // 10 + 8 ** 2
answer_7 = int(input("\nAnswer: "))
if answer_7 == answer7:
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is", answer7)
