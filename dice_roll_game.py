def playgame():
    import random
    while True:
        user = input("roll the dice? ( y/n ) ").lower().strip()

        if user == "y":
            print("your number is:",(random.randint(1,6)) )
            

        if user == "n":
            print("good bye!")
            break
        if user.isdigit():
            print("enter y or n !")
            continue
        if user != "y" and user != "n":
            print("invalid input")
            continue

playgame()