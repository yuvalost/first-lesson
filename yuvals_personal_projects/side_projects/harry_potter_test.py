
answer_points = {
    'a': {'Gryffindor': 3, 'Ravenclaw': 1, 'Hufflepuff': 2, 'Slytherin': 1},
    'b': {'Gryffindor': 1, 'Ravenclaw': 3, 'Hufflepuff': 2, 'Slytherin': 1},
    'c': {'Gryffindor': 2, 'Ravenclaw': 2, 'Hufflepuff': 3, 'Slytherin': 2},
    'd': {'Gryffindor': 1, 'Ravenclaw': 1, 'Hufflepuff': 1, 'Slytherin': 3}
}


house_scores = {'Gryffindor': 0, 'Ravenclaw': 0, 'Hufflepuff': 0, 'Slytherin': 0}


questions = [
    "\nWhat is your approach to facing danger? "
    
    "a) I confront it head-on.\n"
    "b) I analyze the situation carefully.\n"
    "c) I seek help and collaborate with others\n"
    "d) I use cunning and strategy to avoid it\n",

    "What is your approach to facing danger? \n"
    
    "a) Adventures and heroic tales..\n"
    "b) Mysteries and puzzles.\n"
    "c) Heartwarming stories about friendship.\n"
    "d) Books about achieving power and success.\n",

    "How do you respond to someone who wronged you or a friend?\n"
    
    "a) I confront them directly and demand an apology.\n"
    "b) I try to understand their motives and resolve the issue calmly.\n"
    "c) I forgive and forget, valuing harmony and kindness.\n"
    "d) I seek revenge or find a way to outsmart them.\n",

    "What's your favorite magical creature?\n"
    
    "a) Phoenix\n"
    "b) Thestral\n"
    "c) Hippogriff\n"
    "d) Basilisk.",

    "Which subject at Hogwarts would you be most excited to study?\n"
    
    "a) Defense Against the Dark Arts\n"
    "b) Potions and Alchemy\n"
    "c) Care of Magical Creatures\n"
    "d) Ancient Runes.",

    "What quality do you value most in others?\n"
    
    "a) Bravery\n"
    "b) Intelligence\n"
    "c) Loyalty\n"
    "d) Ambition.",



    "Choose a word that best describes you:\n"
    
    "a) Daring\n"
    "b) Curious\n"
    "c) Loyal\n"
    "d) Ambitious.",

    "Which Hogwarts house do you secretly admire the most?\n"
    
    "a) Gryffindor\n"
    "b) Ravenclaw\n"
    "c) Hufflepuff\n"
    "d) Slytherin."

]


def ask_question(question):
    print(question)
    answer = input(f"{name} choose your answer (a, b, c, or d): ").lower()
    for house in house_scores:
        house_scores[house] += answer_points[answer][house]




while True:
    name = input("please enter your name: ")
    print(f"Welcome {name} to the Hogwarts House Sorting Quiz!\n")
    print("Answer the following questions to discover which Hogwarts house you belong to.")
    for question in questions:
        ask_question(question)


    winning_house = max(house_scores, key=house_scores.get)


    if name == "arik".lower():
        print(f"{name} belong's to whore house!")
    else:
        print(f"{name} belong's to {winning_house}!")

    play_again = input("again?y/n:  ")
    if play_again != "y".lower():
        print("ok loser...")
        break

    else:
     house_scores = {'Gryffindor': 0, 'Ravenclaw': 0, 'Hufflepuff': 0, 'Slytherin': 0}





