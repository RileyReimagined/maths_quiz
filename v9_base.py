# instructions
score = 0
while True:
    question = input("would you like instructions ").lower()

# this allows the user to choose whether they want to hear the instruction
    if question == "yes" or question == "y" or question == "yeS":
        # these are my instructions
        print("Hello welcome to my game today I will be testing your maths skills with some")
        print("addition, subtraction, multiplication, and division. You will be given 10 questions and once you get")
        print("them all correct you win! Get ready to do some maths :)")

        break

    elif question == "no" or question == "n" or question == "nO":
        print("onto question 1")
        break

# this is incase they pick something other than yes or no to prevent error
    else:
        print("please select yes or no")


# question 1
while True:
    question1 = input("First Question, what does 15 + 17 = ").lower()

# correct answer
    if question1 == "32":
        print("good job! onto question 2")
        score += 1
        print("your score:")
        print(score)
        break

# negative number
    elif question1 <= "0":
        print("must be a positive number")


# incorrect answer
    else:
        print("incorrect, what does 15 + 17 = ")
        score -= 1
        print("your score:")
        print(score)

# question 2
while True:
    question2 = input("Second Question, what does 64 + 36 = ").lower()

# correct answer
    if question2 == "100":
        print("good job! onto question 3")
        score += 1
        print("your score:")
        print(score)
        break

# negative number
    elif question1 <= "0":
        print("must be a positive number")

# incorrect answer
    else:
        print("incorrect, what does 64 + 36 = ")
        score -= 1
        print("your score:")
        print(score)


# question 3
while True:
    question1 = input("Third Question, what does 78 - 34 = ").lower()

# correct answer
    if question1 == "44":
        print("good job! onto question 4")
        score += 1
        print("your score:")
        print(score)
        break

# incorrect answer
    else:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)

# question 4
while True:
    question2 = input("Forth Question, what does 16 - 57 = ").lower()

# correct answer
    if question2 == "-41":
        print("good job! onto question 5")
        score += 1
        print("your score:")
        print(score)
        break

# incorrect answer
    else:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)

# question 5
while True:
    question1 = input("Fifth Question, what does 5 x 12 = ").lower()

# correct answer
    if question1 == "60":
        print("good job! onto question 6")
        score += 1
        print("your score:")
        print(score)
        break

# incorrect answer
    else:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)

# question 6
while True:
    question2 = input("Sixth Question, what does 12 x 13 = ").lower()

# correct answer
    if question2 == "156":
        print("good job! onto question 7")
        score += 1
        print("your score:")
        print(score)
        break

# incorrect answer
    else:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)

# question 7
while True:
    question1 = input("Seventh Question, what does 75 / 15 = ").lower()

# correct answer
    if question1 == "5":
        print("good job! onto question 8")
        score += 1
        print("your score:")
        print(score)
        break

# incorrect answer
    else:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)

# question 8
while True:
    question2 = input("Eighth Question, what does 15 / 4 = ").lower()

# correct answer
    if question2 == "3.75":
        print("good job! onto question 9")
        score += 1
        print("your score:")
        print(score)
        break

# incorrect answer
    else:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)

# question 9
while True:
    question1 = input("Ninth Question, what does 7 + ( 9 x 3 ) = ").lower()

    if question1 == "34":
        print("good job! onto question 10")
        score += 1
        print("your score:")
        print(score)
        break

    else:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)

# question 10
while True:
    question2 = input("Last Question, what does 18 - ( 8 / 2 ) = ").lower()

# correct answer
    if question2 == "14":
        print("Thank you for doing my quiz!")
        score += 1
        print("Your final score:")
        print(score)
        break

# incorrect answer
    else:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)
