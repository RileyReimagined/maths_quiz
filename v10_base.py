# instructions
score = 0
while True:
    question = input("would you like instructions ").lower()

# this allows the user to choose whether they want to hear the instruction
    if question == "yes" or question == "y" or question == "yeS":
        # these are my instructions
        print("Hello welcome to my game today I will be testing your maths skills with some")
        print("addition, subtraction, multiplication, division, and B.E.D.M.A.S. You will be given 10 questions and")
        print("once you get them all correct you win! Get ready to do some maths :)")

        break

    elif question == "no" or question == "n" or question == "nO":
        print("onto question 1")
        break

# this is incase they pick something other than yes or no to prevent error
    else:
        print("please select yes or no")


# question 1
import random

num1 = random.randint(1,20)
num2 = random.randint(1,20)
num3 = random.randint(10,50)
num4 = random.randint(10,50)

while True:
    question1 = int(input("First Question, what is {} + {}? ".format(num1, num2)))
    print(question1)

    if question1 == num1 + num2:
        print("good job! onto question 2")
        score += 1
        print("your score:")
        print(score)
        break

    elif question1 <= 0:
        print("must be a positive number")

    elif question1 != num1 + num2:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)

while True:
    question1 = int(input("Second Question, what is {} + {}? ".format(num3, num4)))
    print(question1)

    if question1 == num3 + num4:
        print("good job! onto question 3")
        score += 1
        print("your score:")
        print(score)
        break

    elif question1 <= 0:
        print("must be a positive number")

    elif question1 != num3 + num4:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)


# question 3
num5 = random.randint(1,20)
num6 = random.randint(1,20)
num7 = random.randint(10,50)
num8 = random.randint(10,50)

while True:
    question1 = int(input("Third Question, what is {} - {}? ".format(num5, num6)))
    print(question1)

    if question1 == num5 - num6:
        print("good job! onto question 4")
        score += 1
        print("your score:")
        print(score)
        break

    elif question1 != num5 - num6:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)

while True:
    question1 = int(input("Forth Question, what is {} - {}? ".format(num7, num8)))
    print(question1)

    if question1 == num7 - num8:
        print("good job! onto question 5")
        score += 1
        print("your score:")
        print(score)
        break

    elif question1 != num7 - num8:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)

# question 5
num9 = random.randint(1,10)
num10 = random.randint(1,10)
num11 = random.randint(1,20)
num12 = random.randint(1,20)

while True:
    question1 = int(input("Fifth Question, what is {} x {}? ".format(num9, num10)))
    print(question1)

    if question1 == num9 * num10:
        print("good job! onto question 6")
        score += 1
        print("your score:")
        print(score)
        break

    elif question1 != num9 * num10:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)

while True:
    question1 = int(input("Sixth Question, what is {} x {}? ".format(num11, num12)))
    print(question1)

    if question1 == num11 * num12:
        print("good job! onto question 7")
        score += 1
        print("your score:")
        print(score)
        break

    elif question1 != num11 * num12:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)

# question 7
num13 = random.randint(1,10)
num14 = random.randint(1,10)
num15 = random.randint(1,10)
num16 = random.randint(1,10)

while True:
    question1 = float(input("Seventh Question, what is {} ?? {}? ".format(num13, 2)))
    print(question1)

    if question1 == num13 / 2:
        print("good job! onto question 8")
        score += 1
        print("your score:")
        print(score)
        break

    elif question1 != num13 / 2:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)

while True:
    question1 = float(input("Eighth Question, what is {} ?? {}? ".format(num15, 4)))
    print(question1)

    if question1 == num15 / 4:
        print("good job! onto question 9")
        score += 1
        print("your score:")
        print(score)
        break

    elif question1 != num15 / 4:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)

# question 9
num17 = random.randint(1,10)
num18 = random.randint(1,10)
num19 = random.randint(1,10)
num20 = random.randint(1,10)
num21 = random.randint(1,10)
num22 = random.randint(1,10)

while True:
    question1 = int(input("Ninth Question, what is {} + ( {} x {} )? ".format(num17, num18, num19)))
    print(question1)

    if question1 == num18 * num19 + num17:
        print("good job! onto question 4")
        score += 1
        print("your score:")
        print(score)
        break

    elif question1 != num18 * num19 + num17:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)

while True:
    question2 = int(input("Last Question, what is {} + ( {} x {} )? ".format(num20, num21, num22)))
    print(question2)

    if question2 == num21 * num22 + num20:
        print("good job!")
        score += 1
        print("Your Final score:")
        print(score)
        break

    elif question2 != num21 * num22 + num20:
        print("incorrect")
        score -= 1
        print("your score:")
        print(score)

print("Thank you for playing :)")