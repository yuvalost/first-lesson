# Define the points associated with each answer choice for each house.
answer_points = {
    'a': {'Gryffindor': 3, 'Ravenclaw': 1, 'Hufflepuff': 2, 'Slytherin': 1},
    'b': {'Gryffindor': 1, 'Ravenclaw': 3, 'Hufflepuff': 2, 'Slytherin': 1},
    'c': {'Gryffindor': 2, 'Ravenclaw': 2, 'Hufflepuff': 3, 'Slytherin': 2},
    'd': {'Gryffindor': 1, 'Ravenclaw': 1, 'Hufflepuff': 1, 'Slytherin': 3}
}

# Initialize house scores.
house_scores = {'Gryffindor': 0, 'Ravenclaw': 0, 'Hufflepuff': 0, 'Slytherin': 0}

# List of questions. You can add more questions as needed.
questions = [
    "1. What is your approach to facing danger? "
    
    "a) I confront it head-on.\n"
    "b) I analyze the situation carefully.\n"
    "c) I seek help and collaborate with others\n"
    "d) I use cunning and strategy to avoid it\n",

    "2. What is your approach to facing danger? \n"
    
    "a) Adventures and heroic tales..\n"
    "b) Mysteries and puzzles.\n"
    "c) Heartwarming stories about friendship.\n"
    "d) Books about achieving power and success.\n",

    "3. You have a choice between four Magic items.\n" 
    
    "a) A sword that only the worthy can pull from a stone.\n"
    "b) A riddle-locked chest with untold secrets inside.\n"
    "c) A lantern that leads you to the friends you seek.\n"
    "d) A cloak that makes you invisible.\n",

    "4. How do you respond to someone who wronged you or a friend?\n"
    
    "a) I confront them directly and demand an apology.\n"
    "b) I try to understand their motives and resolve the issue calmly.\n"
    "c) I forgive and forget, valuing harmony and kindness.\n"
    "d) I seek revenge or find a way to outsmart them.\n",

    "5. What's your favorite magical creature?\n"
    "a) Phoenix\n"
    "b) Thestral\n"
    "c) Hippogriff\n"
    "d) Basilisk.",

    "6. Which subject at Hogwarts would you be most excited to study?\n"
    "a) Defense Against the Dark Arts\n"
    "b) Potions and Alchemy\n"
    "c) Care of Magical Creatures\n"
    "d) Ancient Runes.",

    "7. What quality do you value most in others?\n"
    "a) Bravery\n"
    "b) Intelligence\n"
    "c) Loyalty\n"
    "d) Ambition.",

    "8. In a magical duel, which spell would you use?\n"
    "a) Expelliarmus\n"
    "b) Alohomora\n"
    "c) Patronus Charm\n"
    "d) Imperius Curse.",

    "9. Choose a word that best describes you:\n"
    "a) Daring\n"
    "b) Curious\n"
    "c) Loyal\n"
    "d) Ambitious.",

    "10. Which Hogwarts house do you secretly admire the most?\n"
    "a) Gryffindor\n"
    "b) Ravenclaw\n"
    "c) Hufflepuff\n"
    "d) Slytherin."

]

# Function to ask questions and update house scores.
def ask_question(question):
    print(question)
    answer = input(f"{name} choose your answer (a, b, c, or d): ").lower()
    for house in house_scores:
        house_scores[house] += answer_points[answer][house]

# Opening statement.
name = input("please enter your name: ")
print(f"Welcome {name} to the Hogwarts House Sorting Quiz!")
print("Answer the following questions to discover which Hogwarts house you belong to.")

# Ask all the questions.
for question in questions:
    ask_question(question)

# Determine the winning house with the highest score.
winning_house = max(house_scores, key=house_scores.get)

# Display the result to the player.
if name == "arik".lower():
    print(f"{name} belong's to whore house!)
else:
    print(f"{name} belong's to {winning_house}!")

# You can also add a brief description of the chosen house here.
