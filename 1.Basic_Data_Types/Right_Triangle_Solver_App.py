# Basic Data Types Challenge 4 - Right Triangle Solver App
import math

print("Welcome to the Right Triangle Sover App")
leg1 = float(input("What is the first leg of the triangle: "))
leg2 = float(input("What is the second leg of the triangle: "))

leg3 = math.sqrt(leg1**2 + leg2**2)
leg3 = round(leg3,3)

area = 0.5 * leg1 * leg2
area = round(area, 3)

print("For a triangle with " + str(leg1)+ " and " + str(leg2)+" the hypotenus is " +str(leg3) + "."  )
print("For a triangle with " + str(leg1)+ " and " + str(leg2)+" the area is " +str(area) + "."  )