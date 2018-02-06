#to know about files "r-read" , "w-write", "r+ - read and write" 
#to know about stripping i.e., line.strip('\n \r')

def Main():
	f = open("myfile.txt", 'w') #to use write mode
	for i in range(4):
	#we are using "for" loop because python knows how many lines are in the file
		f.write(input("please enter a word: ") + '\n')
		print(line.strip()) #we used stripping here to clear the unwanted spaces
	f.close() #to close our file

if __name__=="__main__":
	Main()
