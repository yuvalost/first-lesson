# Initialization
results = {'a': {'Rachel': 3, 'yosi habolbol': 1, 'shir': 2, 'anna': 1},  # Scores for each girl based on option 'a'
           'b': {'Rachel': 4, 'yosi habolbol': 2, 'shir': 3, 'anna': 2},  # Scores for each girl based on option 'b'
           'c': {'Rachel': 1, 'yosi habolbol': 3, 'shir': 4, 'anna': 3},  # Scores for each girl based on option 'c'
           'd': {'Rachel': 2, 'yosi habolbol': 4, 'shir': 1, 'anna': 4},  # Scores for each girl based on option 'd'
}

girl_score = {'Rachel': 0, 'yosi habolbol': 0, 'shir': 0, 'anna': 0}  # Initialize scores for each girl to zero

questions = [
    # List of quiz questions with answer options
]

# Function Definition
def ask_question(question):
    """Function to ask a question, take user input, and update girl scores."""
    print(question)
    answer = input(f"{name} choose your answer (a, b, c, or d): ").lower()
    # Update scores for each girl based on the user's answer
    for i in girl_score:
        girl_score[i] += results[answer][i]

# Main Loop
while True:
    # Ask user for their name
    name = input("please enter your name: ").lower()
    # Welcome message
    print(f"Welcome {name} to the....what girl is for me Quiz!\n")
    print("lets show the girls.... .")
    # Description of each girl
    print("Rachel: An adventurous and outgoing outdoor enthusiast with a great sense of humor.\n")
    print("Anna: A thoughtful and artistic bookworm who enjoys quiet evenings at home.\n")
    print("Tamar: A career-focused and health-conscious traveler with a strong sense of ambition.\n")
    print("Shir: A free-spirited musician with a love for the arts and a bohemian style.\n")
    # Loop through each question and ask the user
    for question in questions:
        ask_question(question)

    # Determine the girl with the highest score
    winning_girl = max(girl_score, key=girl_score.get)

    # Special messages for certain names
    if name == "arik":
        print(f"{name} this isn't for you because you needs a man! \n")
    if name == "shlomi":
        print(f"{name} belong's to.....yosi habolbol \n")
    # Inform the user about their match
    elif winning_girl == 'yosi habolbol':
        print(f"{name} belong's to..... {winning_girl}! \n")
    else:
        print(f"{name} belong's to the girl named.... {winning_girl}!\n")

    # Ask if the user wants to play again
    play_again = input("again?y/n:  \n")
    if play_again != "y".lower():
        print("ok loser...")
        break
    else:
        # Reinitialize scores for each girl to zero for the next round
        girl_score = {'Rachel': 0, 'yosi habolbol': 0, 'shir': 0, 'anna': 0}
