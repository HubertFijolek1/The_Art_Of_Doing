import math
import cmath
import datetime
from math import sqrt
import random

#For Loops Challenge 11: Binary Hexadecimal Converter App
print("Welcome to the Binary/Hexadecimal Converter App")

value = int(input("\nCompute binary and hexadecimal values up to the following decimal number: "))
print("Gererating lists... complete!")
decimal_values = list(range(1, value))
binary_values = []
hexadecimal_values = []
for i,y in zip(decimal_values,decimal_values):
    binary_values.append(bin(i))
    hexadecimal_values.append(hex(y))
print("\nUsing slices, we will now show you a portion of each list.")
dec_num1 = int(input("What decimal number would you like to start at: "))
dec_num2 = int(input("What decimal number would you like to stop at: "))


print("\nDecimal values from " + str(dec_num1) + " to " + str(dec_num2)+":")
for x in decimal_values[(dec_num1-1):dec_num2]:
    print(x)

print("\nBinary values from "+str(dec_num1) +" to " +str(dec_num2)+": ")
for x in binary_values[(dec_num1-1):dec_num2]:
    print(x)

print("\nHexadecimal values from "+str(dec_num1)+" to "+str(dec_num2)+":")
for x in hexadecimal_values[(dec_num1-1):dec_num2]:
    print(x)

input("Press Enter to see all values from 1 to 12")
print("Decimal----Binary----Hexadecimal")
print("---------------------------------")
for a,b,c in zip(decimal_values,binary_values,hexadecimal_values):
    print(str(a)+"----"+str(b)+"----"+str(c))