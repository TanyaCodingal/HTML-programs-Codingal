try:
    n1=int(input("Enter num 1 :"))
    n2=int(input("Enter num 2 :"))
    print(n1/n2)
    print("TrY StAtEmEnT")

except ValueError:
    print("Value Error - Exception Handled")

except ZeroDivisionError:
    print("Zero Division Error - Exception Handled")

except:
    print("Exception Handled")

print("****************************")