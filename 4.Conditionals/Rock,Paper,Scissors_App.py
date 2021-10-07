import random

# Conditionals Challenge 20: Rock, Paper, Scissors App

print("Welcome to a game of Rock, Paper, Scissors")

rounds = int(input("\nHow many rounds would you like to play: "))

moves = ["rock", "paper", "scissors"]
players_score = 0
computer_score = 0


for x in range(1, rounds+1):
    num = random.randrange(0,3)
    print("\nRound: "+str(x))
    print("Player: "+str(players_score)+ "\tComputer: "+str(computer_score))
    move_player = input("Time to pick...rock,paper,scissors: ").lower()
    print("Player: "+str(move_player))
    print("Computer: "+str(moves[num]))
    if move_player == moves[0] and moves[num] == moves[1]:
        print("Computer win!")
        print("Paper covers rock!")
        computer_score += 1
    elif move_player == moves[1] and moves[num] == moves[2]:
        print("Computer win!")
        print("Scissors cut paper!")
        computer_score += 1
    elif move_player == moves[2] and moves[num] == moves[0]:
        print("Computer win!")
        print("")
        computer_score +=1
    elif move_player == moves[1] and moves[num] == moves[0]:
        print("You win!")
        players_score +=1
    elif move_player == moves[2] and moves[num] == moves[1]:
        print("You win!")
        players_score +=1
    elif move_player == moves[0] and moves[num] == moves[2]:
        print("You win!")
        players_score +=1
    elif move_player == moves[0] and moves[num] == moves[0]:
        print("It is a draft! How boring...")
    elif move_player == moves[1] and moves[num] == moves[1]:
        print("It is a draft! How boring...")
    elif move_player == moves[2] and moves[num] == moves[2]:
        print("It is a draft! How boring...")
    elif move_player != moves[0] and move_player != moves[1] and move_player != moves[2]:
        print("I guess, you've type something wrong, that's why computer get a point!")
        computer_score +=1
print("\nFinal Game Results")
print("\tRounds Played: "+str(rounds))
print("\tPlayer Score: "+str(players_score))
print("\tComputer Score:  "+str(computer_score))
if computer_score > players_score:
    print("\tWinner: Computer ")
elif computer_score < players_score:
    print("\tWinner is you!")
else:
    print("The game was a tie... ")
