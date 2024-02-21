import random

title = input("please write a punch-line: ")


# Define lists of setup and punchline for dad jokes
def generate_dad_joke():
    # Define lists of setup and punchline for dad jokes
    # List of setup lines for dad jokes
    joke_setups = [
        "Why did the scarecrow win an award?",
        "Did you hear about the mathematician who's afraid of negative numbers?",
        "How does a penguin build its house?",
        "Why don't skeletons fight each other?",
        "What do you call fake spaghetti?",
        "Why did the bicycle fall over?",
        "What's orange and sounds like a parrot?",
        "Why did the tomato turn red?",
        "What do you call a fish wearing a crown?",
        "Why don't scientists trust atoms?",
        "What do you get when you cross a snowman and a vampire?",
        "What did one wall say to the other wall?",
        "How does a penguin build its house?",
        "What did one hat say to the other?",
        "Why don't eggs tell each other secrets?",
        "How do you organize a space party?",
        "Why did the math book look sad?",
        "Why did the golfer bring extra pants?",
        "What did one plate say to another plate?",
        "How do you catch a squirrel?",
        "Why did the scarecrow become a successful politician?",
        "Why don't scientists trust atoms?",
        "What did one ocean say to the other ocean?",
        "What's brown and sticky?",
        "Why did the computer go to therapy?",
        "How do you organize a space party?",
        "Why don't oysters donate to charity?",
        "What did the janitor say when he jumped out of the closet?",
        "Why don't skeletons fight each other?",
        "Why don't scientists trust atoms?",
        "Why did the bicycle fall over?",
        "What's orange and sounds like a parrot?",
        "Why did the tomato turn red?",
        "What do you call a fish wearing a crown?",
        "Why did the math book look sad?",
        "Why did the golfer bring extra pants?",
        "What did one plate say to another plate?",
        "How do you catch a squirrel?",
        "Why did the scarecrow become a successful politician?",
        "Why don't scientists trust atoms?",
        "What did one ocean say to the other ocean?",
        "What's brown and sticky?",
        "Why did the computer go to therapy?",
        "Why don't oysters donate to charity?",
        "What did the janitor say when he jumped out of the closet?",
        "Why don't scientists trust atoms?",
        "What did one hat say to the other?",
        "Why don't eggs tell each other secrets?",
        "How does a penguin build its house?",
        "What did one wall say to the other wall?",

    ]

    joke_punchlines = [
        # List of punchlines for dad jokes
        "Because he was outstanding in his field!",
        "He'll stop at nothing to avoid them!",
        "Igloos it together!",
        "They don't have the guts!",
        "An impasta!",
        "It was two-tired!",
        "A carrot!",
        "Because it saw the salad dressing!",
        "A kingfish!",
        "Because they make up everything!",
        "Frostbite!",
        "I'll meet you at the corner!",
        "Igloos it together!",
        "You stay here, I'll go on ahead!",
        "Because they might crack up!",
        "You planet!",
        "Because it had too many problems!",
        "In case he got a hole in one!",
        "They both know the dinner's on them!",
        "Because they're afraid of cracking up!",
        "Because it's nuts!",
        "He was outstanding in his field!",
        "Because they make up everything!",
        "It's water's edge!",
        "A stick!",
        "Because it had too many bytes!",
        "You planet!",
        "Because they are shellfish!",
        "Supplies!",
        "They don't have the guts!",
        "Because they make up everything!",
        "It was two-tired!",
        "A carrot!",
        "Because it saw the salad dressing!",
        "A kingfish!",
        "Because they make up everything!",
        "Frostbite!",
        "I'll meet you at the corner!",
        "Igloos it together!",
        "You stay here, I'll go on ahead!",
        "Because they might crack up!",
        "You planet!",
        "Because it had too many problems!",
        "In case he got a hole in one!",
        "They both know the dinner's on them!",
        "Because they're afraid of cracking up!",
        "Because it's nuts!",
        "He was outstanding in his field!",
        "Because they make up everything!",
        "It's water's edge!",
        "A stick!",
        "Because it had too many bytes!",
        "You planet!",
        "Because they are shellfish!",
        "Supplies!",

    ]


    setup = random.choice(joke_setups)
    # Choose a random setup line
    punchline = random.choice(joke_punchlines)
    # Choose a random punchline

    dad_joke = f"{setup}  {title}"

    return dad_joke

# Generate and print two random dad jokes
for _ in range(2):
    print(generate_dad_joke())
    # Generate and print a random dad joke until the user decides to stop
while True:
    print(generate_dad_joke())
    try_again = input("again y/n: " )
    # If the user doesn't want to try again, exit the loop
    if try_again != "y":
        break