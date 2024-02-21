# Import the random module for generating random numbers
import random


# Define a function to simulate rolling a six-sided dice
def roll():
    # Define the minimum and maximum values for the dice
    min_value = 1
    max_value = 6

    # Generate a random integer between min_value and max_value
    roll_result = random.randint(min_value, max_value)

    return roll_result  # Return the result of the dice roll


# Call the roll function to simulate rolling the dice and store the result in the variable 'value'
value = roll()

# Print the result of the dice roll
print(value)
