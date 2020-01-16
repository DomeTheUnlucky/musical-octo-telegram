
from __future__ import division

print("Zbrajanje = 1")
print("Oduzimanje = 2")
print("Dijeljenje = 3")
print("Mnozenje = 4")
print("CM u MM = 5")
print("CM u M = 6")

module = input("Izaberi opciju: ")
			
if module is 1:
	num1 = input("Izaberi broj: ")
	num2 = input("Izaberi jos jedan broj: ")

	print(num1 + num2) #Zbrajanje

if module is 2:
	num1 = input("Izaberi broj: ")
	num2 = input("Izaberi jos jedan broj: ")

	print(num1 - num2) #Oduzimanje

if module is 3:
	num1 = input("Izaberi broj: ")
	num2 = input("Izaberi jos jedan broj: ")

	print(num1 / num2) #Dijeljenje

if module is 4:
	num1 = input("Izaberi broj: ")
	num2 = input("Izaberi jos jedan broj: ")

	print(num1 * num2) #Mnozenje

if module is 5:	
	num1 = input("Izaberi broj: ")
	print(num1 * 10 )

if module is 6:
	num1 = input("Izaberi broj: ")
	print(num1 / 100 )







#num1 = input("Enter a number: ")
#num2 = input("Enter an another number: ")
#num3 = input("Enter an module: ")



