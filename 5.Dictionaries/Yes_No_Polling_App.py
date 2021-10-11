

#Dictionaries Challenge 23: Yes or No Polling App

print("Welcome to the Yes or No Issue Polling App")

issue = input("\nWhat is the yes or no issue you will be voting on today: ")
votes = int(input("What is the number of voters you will allow on the issue: "))
password = input("Enter a password for polling results: ")

vot_yes = 0
vot_no = 0
voters_of_pool = {

}

for x in range(1,votes+1):
    full_name = input("\nWhat is your full name: ").title()
    if full_name in voters_of_pool.keys():
        print("You have already voted, you cannot vote again")
    else:
        print(issue)
        result = input("Here type in you vote (yes/no): ").lower()
        if result == "yes" or  result.startswith("y"):
            result = "yes"
            vot_yes +=1
            print("Thank you "+str(full_name)+"! Your vote has been recorded")
        elif result == "no" or result.startswith("n"):
            result="no"
            vot_no +=1
            print("Thank you " + str(full_name) + "! Your vote has been recorded")
        else:
            print("Hmmm, are you sure this answer is correct "+str(result))
    voters_of_pool[full_name] = result
print("\nhe following "+str(votes)+" people voted.")
for x in voters_of_pool.keys():
         print(x)

print("\nOn the following issue: "+issue)

if vot_yes > vot_no:
    print("Yes wins! "+str(vot_yes)+ " to "+str(vot_no)+".")

elif vot_no > vot_yes:
    print("Oh no, lose! "+str(vot_no)+" to "+str(vot_yes))
else:
    print("It looks like a draw... oh maaan")

see_result = input("To see the voting results enter the admin password: ")
if see_result == password:
    for key, value in voters_of_pool.items():
        print("Voter: "+key +"\t\t Vote:"+value)
else:
    print("I guess, somebody don't remember password...  ;)")

print("\nThanks for using our App, I hope you like it. :)")