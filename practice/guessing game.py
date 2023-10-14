# dice roll code
import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("please enter a number betweeen 2-4: ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Mustbe bettween 2 -4")
    else:
        print("invalid")


player_score = [0 for _ in range(players)]

while max(player_score) < 50:
    for player_idx in range(players):
        print("\nplayer", player_idx +1, "your turn has start's...now! (dont get a 1!)\n")  #in start of each game adds the players number
        current_score = 0

        while True:
            should_score = input("would you like to roll (y/n): ")
            if should_score.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("you rolled a 1! turn done!")
                print("nice! you scored out of 50:",current_score)
                break

            else:
                current_score += value
                print("you rolled a:", value)
                print("you scored:", current_score)
                if current_score >= 20:
                    print(f"\nyou won player {player_idx+1}")
                    break

    player_score[player_idx] += current_score #add to your score
