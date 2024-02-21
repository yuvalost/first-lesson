import random  # Import the random module for generating random numbers

def roll_dice():
    """Function to simulate rolling a six-sided dice."""
    return random.randint(1, 6)  # Return a random integer between 1 and 6 inclusive

def main():
    """Main function to run the Dice Game."""
    print("Welcome to the Dice Game!")
    print("Guess the number rolled on the dice (1-6).")

    target_number = roll_dice()  # Roll the dice to get the target number

    while True:
        try:
            guess = int(input("Enter your guess: "))  # Prompt the user to enter their guess
            if guess < 1 or guess > 6:  # Check if the guess is within the valid range
                print("Please enter a valid guess between 1 and 6.")
                continue  # Ask the user to enter a valid guess

            if guess == target_number:  # Check if the guess matches the target number
                print("Congratulations! You guessed correctly.")
            else:
                print(f"Sorry, the correct number was {target_number}.")

            play_again = input("Do you want to play again? (yes/no): ")  # Ask the user if they want to play again
            if play_again.lower() == "yes":  # If the user wants to play again
                print("Thanks for playing!")
                main()  # Restart the game
            elif play_again.lower() != "yes":  # If the user doesn't want to play again
                print("Invalid input. Game over.")
                break  # End the game

            target_number = roll_dice()  # Roll the dice to get a new target number for the next round

        except ValueError:
            print("Please enter a valid number.")  # Handle the case where the user enters an invalid input

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
