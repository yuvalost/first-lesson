import random  # Import the random module for generating random numbers

def throw_dice():
    """Function to simulate throwing a 27-sided dice."""
    return random.randint(1, 27)  # Return a random integer between 1 and 27 inclusive

num_throws = 1  # Number of dice throws, change this to the desired number

for _ in range(num_throws):  # Loop to perform the specified number of dice throws
    result = throw_dice()  # Call the throw_dice function to get a random result
    print("Dice rolled:", result)  # Print the result of the dice throw

print("")  # Print an empty line after all dice throws
