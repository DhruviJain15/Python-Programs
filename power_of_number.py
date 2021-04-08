#2 raised to 3=2*2*2=2*power(2,exponent-1)
def power(base,exponent):
    if(exponent==0):
        return 1
    elif (exponent==1):
        return base
    else:
        return(base*power(base,(exponent-1)))
base=int(input("Enter the base: "))
exponent=int(input("Enter the exponent: "))
p=power(base,exponent)
print(p)