def factorial(num):
	if num==1:
		return 1
	elif num==0:
		return 0
	else:
		fact=num*factorial(num-1)
		return fact




num=int(input("Enter a number: "))
if(num>=0):
	print(factorial(num));
else:
	print("This input is invalid")
