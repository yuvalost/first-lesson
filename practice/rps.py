import random
name = input("please enter you name: ")


def rps():
    max_number = 3
    min_number = 1
    a = random.randint(min_number, max_number)

    return a
while True:
    user_hand = int(input("You're playing rock, paper, scissors: \n1. rock \n2. scissors \n3. paper \nchoose.... "))
    value = rps()

#if rock
    if value == 1 and user_hand == 1:
        print(f"3...2...1....i choose rock....so did you it's a Tie!! lets go again {name}")

    elif value == 2 and user_hand == 1:
        print(f"3...2...1....i choose scissors....damm i lost... lets go again {name}")

    elif value == 3 and user_hand == 1:
        print(f"3...2...1....i choose paper....hell yeah you lost!!! lets go again {name}")
    # if scissors
    elif value == 1 and user_hand == 2:
        print(f"3...2...1....i choose rock....hell yeah i win that means you lost!!! lets go again {name}")

    elif value == 2 and user_hand == 2:
        print(f"3...2...1....i choose scissors....so did you it's a Tie!! lets go again {name}")

    elif value == 3 and user_hand == 2:
        print(f"3...2...1....i choose paper....damm i lost.... lets go again {name}")
    # if paper
    elif value == 1 and user_hand == 3:
        print(f"3...2...1....i choose rock....damm i lost.... lets go again {name}")

    elif value == 2 and user_hand == 3:
        print(f"3...2...1....i choose scissors....hell yeah!!! i win, that means you lost!!! lets go again {name}")

    elif value == 3 and user_hand == 3:
        print(f"3...2...1....i choose paper....so did you, it's a Tie!! lets go again {name}")


    play_again = input("Want to try again?y/n   ")
    if play_again.lower() !="y":
        break
