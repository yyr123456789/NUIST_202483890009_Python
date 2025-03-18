# Add Two Numbers in Python
# Author:fanchenxuan
# Using a function

# function to add two numbers
def add(a,b):
	#converting input to float and adding	
	res=float(a)+float(b)
	return res

#taking user input
a=input("First number: ")
b=input("Second number: ")
result=add(a,b)
print("the answer is ",result)
