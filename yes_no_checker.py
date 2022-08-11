while True:
    question = input("would you like instructions").lower()

    if question == "yes" or question == "y" or question == "yeS":
        print("Hello welcome to my game *and the crowd goes wild* today I will be testing your maths skills with some "
              "addition, subtraction, multiplication, and division. You will be given 10 questions and once you get "
              "them all correct you win! Get ready to do some maths :)")
        break

    elif question == "no" or question == "n" or question == "nO":
        print("continue game")
        break

    else:
        print("please select yes or no")

