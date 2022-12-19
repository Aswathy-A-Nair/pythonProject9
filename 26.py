def computeGCD(a,b):
    if b==0:
        return a
    else:
        return computeGCD(b,a%b)
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print(computeGCD(num1,num2))