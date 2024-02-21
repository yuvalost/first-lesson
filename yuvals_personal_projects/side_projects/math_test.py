import random  # Import the random module for generating random numbers
import time  # Import the time module for measuring time

math_symbols = ["+", "-", "*"]  # List of mathematical symbols
max_numbers = 12  # Maximum value for the numbers in equations
min_numbers = 1  # Minimum value for the numbers in equations
total_problems = 10  # Total number of problems to be generated

def generate_problem():
    """Function to generate a random math problem."""
    left = random.randint(min_numbers, max_numbers)  # Generate a random left operand
    right = random.randint(min_numbers, max_numbers)  # Generate a random right operand
    math_symbol = random.choice(math_symbols)  # Choose a random math symbol

    # Formulate the equation as a string
    equation_formation = str(left) + " " + math_symbol + " " + str(right)
    answer = eval(equation_formation)  # Calculate the answer using eval function
    return equation_formation, answer  # Return the equation and its answer

def play_game():
    """Function to play the math game."""
    wrong = 0  # Counter for wrong answers

    input("Let's start! Press enter to begin...")  # Prompt the user to start the game
    print("-" * 100)  # Print a separator line

    start_time = time.time()  # Record the start time of the game

    # Loop to generate and solve math problems
    for i in range(total_problems):
        equation_formation, answer = generate_problem()  # Generate a math problem
        while True:
            # Prompt the user to input their guess
            user_guess = input("Problem #" + str(i + 1) + ": " + equation_formation + " = ")

            if user_guess == str(answer):  # Check if the user's guess is correct
                break  # Exit the loop if the guess is correct

            wrong += 1  # Increment the wrong answer counter

    end_time = time.time()  # Record the end time of the game
    total_time = end_time - start_time  # Calculate the total time taken to complete the game

    print("-" * 100)  # Print a separator line
    print("Congratulations! You finished in", round(total_time), "seconds!")  # Print the total time taken

while True:
    play_game()  # Play the math game
    another_try = input("Would you like to try again? (y/n): ")  # Ask the user if they want to play again
    if another_try.lower() != "y":  # If the user doesn't want to play again
        print("Goodbye!")
        break  # Exit the loop and end the program
