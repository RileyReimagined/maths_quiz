# instructions
while True:
    question = input("would you like instructions ").lower()

    if question == "yes" or question == "y" or question == "yeS":
        print("Hello welcome to my game *and the crowd goes wild* today I will be testing your maths skills with some "
              "addition, subtraction, multiplication, and division. You will be given 10 questions and once you get "
              "them all correct you win! Get ready to do some maths :)")
        score = 0
        break

    elif question == "no" or question == "n" or question == "nO":
        print("onto question 1")
        break

    else:
        print("please select yes or no")


# question 1
while True:
    question1 = input("First Question, what does 15 + 17 = ").lower()

    if question1 == "32":
        print("good job! onto question 2")
        break

    elif question1 <= "0":
        print("must be a positive number")

    elif question1 > "200":
        print("out of range")

    else:
        print("incorrect, what does 15 + 17 = ")

# question 2
while True:
    question2 = input("Second Question, what does 64 + 36 = ").lower()

    if question2 == "100":
        print("good job! onto question 3")
        break

    elif question1 <= "0":
        print("must be a positive number")

    elif question1 > "250":
        print("out of range")

    else:
        print("incorrect, what does 64 + 36 = ")


# question 3
while True:
    question1 = input("Third Question, what does 78 - 34 = ").lower()

    if question1 == "44":
        print("good job! onto question 4")
        break

    else:
        print("incorrect")

# question 4
while True:
    question2 = input("Second Question, what does 16 - 57 = ").lower()

    if question2 == "-41":
        print("good job! onto question 5")
        break

    else:
        print("incorrect")
