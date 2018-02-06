#iteration
#use of for and while loops
#use of turtles and drawing a square is perfect example to learn iteration

def Main():
	for step in range(5):
		print(step)

	words = ['cat','bat','hat','rat','sat']
	#the above words is an example of list

	for word in words:
		print(word)
	
	num = 0
	while num <= 0:
		num = int(input("please enter a positive integer: "))

if __name__=="__main__":
	Main()
