import random


def roll_dice():
    return random.randint(1, 6)


def main():
    print("Welcome to the Dice Game!")
    print("Guess the number rolled on the dice (1-6).")

    target_number = roll_dice()

    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 6:
                print("Please enter a valid guess between 1 and 6.")
                continue

            if guess == target_number:
                print("Congratulations! You guessed correctly.")
            else:
                print(f"Sorry, the correct number was {target_number}.")

            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() == "yes":
                print("Thanks for playing!")
                main()
            elif play_again.lower() != "yes":
                print("Invalid input. Game over.")
                break

            target_number = roll_dice()

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()






