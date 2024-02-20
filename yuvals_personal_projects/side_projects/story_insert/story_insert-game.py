with open("story1.txt", "r") as f: #with=contaxt to this file and best practice, r=means it in read mode and you could use file without overwriting.
    story = f.read()

words = set()
start_of_word = -1

traget_start = "<"
traget_end = ">"

for i, char in enumerate(story):
    if char == traget_start:
        start_of_word = i
    if char == traget_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word) #add is better than set because it will make sure no duplicte
        start_of_word = -1

answers = {}

suggestions = {
    "<adjective>": ["charming", "cazy", "bustling", "mysterious"],
    "<your_name>": ["make up a name", "Emily", "Alex", "Sophia"],
    "<emotion>": ["nervous", "excited", "happy", "confident"],
    "<girl_name>": ["Emma", "Sarah", "Lily", "Olivia"],
    "<Friend_1>": ["John", "Kate", "Mike", "mysterious person"],
    "<Friend_2>": ["David", "Lisa", "Mark", "Anna" , "Sophia"],
    "<Friend_3>": ["Chris", "Megan", "Tom", "Olivia"],
    "<Competitor_Name>": ["Mike", "Alex", "Tom", "Chris", "somone you hate"],
    "<Action>": ["telling jokes", "dancing", "playing the guitar", "being himself", "bad stuff"],
    "<Adverb>": ["charmingly", "confidently", "humorously", "smoothly"],
    "<adjective>": ["red bar", "old saloon ", "or any name for an object"],
}


for word in words:
    if word in suggestions:
        suggestion_list = suggestions[word]
        suggestion_str = ", ".join(suggestion_list)
        answer = input(f"Enter a word for {word} or enter '?' for suggestions: ")
        if answer == '?':
            print(f"Suggestions for {word}: {', '.join(suggestions[word])}")
            answer = input(f"Enter a word for {word}: ")


    answers[word] = answer

for word, answer in answers.items():
    story = story.replace(word, answer)

# Print the complete story with the replaced words
print("\nHere's your modified story:\n")
print(story)
