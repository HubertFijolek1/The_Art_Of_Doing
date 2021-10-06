import math
import cmath
import datetime
from math import sqrt
import random
# For Loops Challenge 14: Fibonacci Calculator App

print("Welcome to the Fibonacci Calculator App")

num = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))
fib = [1,1]
for i in range(num-2):
    new_fib = fib[i] + fib[i+1]
    fib.append(new_fib)
print("The first 15 numbers of the Fibonacci sequence are: ")
for i in fib:
    print(i)

print("The corresponding Godler Ratio values are: ")
new_fib_list = []
for i in range(num-2):
    divide_number = fib[i]/fib[i-1]
    new_fib_list.append(divide_number)

for i in new_fib_list:
    print(i)


print("The ratio of consecutive Fibonacci terms approaches Phi; 1.618....")