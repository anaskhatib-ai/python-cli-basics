import random

print("\n___WELCOME TO ROCK PAPER AND SCISSORS GAME___\n")

options = ["r", "p", "s"]
computer_score = 0
your_score = 0

while True:
    user_input = input("Type R / P / S for rock paper scissors or Q to quit: ").lower().strip()

    if user_input == "q":
        print("GOOD BYE!")
        break

    if user_input not in options :
        print("Invalid input try again!")
        continue

    computer_pick = random.choice(options)
    print(f"Computer picked {computer_pick}.")

    if user_input == computer_pick:
        print("It's a tie!\n")

    elif (user_input == "r" and computer_pick == "s") or \
        (user_input == "s" and computer_pick == "p" )or \
       ( user_input == "p" and computer_pick == "r"):
        print("You won!")
        your_score += 1
        print(f"your score is {your_score}")
        print(f"computer's score is {computer_score}\n")

    else:
        print("You lost!")
        computer_score += 1
        print(f"computer's score is {computer_score}")
        print(f"your score is {your_score}\n")

    if your_score == 7:
        print("\nCONGRATULATION! you beated the computer! you made 7 points")   
        break

    elif computer_score == 7 :
        print(f"OOPS! you lost! you made {your_score} point(s)")
        break

    elif computer_score == 7 and your_score == 7:
        print("its a tie! ")
        break