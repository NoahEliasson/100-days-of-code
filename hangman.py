import random

word_list = ["ardvark", "baboon", "camel"]
idx = random.randrange(len(word_list))
chosen_word = word_list[idx]
print(chosen_word)


display = []
for i in range(len(chosen_word)):
    display+="_"

game_on = True

lives = 6

while game_on:
    guess_letter = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess_letter:
            display[position] = letter
    
    if guess_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_on = False
            print("you lose")

    print(f"{' '.join(display)}")
    
    if display.count("_") == 0:
        game_on = False
        print("you win")


        