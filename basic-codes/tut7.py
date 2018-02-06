#to know about files "r-read" , 
#to know about stripping i.e., line.strip('\n \r')

def Main():
	f = open("myfile.txt", 'r')
	for line in f:
	#we are using "for" loop because python knows how many lines are in the file
		print(line.strip()) #we used stripping here to clear the unwanted spaces
	f.close() #to close our file

if __name__=="__main__":
	Main()
