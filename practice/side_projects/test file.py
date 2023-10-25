def third_town():
    print("You have successfully left the town.")
    new_town()

print("Howie accepts your request, but if you don't add 'unicorn' to the story, then you die...")
print("Howie accepts your request, but if it's not good, then you die...")

while True:
    story = input("Start writing your story here -> ")
    if 'unicorn' in story.lower():
        print("OK, you may leave this town.")
        third_town()
        break
    else:
        print("Where is the unicorn? Start again.")


def new_town():
    Print("lovely day")