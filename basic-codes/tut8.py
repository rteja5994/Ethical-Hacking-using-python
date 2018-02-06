#exceptions
"""
 	try:
		do stuff here
	except:
		do this if try is failed
	finally:
		do this first two cases failed """

def Main():
	try:
		f = open("xyz.txt","r")
		for line in f:
			print(line.strip())
		f.close()
	except:
		print("The file you are trying to open does not exist")

	finally:   
	#finally always executes and prints 
		print("Exiting")

if __name__=="__main__":
	Main()
