n1=int(input("Enter the first integer : "))
n2=int(input("Enter the second integer : "))
n3=int(input("Enter the third integer : "))

if n1>n2 and n1>n3:
    print(n1," is the greater number among them.")

elif n2>n1 and n2>n3:
    print(n2," is the greater number among them.")

elif n3>n1 and n3>n2:
    print(n3," is the greater number among them.")

else:
    print("None of them are greater.")