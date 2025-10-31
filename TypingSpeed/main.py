import time
import random

messages = [
    "Hello World!",
    "Wake up to reality!",
    "Matin is the greatest programmer in the world!"
]
def typing_speed():
    
    rand = random.choice(messages)
    
    print(rand)
    start = time.time()
    entry = str(input("Enter the the above text: "))
    finish = time.time()
    
    if rand == entry:
        last = finish - start
        print(f"{last:.2f}")
    else:
        print("Please just enter the given text!")

typing_speed()
