row=int(input("Enter the number of rows :"))

if row%2==0:
    halfDiamond=int(row/2)
else:
    halfDiamond=int(row/2)+1
space=halfDiamond-1

#Upper half
for i in range(1,halfDiamond+1):
    for j in range(1,space+1):
        print(end=" ")
    space=space-1
    num=1
    for j in range(2*i-i):
        print(end=str(num))
        num=num+1
    print()

space=1

#Lower half
for i in range(1,halfDiamond):
    for j in range(1,space+1):
        print(end=" ")
    space=space+1
    num=1
    for j in range(1,2*(halfDiamond-i)):
        print(end=str(num))
        num=num+1
    print()