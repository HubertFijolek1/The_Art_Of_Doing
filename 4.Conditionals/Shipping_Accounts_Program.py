#Conditionals Challenge 16: Shipping Accounts Program

users = ['eramom' , 'footea', 'davisv', 'papinukt', 'allen']
print("Welcome to the Shipping Accounts Program")

user = input("Hello, what is your username: ").lower()

if user in users:
    print("\nHello " +str(user) + ". Welcome back to your account. ")
    print("Current shipping prices are as follows: ")
    ship1 = 5.10
    ship2 = 5.00
    ship3 = 4.95
    ship4 = 4.80
    print("\nShipping orders 0 to 100: " + "\t\t$" + str(ship1) + "0 each")
    print("Shipping orders 100 to 500:" + "\t\t$" + str(ship2) + "0 each")
    print("Shipping orders 500 to 1000:" + "\t$" + str(ship3) + " each")
    print("Shipping orders over 1000: " + "\t\t$" + str(ship4) + "0 each")
    round(ship1,2)
    num_items = int(input("\nHow many items would you like to ship: "))
    if num_items < 100:
        result1 = num_items*ship1
        result1 = round(result1,2)
        print("To ship: " +str(num_items)+ " items will cost you "+str(result1)+"$ at "+str(ship1)+"$ per item.")
    elif num_items >100 and num_items <500:
        result2 = num_items * ship2
        result2 = round(result2, 2)
        print("To ship: " + str(num_items) + " items will cost you " + str(result2) + "$ at " + str(
            ship2) + "$ per item.")
    elif num_items > 500 and num_items <1000:
        result3 = num_items * ship3
        result3 = round(result3, 2)
        print("To ship: " + str(num_items) + " items will cost you " + str(result3) + "$ at " + str(
            ship3) + "$ per item.")
    elif num_items>1000:
        result4 = num_items * ship3
        result4 = round(result4, 2)
        print("To ship: " + str(num_items) + " items will cost you " + str(result4) + "$ at " + str(
            ship4) + "$ per item.")
    answer = input("Would you like to place this order (y/n): ")
    if answer == "y":
        print("Okay. Shipping your "+str(num_items)+" items")
    elif answer == "n":
        print("Okay, no order is being placed at this time.")

else:
    print("You are not on the list, I am sorry, but I have to say goodbye")