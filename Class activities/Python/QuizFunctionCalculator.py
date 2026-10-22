print("\n\n=====Welcome to my Python Quiz II Section C CALCULATOR PROGRAM!!=====")
print("#DISCLAIMER : Bigger number will be operated upon by the smaller number wherever necessary\n")

#Defining 4 functions : Addition, Subtraction, Multiplication and Division
def Addition(n1,n2):
    return n1+n2

def Subtraction(n1,n2):
    return n1-n2

def Multiplication(n1,n2):
    return n1*n2

def Division(n1,n2):
    return n1/n2

try:
    #Inputs from user
    n1=float(input("Enter the bigger number :"))
    n2=float(input("Enter the smaller number :"))

    #if-elif for defs
    op=input("\nEnter the operation you wish to perform on the entered numbers(with correct spellings) :").lower()
    if op=="addition":
        aTotal=Addition(n1,n2)
        print("\nOPERATION PICKED :",op,"\nTOTAL RECEIVED :",aTotal)

    elif op=="subtraction":
        sTotal=Subtraction(n1,n2)
        print("\nOPERATION PICKED :",op,"\nTOTAL RECEIVED :",sTotal)

    elif op=="multiplication":
        mTotal=Multiplication(n1,n2)
        print("\nOPERATION PICKED :",op,"\nTOTAL RECEIVED :",mTotal)
    
    elif op=="division":
        dTotal=Division(n1,n2)
        print("\nOPERATION PICKED :",op,"\nTOTAL RECEIVED :",dTotal)

    print("Thanks for running the program and spending your precious time here!! ❤️")

except ValueError:
    print("Oops! That was not a number 😅")

except ZeroDivisionError:
    print("Oops! You can't divide a number with zero 😅")