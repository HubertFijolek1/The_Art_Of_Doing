import math
import cmath
import datetime
from math import sqrt
import random

# Lists Challenge 8: Grocery List App

your_list = ["Meat", "Cheese"]

print("Welcome to the Grocery List App")
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

print("Current Date and Time:",month,"/",day,hour,":",minute,".")
print("You currently have ",your_list[0]," and ",your_list[1], "in your list.")

your_list.append(str.title((input("\nType of food to add to the grocery list: "))))
your_list.append(str.title((input("Type of food to add to the grocery list: "))))
your_list.append(str.title((input("Type of food to add to the grocery list: "))))
print("\nHere is your grocery list: ")
print(your_list)
print("Here is your grocery list sorted: ")
your_list.sort()
print(your_list)
print("\nSimulating grocery shopping...")

print("\n Current grocery list: ",len(your_list),".")
print(your_list)
rem = str.title(input("What food did you just buy: "))
your_list.remove(rem)
print("Removing" ,str(rem), "from list...")
print(your_list)

print("\n Current grocery list: ",len(your_list),".")
print(your_list)
rem = str.title(input("What food did you just buy: "))
your_list.remove(rem)
print("Removing" ,str(rem), "from list...")
print(your_list)

print("\n Current grocery list: ",len(your_list),".")
print(your_list)
rem = str.title(input("What food did you just buy: "))
your_list.remove(rem)
print("Removing" ,str(rem), "from list...")

print("Current grocery list: ",len(your_list),"items")
print(your_list)

old_product = your_list[-1]
print("\n Sorry, the store is out of",old_product, ".")
new_product = input("What would you like instead: ")
your_list.remove(old_product),your_list.append(str.title(new_product))
print("\nHere is what remains on your grocery list:")
print(your_list)