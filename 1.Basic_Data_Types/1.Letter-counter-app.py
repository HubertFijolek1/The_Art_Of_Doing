
print("Welcome to the Letter Counter App")
name = input("What is your name: ").title().strip()
print("Hello, " + name + "!" )
print("I will count the number of times that a specific letter occurs in a message . \n")
message = input("Please enter a message: ").lower()
letter = input("Which letter would you like to count the occurrences of: ").lower()
i=0
for l in message:
    if letter == l: 
        i+=1
    
print(name + "your master has " + str(i)+ "'s in it")

