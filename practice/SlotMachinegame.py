# Import the 'random' module to generate random numbers
import random

# Constants for the game
MAX_LINES = 3  # Maximum number of lines a player can bet on
MAX_BET = 100  # Maximum bet amount
MIN_BET = 1    # Minimum bet amount
LOSS_MULTIPLIER = 0.5  # Multiplier for the bet amount when there are no matching symbols

ROWS = 3  # Number of rows on the slot machine display
COLS = 3  # Number of columns on the slot machine display

# Dictionary to store the count and payout value of each symbol
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}


# Function to get a random spin result for the slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # Prepare a list with all the symbols, repeated based on their count
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    # Initialize an empty 2D list for the slot machine display
    columns = [[] for _ in range(cols)]
    for col in range(COLS):
        column = []
        current_symbols = all_symbols[:]
        # Randomly choose a symbol for each row in the column
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns[col] = column

    return columns


# Function to print the slot machine display
def print_slot_machine(columns):
    symbol_width = 8  # Width of the slot machine symbol cell

    # Print the top border
    print("+" + "-" * (symbol_width * COLS + COLS - 1) + "+")

    # Print the content of each row
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            symbol = column[row]
            print(f"| {symbol:{symbol_width}}", end="")
        print("|")

        # Print the row separator
        if row < len(columns[0]) - 1:
            print("+" + "-" * (symbol_width * COLS + COLS - 1) + "+")

    # Print the bottom border
    print("+" + "-" * (symbol_width * COLS + COLS - 1) + "+")


# Function to get the initial deposit amount from the player
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter an amount greater than 0.")
        else:
            print("Please enter a valid number.")

    return amount


# Function to get the number of lines the player wants to bet on
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please enter a valid number of lines (1-{MAX_LINES}).")
        else:
            print("Please enter a number.")

    return lines


# Function to get the bet amount from the player for each line
def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line? (${MIN_BET}-{MAX_BET}): $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please enter an amount between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


# Function to calculate the winnings or losses for a spin based on the slot machine result
def calculate_spin_result(columns, bet_per_line):
    symbol_set_list = [set(column) for column in columns]
    all_symbols = set.union(*symbol_set_list)
    num_unique_symbols = len(all_symbols)

    # Check if any row contains all the same symbols
    for row in range(len(columns[0])):
        symbol_set = symbol_set_list[row]
        if len(symbol_set) == 1:
            symbol = columns[0][row]
            if symbol in symbol_count:
                # Add the winnings based on the symbol and bet_per_line
                return symbol_count[symbol] * bet_per_line

    # No matching symbols in any row, return the loss amount
    return -int(LOSS_MULTIPLIER * bet_per_line * num_unique_symbols)


# Main game function
def main():
    # Get the initial balance from the player
    balance = deposit()
    total_winnings = 0

    # Game loop: continue playing until the player runs out of money (balance <= 0)
    while balance > 0:
        # Get the number of lines the player wants to bet on
        lines = get_number_of_lines()

        # Get the bet amount from the player for each line
        while True:
            bet = get_bet()
            total_bet = bet * lines
            if total_bet > balance:
                print(f"You don't have enough to bet that amount, your balance is ${balance}.")
            else:
                break

        print(f"You're betting ${bet} on {lines} lines. Total bet: ${total_bet}")

        # Get the slot machine spin result
        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)

        # Calculate the winnings or losses for the current spin
        result = calculate_spin_result(slots, bet)
        if result > 0:
            print(f"Congratulations! You won ${result}.")
        else:
            print(f"Better luck next time. You lost ${abs(result)}.")

        # Update the player's balance
        balance += result
        total_winnings += result

        print(f"Your current balance: ${balance}")

    print("Game over. You have no more money to bet.")
    print(f"Total winnings: ${total_winnings}")
    print(f"Final balance: ${balance}")


# Start the game
main()
