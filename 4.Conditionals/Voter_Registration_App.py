#Conditionals Challenge 18: Voter Registration App
 
 
print("Welcome to the Voter Registration App")

name = input("What's your name bro: ").capitalize()
age = int(input("How old are you mate: "))

parties = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]


if age > 17:
    print("\nCongratulations "+str(name)+"! You are old enough to register to vote")
    print("Here is a list of political to join: ")
    
    for x in parties:
        print("\t-"+str(x))

    joining = input("\nWhat party would you like to join: ").capitalize()
    if joining in parties:
        print("Congratulations "+str(name)+"! You have joined the "+str(joining)+" party")
        if joining == "Republican" or joining == "Democratic":
            print("That is a major party!")
        elif joining == "Independent":
            print("You are an independent person!")
        else:
            print("That is not a major party.")
    else:
        print("That is not a given party.")
        



else:
    print("\nNot this time, baby... ;)")