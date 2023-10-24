import  random
import  time

math_symbols = ["+", "-", "*"]
max_numbers = 12
min_numbers = 1
total_problems = 2

def generate_problem():
    left = random.randint(min_numbers, max_numbers)
    right = random.randint(min_numbers, max_numbers)
    math_symbol = random.choice(math_symbols)

    equation_formation = str(left) + " " + math_symbol + " " + str(right)
    answer = eval(equation_formation)
    return equation_formation, answer
def play_game():
    wrong = 0
    input("press enter or any key (i dont care..)")
    print("-" * 100)

    start_time = time.time()

    for i in range(total_problems):
        equation_formation, answer = generate_problem()
        while True:
            user_guess = input("problem #" + str(i + 1) + ": " + equation_formation + " = ")

            if user_guess == str(answer):
                break

            wrong += 1

    end_time = time.time()
    total_time = end_time - start_time
    print("-" * 100)
    print("Nice work you finished in", round(total_time), "seconds!")
while True:
    play_game()
    anoter_try = input("Nice lets beat that time?y/n  ")
    if anoter_try != "y":
        print("i will take that as no....goodbye")
        break




