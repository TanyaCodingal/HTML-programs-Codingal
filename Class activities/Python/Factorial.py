def Factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*Factorial(n-1)

print("Factorial of 0 :",Factorial(0))
print("Factorial of 1 :",Factorial(1))
print("Factorial of 2 :",Factorial(2))
print("Factorial of 3 :",Factorial(3))
print("Factorial of 4 :",Factorial(4))
print("Factorial of 5 :",Factorial(5))