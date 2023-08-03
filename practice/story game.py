import time
player_name=input("before we start....whats your name?   ")

def intro():
    print("You are the sheriff In the quaint town of Holly-Holly-Holly-Holly, ")
    print("where the air was always filled with the sweet cent of babies, ")
    print(f'and the streets were lined with charming cows, one  Sheriff {player_name}   ')
    print("A notorious gang led by Billy the Bitch has taken over the town and is causing havoc.")
    print("You need to decide how to confront the gang and restore peace to the town.\n")


def encounter_gang():
    print("You encounter Billy the Bitch and his gang in the town center.")
    print("They are armed to the teeth and appear ready for violence.\n")


def shoot_outcome():
    print("You decide to draw your gun and open fire on Billy the Bitch and his gang.")
    print("A chaotic shootout ensues. You manage to take down a few gang members.")
    print("However, their gunfire is accurate, and you get severely wounded. You fall to the ground and die.\n")


def negotiate_outcome():
    print("You decide to attempt a risky negotiation with Billy the Bitch and his gang.")
    print("Surprisingly, they agree to listen, albeit skeptically.")
    print("You manage to convince them that their actions will lead to their demise.")
    print("Billy the Bitch decides to leave the town, and his gang reluctantly follows suit.\n")


def wrong_decision_outcome():
    print("You hesitate and struggle to decide on a plan of action.")
    print("Billy the Bitch seizes the opportunity and orders his gang to attack.")
    print("Caught off guard, you become an easy target. You're outnumbered and killed.\n")
    print("After 7 days, you awaken as if from a deep sleep. You realize you are now a cyborg.")
    print("Billy the Bitch and his gang are long gone, but you feel a newfound strength and determination.\n")


def abandoned_house():
    print("As you walk through the deserted town, you come across an old, abandoned house.")
    print("It looks eerie and unsettling. What will you do?")
    print("1. Enter the abandoned house to investigate.")
    print("2. Keep walking through the desolate streets, wary of the surroundings.")

    decision = input("Enter the number of your decision: ")

    if decision == "1":
        print("You cautiously enter the abandoned house.")
        print("Inside, you find remnants of the past and some supplies.")
        print("Suddenly, you hear footsteps behind you and turn around to face a mysterious figure.")
        print("The figure introduces themselves as Bobby B, a lone wanderer. They offer to join your cause.")
        print("With a new ally by your side, you continue your journey to restore the town.\n")
    elif decision == "2":
        print("You decide to avoid the abandoned house and continue walking through the desolate streets.")
        print("As you walk, you sense someone following you.")
        print("You turn around and come face-to-face with a mysterious figure.")
        print("The figure introduces themselves as Bobby B, a lone wanderer. They offer to join your cause.")
        print("With a new ally by your side, you continue your journey to restore the town.\n")
    else:
        print("Invalid choice!")


def play_game():
    intro()
    print("What will you do?")
    print("1. Confront Billy the Bitch and his gang head-on with force.")
    print("2. Try to negotiate a truce with Billy the Bitch and his gang.")
    print("3. Hesitate and analyze the situation further.")

    decision = input("Enter the number of your decision: ")

    if decision == "1":
        shoot_outcome()
    elif decision == "2":
        negotiate_outcome()
    elif decision == "3":
        wrong_decision_outcome()

    abandoned_house()


def main():
    play_game()


if __name__ == "__main__":
    main()
