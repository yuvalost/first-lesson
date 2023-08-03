import time
player_name=input("before we start....whats your name?   ")
town_name = input(" what does arik want the name of the town to be? ")

def intro():
    print(f"You are the sheriff In the quaint town of {town_name}, ")
    print("where the air was always filled with the sweet cent of babies, ")
    print(f'and the streets were lined with charming cows, the town was protected by (you) Sheriff {player_name} ')
    print("one day... A notorious gang led by Billy the Bitch has show up looking for some gay orgy")
    print("....oh shit i mean trouble...in the good way!")
    print("his gang started to touch the towns man...i mean people!! you decided as the sheriff to stop this crazy shit ")
    print("you say: stop this crazy shit you Meanies!! this is my town and i dont like this un-holly touches!  ")
    print("You need to decide how to confront the gang and restore peace to the town.\n")


def encounter_gang():
    print("You encounter Billy the Bitch and his gang in the town center.")
    print("They are armed to the teeth and appear ready for violence.")
    print("They are armed to the teeth and appear ready for violence.\n")


def shoot_outcome():
    print("You decide Confront by draw your gun and open fire on Billy the Bitch and his gang.")
    print("one gang member got hit and the rest run away also billy (because that bitch always gets away with it.")
    print("Billy the bitch yelled: why you shoot me?.")
    print(f'{player_name}: beacuse i aint no bitch like you.....')
    print("rest of the town: owww shiittt.... that's a burn")
    print("Billy the bitch: ok ok thats nice but now it's personal! ")
    print("Billy the bitch took out his gun and started shooting at you, you fire back, the whole town runs for cover ")
    print("A chaotic shootout ensues. You manage to take down a few gang members.")
    print(f"However, their gunfire is accurate, and you get severely wounded. "
          f"{player_name} fall's to the ground and look at the sky saying: omg omg omg this is it and just die."
          f"Billy the bitch and the rest of the gang just laugh and continue doing....i guess gay shit \n")

    print(f"{player_name} wake up from the dead...shocked that youre still alive,"
          f"the town looks to be abandoned, you use your last strength to pick yourself up, "
          f"but cant believe you're still alive"
          f"{player_name}: how is this possible, and where is everyone?!\n")
    print("what to do you ask")
    print("1. look around the town of Holly-Holly-Holly-Holly.")
    print("2. run away.")

    decision = input("Enter the number of your decision: ")

    if decision == "1":
        print(f"{player_name} realize wounds are gone and that's a need for answer."
              f"you walk around the town and see a little girl in the old sallon."
              f"you walk towards her for some answer's")
    elif decision == "2":
        print("You find a good hiding spot and wait for the gang members to approach.")
        print("As they come close, you surprise them and manage to take down a few more.")
        print("However, they eventually overpower you and you fall unconscious.")
        print("You wake up later, and the town has been saved in your absence.")
    else:
        print("Invalid choice!")

    abandoned_house()


def negotiate_outcome():
    print("You decide to attempt a risky negotiation with Billy the Bitch and his gang. "
          "Surprisingly, they agree to listen, and you join the gang in one epic gay gang bang this town has ever seen"
          "(except Molly she seen some shit) after you finish... billy ask you to join his gang and fight as an "
          "outlaw! you think about it and say it's what i have been chosen for.\n")


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

def main():
    play_game()


if __name__ == "__main__":
    main()
