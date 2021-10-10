

import random

#Conditionals Challenge 17: Coin Toss App

print("Welcome in Coint Toss App")
print("\nI will flip a coin a set number of times")
num_flip = int(input("Hey, how many time would you like to toss a coin, bro: "))
yes_no = input("Next question is, would you like to see result of each individual coin flip (yes/no): ").lower()
print("\nFLIPPING!!!")
heads = 0
tails = 0
if yes_no.startswith("y"):
    for x in range(0,num_flip):
        coin = int(random.randint(0, 1))
        if coin == 0:
            heads = heads+1
            print("HEADS")
        elif coin == 1:
            tails = tails+1
            print("TAILS")

        if tails == heads:
            print("At "+str(x+1)+" flips, the number of heads and tails were equal at " +str(heads)+" each.")
    print("\nResults Of Flipping A Coing " +str(num_flip)+" Times: ")
    result_heads = ((heads/num_flip)*100)
    result_heads = round(result_heads,2)
    result_tails = ((tails/num_flip)*100)
    result_tails = round(result_tails,2)
    print("\n Side "+"\t\tCount"+"\t\tPercentage")
    print("Heads "+"\t\t"+str(heads)+"/"+str(num_flip)+"\t\t"+str(result_heads)+"%")
    print("Tails "+"\t\t"+str(tails)+"/"+str(num_flip)+"\t\t"+str(result_tails)+"%")
elif yes_no.startswith("n"):
    for x in range(0,num_flip):
        coin = int(random.randint(0, 1))
        if coin == 0:
            heads = heads+1
        elif coin == 1:
            tails = tails+1

        if tails == heads:
            print("At "+str(x+1)+" flips, the number of heads and tails were equal at " +str(heads)+" each.")
    print("\nResults Of Flipping A Coing " +str(num_flip)+" Times: ")
    result_heads = ((heads/num_flip)*100)
    result_heads = round(result_heads,2)
    result_tails = ((tails/num_flip)*100)
    result_tails = round(result_tails,2)
    print("\n Side "+"\t\tCount"+"\t\tPercentage")
    print("Heads "+"\t\t"+str(heads)+"/"+str(num_flip)+"\t\t"+str(result_heads)+"%")
    print("Tails "+"\t\t"+str(tails)+"/"+str(num_flip)+"\t\t"+str(result_tails)+"%")