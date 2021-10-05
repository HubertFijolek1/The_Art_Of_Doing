import math
import cmath
import datetime
from math import sqrt
import random
# Lists Challenge 6 - Grade Sorter App

print("Welcome to the Grade Sorter App")
grades = []
grade1 = int(input("\nWhat is your first grade (0-100): "))
grade2 = int(input("What is your first grade (0-100): "))
grade3 = int(input("What is your first grade (0-100): "))
grade4 = int(input("What is your first grade (0-100): "))
grades.append(grade1)
grades.append(grade2)
grades.append(grade3)
grades.append(grade4)
print("\nYour grades are: " + str(grades) + ".")
grades.sort(reverse=True)
print("\nYour grades from highest to lowest are: " + str(grades)+".")

print("\nThe lowest two grades will now be dropped.")
remove_grade = grades.pop()
print("Removed grade: "+ str(remove_grade) +".")
remove_grade = grades.pop()
print("Removed grade: "+ str(remove_grade) +".")
print("\nYour remaining grades are: "+str(grades)+".")
print("\nNice work! Your highest grade is a "+str(grades[0]))