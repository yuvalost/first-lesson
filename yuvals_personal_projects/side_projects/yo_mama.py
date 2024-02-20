import random

def generate_setup():
    yo_mama_setups = [
        "Yo mama is so fat ",
        "Yo mama is so stupid ",
        "Yo mama is such a bitch ",
        "Yo mama is such a good person ",
        "Yo mama is so hot ",
        "Yo mama is so not funny ",
        # Add more "Yo mama" setups as needed
    ]
    setup = random.choice(yo_mama_setups)
    print(setup)
    punchline = input("punchline here: ")
    mama_joke = f"{setup} {punchline}"

    return mama_joke


# for _ in range(2):
#     print(generate_setup())
while True:
    print(generate_setup())
    try_again = input("again y/n: ")

    if try_again != "y":
        break
