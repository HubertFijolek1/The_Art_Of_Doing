# Basic Data Types Challenge 5  - Multiplication/Exponent Table App

print("Welcome to the Multiplication/Exponent Table App")
name = input("Give me your name: ")
number = float(input("Give me your number: "))
message = name.title()+ " Math is cool!"
print("\nMultiplication Table for: " + str(number))

print("\t"+"1.0 * "+str(number)+" = " + str(round(1*number,4)))
print("\t"+"2.0 * "+str(number)+" = " + str(round(2*number,4)))
print("\t"+"3.0 * "+str(number)+" = " + str(round(3*number,4)))
print("\t"+"4.0 * "+str(number)+" = " + str(round(4*number,4)))
print("\t"+"5.0 * "+str(number)+" = " + str(round(5*number,4)))
print("\t"+"6.0 * "+str(number)+" = " + str(round(6*number,4)))
print("\t"+"7.0 * "+str(number)+" = " + str(round(7*number,4)))
print("\t"+"8.0 * "+str(number)+" = " + str(round(8*number,4)))
print("\t"+"9.0 * "+str(number)+" = " + str(round(9*number,4)))


print("\nExponent Table for "+ str(number))
print("\t"+str(number) + " ** 1 = "+ str(round(number**1,4)))
print("\t"+str(number) + " ** 2 = "+ str(round(number**2,4)))
print("\t"+str(number) + " ** 3 = "+ str(round(number**3,4)))
print("\t"+str(number) + " ** 4 = "+ str(round(number**4,4)))
print("\t"+str(number) + " ** 5 = "+ str(round(number**5,4)))
print("\t"+str(number) + " ** 6 = "+ str(round(number**6,4)))
print("\t"+str(number) + " ** 7 = "+ str(round(number**7,4)))
print("\t"+str(number) + " ** 8 = "+ str(round(number**8,4)))
print("\t"+str(number) + " ** 9 = "+ str(round(number**9,4)))

print("\n" + message)
print("\t" + message.lower())
print("\t\t" + message.title())
print("\t\t\t" + message.upper())