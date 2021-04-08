#Program to calculate highest common factor(hcf) using recursion
#Logic:hcf(64,36)=64 mod 36=28
#      hcf(36,28)=36 mod 28=8
#      hcf(28,8)=28 mod 8=4
#      hcf(8,4)=8 mod 4=0
#Hence hcf=4
#hcf(a,b)=hcf(b,a mod b)
#base condition: hcf(a,0)=a
def hcf(a,b):
    if(a<0):
        a=-1*a
        #converting negative numbers to positive because gcd of negative and positive no. is same
    if(b<0):
        b=-1*b
    if(b==0):
        return a
    else:
        return hcf(b,a%b)
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
h=hcf(a,b)
print(h)