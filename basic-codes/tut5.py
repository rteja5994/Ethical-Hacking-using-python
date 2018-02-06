#to use functions and why main functions is used in programming

def getinteger(prompt):
	#we used prompt to use pass by reference
	result = int(input(prompt))
	return result

def Main():
	print("Started")
	output = getinteger("Please enter an integer:")
	print(output)

if __name__=="__main__":
	Main()
