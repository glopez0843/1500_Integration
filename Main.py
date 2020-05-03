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
answer = input("\nAnswer: ")
if answer == "A":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is A.")

print("\nQuestion 2: What does the function 'input()' do?")
print("A) Asks for the user to rate the program")
print("B) Displays the phrase in the parentheses")
print("C) Displays the phrase in the parentheses and has the user input a response")
answer = input("\nAnswer: ")
if answer == "C":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is C.")

print("\nQuestion 3: What symbol allows for someone to multiply?")
print("A) *")
print("B) x")
print("C) **")
print("D) %")
answer = input("\nAnswer: ")
if answer == "A":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is A.")

print("\nQuestion 4: What symbol allows for someone to divide with the outcome not being rounded?")
print("A) /")
print("B) //")
print("C) --")
print("D) %")
answer = input("\nAnswer: ")
if answer == "A":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is A.")

print("\nQuestion 5: What symbol allows for someone to divide with the outcome only being the remainder?")
print("A) //")
print("B) %")
print("C) /")
print("D) --")
answer = input("\nAnswer: ")
if answer == "B":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is B.")

# This question asks for an answer that is rounded after dividing.
print("\nQuestion 6: Solve 134 // 10")
answer = 134 // 10
answer_6 = int(input("\nAnswer: "))
if answer_6 == answer:
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is", answer)

# This question integrates different mathematical symbols used by Python.
# The user will input their answer into the program to see if they're correct.
print("\nQuestion 7: Solve 50 - 130 // 10 + 8 ** 2")
answer = 50 - 130 // 10 + 8 ** 2
answer_7 = int(input("\nAnswer: "))
if answer_7 == answer:
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is", answer)

print("\nQuestion 8: Which of the following is a shortcut operator? Explain its function.")
print("A) n += 1; performs the mathematical operation given by the sign and number (such as + for addition) on the variable n and reassigns to n")
print("B) n -= 1; performs the mathematical operation given by the sign and number (such as + for addition) on the number and reassigns to n")
print("C) n = n + 1; performs the mathematical operation given by the sign and number (such as + for addition) on the variable n and reassigns to n")
print("D) n = 1 + 1; performs the mathematical operation given by the sign and number (such as + for addition) on the number and reassigns to n")
answer = input("\nAnswer: ")
if answer == "A":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is A.")

print("\nQuestion 9: What is the purpose of 'elif' in a function?")
print("A) Connects more conditional statements in if-else statements")
print("B) Can be used instead of 'else' in an if-else statement")
print("C) None of the above")
print("D) Both A and B")
answer = input("\nAnswer: ")
if answer == "D":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is D.")

print("\nQuestion 10: What are 'while' and 'for' functions?")
print("A) Loop statements")
print("B) Conditional statements")
print("C) Strings")
print("D) None of the above")
answer = input("\nAnswer: ")
if answer == "A":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is A.")

print("\nQuestion 11: How are 'while' and 'for' functions different?")
print("A) 'while' loops will function until a condition is met; 'for' loops will function based on the programmer's given commands")
print("B) 'for' loops will function until a condition is met; 'while' loops will function based on the programmer's given commands")
print("C) Both function the same way")
answer = input("\nAnswer: ")
if answer == "A":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is A.")

print("\nQuestion 12: What are function definitions?")
print("A) Code that is programmed to create definitions")
print("B) Code that is programmed to run when called")
print("C) Code that is programmed to explain the purpose of other functions")
answer = input("\nAnswer: ")
if answer == "B":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is B.")

print("\nQuestion 13: How are function definitions written in a program?")
print("A) Another function creates them")
print("B) 'definition' is put in front of a function name")
print("C) They are already implemented in Python")
print("D) 'def' is put in front of a function name")
answer = input("\nAnswer: ")
if answer == "D":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is D.")

print("\nQuestion 14: What is a header?")
print("A) A title given to a function definition, written before 'def'")
print("B) The part of the program where you put your name and information about the program in pseudocode")
print("C) A title given to a function definition, written after 'def'")
print("D) None of the above")
answer = input("\nAnswer: ")
if answer == "C":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is C.")

print("\nQuestion 15: How is a function definition called?")
print("A) It's not")
print("B) Write the name of the function")
print("C) Write the name of the function with parenthesis after")
print("D) Write the header again without the colon")
print("E) Write the header again without the colon and parenthesis")
answer = input("\nAnswer: ")
if answer == "C":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is C.")

print("\nQuestion 16: Which is an example of a function definition?")
print("A) def example")
print("B) example def:")
print("C) def example():")
print("D) definition example():")
print("E) example()")
answer = input("\nAnswer: ")
if answer == "C":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is C.")

print("\nQuestion 17: What is a parameter?")
print("A) The variable in the parenthesis of a function definition")
print("B) The variable in the parenthesis that is given a value and sent to a function definition when called")
print("C) Another name for an argument")
print("D) A variable that is used in conditional statements")
answer = input("\nAnswer: ")
if answer == "A":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is A.")

print("\nQuestion 18: What is an argument?")
print("A) The variable that calls a function")
print("B) A variable used in loop statements")
print("C) The variable in the parenthesis that is given a value and sent to a function definition when called")
print("D) The variable in the parenthesis of a function definition")
answer = input("\nAnswer: ")
if answer == "C":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is C.")

print("\nQuestion 19: What is '!=' used for?")
print("A) Used to determine if the first value is greater than the second value")
print("B) Used to determine if both values or variable are not equal to each other")
print("C) Used to determine if both values or variable are equal to each other")
print("D) Used to determine if the first value is less than the second value")
answer = input("\nAnswer: ")
if answer == "C":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is C.")

print("\nQuestion 20: What is '<=' used for?")
print("A) Used to determine if the first value is greater than or equal to the second value")
print("B) Used to determine if the first value is greater than the second value")
print("C) Used to determine if the first value is less than the second value")
print("D) Used to determine if the first value is less than or equal to the second value")
answer = input("\nAnswer: ")
if answer == "D":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is D.")

print("\nQuestion 21: What is '>=' used for?")
print("A) Used to determine if the first value is greater than or equal to the second value")
print("B) Used to determine if the first value is greater than the second value")
print("C) Used to determine if the first value is less than the second value")
print("D) Used to determine if the first value is less than or equal to the second value")
answer = input("\nAnswer: ")
if answer == "A":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is A.")

print("\nQuestion 22: What is '<' used for?")
print("A) Used to determine if the first value is greater than the second value")
print("B) Used to determine if the first value is greater than or equal to the second value")
print("C) Used to determine if the first value is less than or equal to the second value")
print("D) Used to determine if the first value is less than the second value")
answer = input("\nAnswer: ")
if answer == "D":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is D.")

print("\nQuestion 23: What is '>' used for?")
print("A) Used to determine if the first value is greater than the second value")
print("B) Used to determine if the first value is greater than or equal to the second value")
print("C) Used to determine if the first value is less than or equal to the second value")
print("D) Used to determine if the first value is less than the second value")
answer = input("\nAnswer: ")
if answer == "A":
    print("That's correct!")
else:
    print("That's incorrect. The correct answer is A.")
