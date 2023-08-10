import random

def throw_dice():
    return random.randint(1, 27)

num_throws = 1  # Change this to the desired number of dice throws

for _ in range(num_throws):
    result = throw_dice()
    print("Dice rolled:", result)