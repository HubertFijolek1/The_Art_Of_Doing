import random
import math
import datetime

print("Welcome in Guess My Word App")
#Our dictionary with diffrent keys and value

game_dict = {
 "sports":['basketball', 'baseball', 'soccer', 'football', 'tennis',
'curling'],
 "colors":['orange', 'yellow', 'purple', 'aquamarine', 'violet', 'gold'],
 "fruits":['apple', 'banana', 'watermelon', 'peach', 'mango', 'strawberry'],
 "classes":['english', 'history', 'science', 'mathematics', 'art', 'health'],
 }

#There will be keys from our game_dict
game_keys = []
for key in game_dict.keys():
    game_keys.append(key)

active = True
while active:
    #creating random value from the game_dict
    game_category = game_keys[random.randint(0, len(game_keys) - 1)]
    game_word = game_dict[game_category][random.randint(0, len(game_dict[game_category]) - 1)]
    # print(game_word)
    blank_word = []
    for letter in game_word:
        blank_word.append("-")
    print("\nGuess a "+str(len(game_word))+" word from the following category: "+game_category.title())
#  First part ends here

    guess = ""
    guess_count = 0

    while guess!=game_word:
        print("".join(blank_word))
        guess = input("\nEnter your chance: ").lower()
        guess_count += 1

        if guess == game_word:
            print("Oh yeah! You won the game in "+ str(guess_count) + " tries. Congratulations :D")
            break
        else:
            print("That is not correct. Let us reveal a letter to help you!")
            second_active = True
            while second_active:
                number = random.randint(0,len(game_word)-1)
                if blank_word[number] == "-":
                    blank_word[number] = game_word[number]
                    second_active = False


    choice = input("\n Would you like to play again (y/n): ").lower()
    if choice != "y":
        active = False
        print("Thank you for playing the game ")
