import math
import cmath
import datetime
from math import sqrt
import random

print("Welcome to the Favorite Teachers Program")
fav_techears = []
fav_techears.append(input("\nWho is your first favorite teacher: ").title())
fav_techears.append(input("Who is your second favorite teacher: ").title())
fav_techears.append(input("Who is your third favorite teacher: ").title())
fav_techears.append(input("Who is your fourth favorite teacher: ").title())
print("\nYour favourite teachers are: " + str(fav_techears)+".")
print("Your favourite teachers alphabetically order are: "+ str(sorted(fav_techears)))
print("Your favourite teachers in reverse alphabetical order are: " +str(sorted(fav_techears, reverse=True)))
print("\nYour top two techears are: "+fav_techears[0]+" and "+fav_techears[1])
print("your next two teacher two favourite teachers are: "+fav_techears[2]+" and "+fav_techears[3]+".")
print("Your last favourite teacher is: " + fav_techears[-1])
print("You have a total of" ,len(fav_techears), "favourite teachers")

print("\nOops, ",fav_techears[0], "is no longer your first teacher. Who is your new FAVOURITE teacher:")
new_fav = str.title(input())
fav_techears.insert(0,new_fav)
print("\n","Your favourite teachers ranked are: ",fav_techears)
print("Your favourite teachers alphabetically are: " + str(sorted(fav_techears)))
print("Your favourite teachers in reverse aplhabetical order are: " + str(sorted(fav_techears, reverse=True)))

print("\nYour top two teachers are: "+fav_techears[0] + " and " + fav_techears[1])
print("Your next two favourite teachers are: "+ fav_techears[2] +" and "+fav_techears[3])
print("Your last favourite teacher is: "+ fav_techears[-1])
print("You have a total of "+ str(len(fav_techears))+" favourite teachers.")

fav_techears.remove(input("\nYou've decided you no longer like a teacher. Wich teacher would you like to remove from you list: ").title())

print("\nYour favourite teachers ranked are: " + str(fav_techears))
print("Your favourite teachers ranked are: " + str(sorted(fav_techears)))
print("Your favourite teachers ranked are: " + str(sorted(fav_techears, reverse=True)))


print("\nYour top two teachers are: "+fav_techears[0]+" and "+fav_techears[1])
print("Your next two favourite teachers are : "+fav_techears[2]+" and "+fav_techears[3])
print("Your last favourite teacher is: "+fav_techears[-1])
print("You have a total of "+str(len(fav_techears))+" favourite teachers")