import random

run = True

while run:
    user_input = input("roll the disc press enter or type 'x' to stop:")
    if user_input=='x':
        break
    else:
        r = random.randint(1,6)
        print(f"you rolled {r}")
