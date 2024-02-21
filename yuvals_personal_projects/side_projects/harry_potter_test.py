# Dictionary defining points for each house based on the user's answers
answer_points = {
    'a': {'Gryffindor': 3, 'Ravenclaw': 1, 'Hufflepuff': 2, 'Slytherin': 1},
    'b': {'Gryffindor': 1, 'Ravenclaw': 3, 'Hufflepuff': 2, 'Slytherin': 1},
    'c': {'Gryffindor': 2, 'Ravenclaw': 2, 'Hufflepuff': 3, 'Slytherin': 2},
    'd': {'Gryffindor': 1, 'Ravenclaw': 1, 'Hufflepuff': 1, 'Slytherin': 3}
}

# Dictionary to store scores for each house
house_scores = {'Gryffindor': 0, 'Ravenclaw': 0, 'Hufflepuff': 0, 'Slytherin': 0}

# List of questions for the quiz
questions = [
    # Questions and answer options
]

# Function to ask a question and update house scores based on the user's answer
def ask_question(question):
    print(question)
    answer = input(f"{name} choose your answer (a, b, c, or d): ").lower()
    for house in house_scores:
        house_scores[house] += answer_points[answer][house]

# Main loop of the program
while True:
    name = input("please enter your name: ")  # Ask the user for their name
    print(f"Welcome {name} to the Hogwarts House Sorting Quiz!\n")  # Welcome message
    print("Answer the following questions to discover which Hogwarts house you belong to.")
    for question in questions:
        ask_question(question)  # Ask each question and update house scores accordingly

    # Determine the house with the highest score
    winning_house = max(house_scores, key=house_scores.get)

    # Print the result for the user
    if name.lower() == "arik":
        print(f"{name} belong's to whore house!")  # Special message for "arik"
    else:
        print(f"{name} belong's to {winning_house}!")  # Print the winning house

    play_again = input("again?y/n:  ")  # Ask the user if they want to play again
    if play_again.lower() != "y":
        print("ok loser...")  # End the game if the user doesn't want to play again
        break
    else:
        house_scores = {'Gryffindor': 0, 'Ravenclaw': 0, 'Hufflepuff': 0, 'Slytherin': 0}  # Reset scores for the next round
