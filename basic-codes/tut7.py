#to know about files "r-read" , "w-write", "r+ - read and write" 
#to know about stripping i.e., line.strip('\n \r')
#using with , with automatically closes the book

def Main():
	words = ['cat','bat','mat','rat']
	with open("myfile.txt", 'w') as f:
		for word in words:
			f.write(word + '\n')
	

if __name__=="__main__":
	Main()
