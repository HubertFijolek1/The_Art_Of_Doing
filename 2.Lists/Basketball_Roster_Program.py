import math
import cmath
import datetime
from math import sqrt
import random

print("Welcome to the Basketball Roaster Program")
roster = []
point_guard = str.title(input("\nWho is you point guard: "))
roster.append(point_guard)
shooting_guard = str.title(input("Who is your shooting guard:  "))
roster.append(shooting_guard)
small_forward = str.title(input("Who is your power forward: "))
roster.append(small_forward)
power_forward = str.title(input("Who is your power forward: "))
roster.append(power_forward)
center = str.title(input("Who is your center: "))
roster.append(center)

print("\n\tYour starting 5 for the upcoming basketballl season")
print("\tPoint Guard: ","\t\t\t\t",roster[0])
print("\tShooting Guard: ","\t\t\t",roster[1])
print("\tSmall Forward: ","\t\t\t",roster[2])
print("\tPower Forward: ","\t\t\t",roster[3])
print("\tCenter: ","\t\t\t\t",roster[4])
injured_player = roster[2]
print("\nOh no,",roster[2],"is injured.")
roster.remove(roster[2])
print("Your roster only has ",len(roster),"players")
added_player = input("Who will take "+ injured_player +"'s spot: ").title()
roster.insert(2, added_player)

print("\n\tYour starting 5 for the upcoming basketballl season")
print("\tPoint Guard: ","\t\t\t\t",roster[0])
print("\tShooting Guard: ","\t\t\t",roster[1])
print("\tSmall Forward: ","\t\t\t",roster[2])
print("\tPower Forward: ","\t\t\t",roster[3])
print("\tCenter: ","\t\t\t\t",roster[4])

print("\nGood luck", roster[2], "you will do great!")
print("Your roster now has", len(roster), "players")