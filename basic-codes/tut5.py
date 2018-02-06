#to use functions and why main functions is used in programming

def getinteger():
	result = int(input("Please enter an integer: "))
	return result

def Main():
	print("Started")
	output = getinteger()
	print(output)

if __name__=="__main__":
	Main()
