

results = {'a': {'Rachel': 3, 'yosi habolbol': 1, 'shir': 2, 'anna': 1},
           'b': {'Rachel': 4, 'yosi habolbol': 2, 'shir': 3, 'anna': 2},
           'c': {'Rachel': 1, 'yosi habolbol': 3, 'shir': 4, 'anna': 3},
           'd': {'Rachel': 2, 'yosi habolbol': 4, 'shir': 1, 'anna': 4},
}

girl_score = {'Rachel': 0, 'yosi habolbol': 0, 'shir': 0, 'anna': 0}

questions = [

"What's your ideal date night?\n"
"a) A fancy dinner at a romantic restaurant\n"
"b) Netflix and pizza at home\n"
"c) A fun outdoor adventure\n"
"d) sex\n",

"What's your communication style?\n"
"a) I love deep, meaningful conversations\n"
"b) I prefer light-hearted and humorous chats\n"
"c) I'm a great listener and observer\n"
"d) sex\n",

"How do you handle conflict in a relationship?\n"
"a) Confront it head-on and communicate openly\n"
"b) Avoid confrontation and hope it resolves itself\n"
"c) Find a compromise and keep the peace\n"
"d) sex\n",

"What's your ideal vacation destination?\n"
"a) A bustling city with cultural attractions\n"
"b) A quiet beach with a good book\n"
"c) A remote cabin in the mountains\n"
"d) sex\n",

"What's your stance on having children?\n"
"a) I definitely want kids someday\n"
"b) I'm not sure if I want children\n"
"c) I prefer not to have children\n"
"d) sex\n",

"What's your attitude towards personal space and independence?\n"
"a) I need a lot of personal space and independence\n"
"b) I enjoy spending time together but also need me-time\n"
"c) I'm happiest when we do everything together\n"
"d) sex\n",

"What role does humor play in your life?\n"
"a) I appreciate a partner who can make me laugh\n"
"b) I value a good sense of humor but it's not essential\n"
"c) Humor is not a priority for me in a partner\n"
"d) sex\n",

"What's your approach to handling finances in a relationship?\n"
"a) Joint finances and shared responsibility\n"
"b) Keeping some financial independence\n"
"c) Separate finances and bills\n"
"d) sex\n",

]

def ask_question(question):
    print(question)
    answer = input(f"{name} choose your answer (a, b, c, or d): ").lower()
    for i in girl_score:
        girl_score[i] += results[answer][i]



while True:
    name = input("please enter your name: ").lower()
    print(f"Welcome {name} to the....what girl is for me Quiz!\n")
    print("lets show the girls.... .")
    print("Rachel: An adventurous and outgoing outdoor enthusiast with a great sense of humor.\n")
    print("Anna: A thoughtful and artistic bookworm who enjoys quiet evenings at home.\n")
    print("Tamar: A career-focused and health-conscious traveler with a strong sense of ambition.\n")
    print("Shir: A free-spirited musician with a love for the arts and a bohemian style.\n")
    for question in questions:
        ask_question(question)


    winning_girl = max(girl_score, key=girl_score.get)


    if name == "arik":
        print(f"{name} this isn't for you because you needs a man! \n")
    if name == "shlomi":
        print(f"{name} belong's to.....yosi habolbol \n")
    elif winning_girl == 'yosi habolbol':
        print(f"{name} belong's to..... {winning_girl}! \n")
    else:
        print(f"{name} belong's to the girl named.... {winning_girl}!\n")

    play_again = input("again?y/n:  \n")
    if play_again != "y".lower():
        print("ok loser...")
        break

    else:
     girl_score = {'Rachel': 0, 'yosi habolbol': 0, 'shir': 0, 'anna': 0}
