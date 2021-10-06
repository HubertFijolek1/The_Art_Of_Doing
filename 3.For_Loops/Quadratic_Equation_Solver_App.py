from math import sqrt

#For Loops Challenge 12: Quadratic Equation Solver App

print("Welcome to the Quadratic Equation Solver App")

print("\n A quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers. ")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion")
list_of_numbers = []
num_of_equation = int(input("\nHow many equations would you like to solve today: "))
for num_of_equation in range(1, num_of_equation+1):
    list_of_numbers.append(num_of_equation)
for i in list_of_numbers:
    print("\nSolving equation #" +str(list_of_numbers[0]))
    list_of_numbers.remove(list_of_numbers[0])
    print("--------------------------------------")
    a = float(input("Please enter your value of a(coefficient of x^2):" ))
    b = float(input("Please enter your value of b(coefficient of x):" ))
    c = float(input("Please enter your value of a(coefficient):" ))
    print("\nThe sollutions to" ,a, "x^2 + " ,b, "x +" ,c, "=0")
    delta = b**2 - (4*a*c)

    x1 = (-b - delta * (1/2))/(2*a)
    x2 = (-b + delta * (1/2))/(2*a)
    print("\nx1 = (",x1,"+",b,")")
    print("x2 = (",x2,"-",b,")")
print("\nThank you for using the Quadratic Equation Solver App. Goodbye")