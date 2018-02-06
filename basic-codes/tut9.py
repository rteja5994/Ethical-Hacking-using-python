#modules
#to use modules and import whicha re required

#in this program we are using "fabs" math.fabs() which is used to turn all negative integers to positive integers

import math

def Main():
	try:
		number = float(input("Please enter a number: "))
		number = math.fabs(number)
		print(number)

	except:
		print("You did not enter a number!!!")

if __name__=="__main__":
	Main()
