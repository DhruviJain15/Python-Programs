#Program to calculate factorial
#5=1*2*3*4*5=120
#n=1*2*3.....*(n-1)*n
num=int(input("Enter a number: "))
if(num>=0):
	fact=1
	for i in range(1,num+1):
		fact=fact*i
	print("The factorial is",fact)
else:
	print("The number entered is invalid")

