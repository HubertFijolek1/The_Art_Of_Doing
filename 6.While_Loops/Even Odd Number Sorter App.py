#While Loops Challenge 27: Even Odd Number Sorter App

print("Welcome to the Even Odd Number Sorter App")

flag = True

while flag:
    numbers_separated_comma = input("Give me series of numbers ")
    for x in numbers_separated_comma:
        numbers_separated_comma = numbers_separated_comma.replace(" ", "")
    numbers_separated_comma = numbers_separated_comma.split(",")
    print(numbers_separated_comma)
    evens = []
    odds = []
    print("\n---Result Summary---")
    for number in numbers_separated_comma:
        number = int(number)
        if number % 2 == 0:
            print("\t"+str(number)+" is even!")
            evens.append(number)
        else:
            print("\t"+str(number)+" is odd!")
            odds.append(number)


    print("\nThe following " +str(len(evens)) + " numbers are even: ")
    for num in evens:
        print("\t"+ str(num) )


    print("\nThe following "+ str(len(odds)) +" numbers are odd")
    for num in odds:
        print("\t"+str(num))

    decison = input("Would you like to run the program again: (y/n) ")
    if decison.startswith("y"):
        flag = True
        print("Okey, let's try again...")
    else:
        flag = False
        print("Thank tou for using the program. Goodbye")

