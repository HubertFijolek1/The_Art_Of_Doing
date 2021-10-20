#While Loops Challenge 26: Factor Generator App

print("Welcome to the Factor Generator App")

flag = True
while flag:
    number_of_factors = int(input("\nEnter a number to determine all factor of that number: "))
    factors = []
    for x in range(1,number_of_factors+1):
        if number_of_factors % x == 0:
            factors.append(x)

    print("\nFactors of "+str(number_of_factors)+ " are")
    for y in factors:
        print(y)

    print("\nIn summary: ")
    while factors:
        result = factors[0] * factors[-1]
        print(str(factors[0])+" * "+str(factors[-1])+" = "+ str(result))
        del factors[0]
        del factors[-1]
    option = input("Would you like to continue (y/n): ").lower()
    if option.startswith("y"):
       flag = True
    elif option.startswith("n"):
        print("Thank you for using the program. Have a great day")
        flag = False