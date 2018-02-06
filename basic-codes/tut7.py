#to know about files

def Main():
	f = open("myfile.txt", 'r')
	for line in f:
	#we are using "for" loop because python knows how many lines are in the file
		print(line)
	f.close() #to close our file

if __name__=="__main__":
	Main()
