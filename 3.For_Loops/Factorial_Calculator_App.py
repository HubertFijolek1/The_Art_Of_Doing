import math
import cmath
import datetime
from math import sqrt
import random
# For Loops Challenge 13: Factorial Calculator App

print("Welcome to the Factorial Calculator App")

number = int(input("\nWhat number would you like to compute the factorial of? : "))
print(str(number) + "! =", end="")
for i in range(0 , number):
    print(str(i), end="*")
print(str(number))

x = math.factorial(number)
print("\nHere is the result fronm the math library: ")
print("The factorial of "+str(number)+" is "+str(x)+"!")

fact = 1
for i in range(1 , number+1):
    fact = fact * i

print("\nHere is the result from my own algorithm: ")
print("The factorial of "+str(number)+" is " + str(fact)+"!")

print("\nIt is shown twice that "+str(number)+"! = "+str(fact)+" with excitement")