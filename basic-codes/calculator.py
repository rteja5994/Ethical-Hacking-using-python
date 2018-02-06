#This is my first calculator program

#To add two numbers:
def add(x,y):
	return x+y

#To subtract two numbers:
def sub(x,y):
	return x-y

#To multiply two numbers:
def mul(x,y):
	return x*y

#To divide two numbers:
def div(x,y):
	return x/y

print("please select the required option you need to perform.")
print("1.Add")
print("2.subtract")
print("3.multiply")
print("4.subtract")

#to take the inputs from the user
choice = input("Enter choice(1/2/3/4): ")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == '1':
	print(num1, "+", num2,"=", add(num1,num2))

elif choice == '2':
	print(num1, "-", num2,"=", sub(num1,num2))

elif choice == '3':
	print(num1, "*", num2,"=", mul(num1,num2))

elif choice == '4':
	print(num1, "/", num2,"=", div(num1,num2))

else 
	print("Invalid input given")
