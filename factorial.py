#Calculate the factorial of a number
#factorial of n=1*2*3*4*.....(n-1)*n
num=int(input("Enter a number: "))
fact=1
for i in range(1,num+1):
	fact=fact*i
print("The factorial of the number is:",fact)

