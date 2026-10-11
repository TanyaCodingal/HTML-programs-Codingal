#Calculate change function
def Change(paid,price):
    change=paid-price
    return change

#Initialising variables and warning consumer of accepted values
print("==========Snack Vending Machine=========")
print("All packets of chips cost 25 INR. COins of 1,5,10 and 25 INR only is accepted.\n")

total=0
coinNo=0
price=25

#User enters amount (infinitely) till price is fulfilled
while True:
    coin=int(input("Enter coin value (e.g.:1) :"))
    if coin!=1 and coin!=5 and coin!=10 and coin!=25:
        print("Your coin was rejected as it was of an invalid amount. Please retry.")
        continue

    total+=coin
    coinNo+=1

    print("So far you have inserted",coinNo,"coins and paid",total,"INR.")

    #if inserted price is greater than total price, break the loop
    if total>=price:
        print("\nYou have inserted enough money. Hang on...")
        break

flavour=input("What flavour of chips do you want from my vending machine :")

#Call calculate change function and pass 
changePending=Change(total,price)

#if change is zero, pass. Else, print a msg
if changePending==0:
    pass
else:
    print("\nYour change has been ejected.")

#print the bill
print("\nHere is your bill :")
print("\n===============Happy Crunches Vending Machine===============")
print("Chips flavour            :",flavour)
print("Cost of chips            :",price)
print("Number of coins received :",coinNo)
print("Amount paid              :",total)
print("Change received(if any)  :",changePending)
print("Signature                : 🛜🌏🔐")
print("===============Thank You and Have a Nice Day!===============")