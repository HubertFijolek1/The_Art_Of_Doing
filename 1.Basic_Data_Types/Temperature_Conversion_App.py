f = float(input("Give me temperature in Fahrenheit: "))

c = (f-32) * 5/9
c = round(c,4)

k = (f-32)/1.8000 + 273.15
k = round(k,4)
print("Degrees Fahrenheit: "+"\t"+ str(f) + ".")
print("Degrees Celsius: "+ "\t"+"\t"+ str(c) + ".")
print("Degrees Kelvin: "+ "\t"+"\t"+str(k) + ".")