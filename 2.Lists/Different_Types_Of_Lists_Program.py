import math
import cmath
import datetime
from math import sqrt
import random
# Lists Challenge 7  - Different Types of Lists Program

# Making 4 lists
num_strings = ["15","100","55","42"]
num_ints = [15,100,55,42]
num_floats = [1.2, 2.3, 3.4, 4.5]
num_lists = [[1,2,3,],[4,5,6],[7,8,9]]

# First 3 sentenceses
num_strings = type(num_strings)
print("\t\t\t Summary Table")
print("\nThe variable num_strings is a " +str(num_strings) +".")
num_strings = ["15","100","55","42"]
print("It contains the elements: ", num_strings ,".")
num1 = type(num_strings[0])
print("The element", num_strings[0], "is a ", num1 , "." )

# Second 3 sentences
num_ints = type(num_ints)
print("\nThe variable num_ints is a ",str(num_ints) ,".")
num_ints = [15,100,55,42]
print("It contains the elements: ",num_ints,".")
num2 = type(num_ints[0])
print("The element",num_ints[0],"is a",num2,".")

# Third 3 sentences
num_floats = type(num_floats)
print("\nThe variable num_floats is a", str(num_lists),".")
num_floats = [0.2, 2.3, 3.4, 4.5]
print("It contains the elements: ",num_floats ,".")
num3 = type(num_floats[0])
print("The element",num_floats[0],"is a ",num3,".")


# Fourth 3 sentences
num_lists = type(num_lists)
print("\nThe variable num_lists is a ",str(num_lists),".")
num_lists = [[0,2,3,],[4,5,6],[7,8,9]]
print("It contains the elements: ",num_lists,".")
num4 = type(num_lists[0])
print("The element", num_lists[0], "is a ",num4,".")


num_strings = ["15","100","55","42"]
num_ints = [15,100,55,42]
num_floats = [1.2, 2.3, 3.4, 4.5]
num_lists = [[1,2,3,],[4,5,6],[7,8,9]]

num_strings.sort()
num_ints.sort()
print("\nNow sorting num_strings and num_ints...")
print("Sorted num_strings: ", num_strings,".")
print("Sorted num_ints: ",num_ints, ".")

print("\nStrings are sorted alphabetically while integers are sorted numerically!")