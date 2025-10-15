import random

while True:
    rool_number = random.randint(1, 6)
    
    entry = int(input("Enter 1 to roll or 2 to exit: "))
    if entry == 1:
        print(f"\nYou rolled a {rool_number}\U0001F3B2 \n")
    else:
        print("Bye\U0001F44B")
        break