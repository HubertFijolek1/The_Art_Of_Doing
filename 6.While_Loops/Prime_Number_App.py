import time

# While Loops Challenge 28: Prime Number App

print("Welcome to The Prime Number App")

flag = True
while flag:
    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")
    choice = input("\nEnter your choice 1 or 2: ")
    if choice=="1":

        number = int(input("\nEnter a number to determine if it is prime or not: "))
        if number%number==0 and number%1==0:
            print(str(number) +" is prime")
            prime_status = True
            choice_again = input("Would you like to run the program again(y/n):")
            if choice_again.startswith("y"):
                continue
            elif choice_again.startswith("n"):
                print("Thank you for using the program. Have a nice day ")
                break
        else:
            prime_status = False
            print(str(number)+"is not prime! ")

            choice_again = input("Would you like to run the program again(y/n):" )
            if choice_again.startswith("y"):
                print("YES")
                continue
            elif choice_again.startswith("n"):
                print("Thank you for using the program. Have a nice day ")
                break
    elif choice == "2":
        rang_1 = int(input("Enter the lower bound of your range: "))
        rang_2 = int(input("Enter the upper bound of your range: "))


        primes = []
        start_time = time.time()
        for num in range(rang_1,rang_2+1):
            if num > 1:
                prime_status = True
                for i in range(2,num):
                    if num % i == 0:
                        prime_status = False
                        break
            else:
                prime_status = False
            if prime_status:
                primes.append(num)
        end_time = time.time()
        delta_time = round(start_time - end_time , 6)


        for nume in primes:
            print(nume)

        print("Calculations took a "+str(delta_time)+" total of seconds. ")
        print("The following numbers between " + str(rang_1) + " and " + str(rang_2) + " are prime")
        print("Press enter to continue")
        input()

        choice = input("Would you like to run the program again (y/n): ")
        if choice.startswith("y"):
            continue
        elif choice.startswith("n"):
            print("Thank you for using The Program. Have a nice day.")
            flag = False


    else:
        print("This is not a valid option.")
        choice = input("Would you like run the program again (y/n): ")
        if choice.startswith("y"):
            continue

        elif choice.startswith("n"):
            print("\nThank you for using the program. Have a nice day. ")
            flag = False
