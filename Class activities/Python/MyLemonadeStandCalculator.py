'''1. Greet the customer (name, greeting)
   2. Ask -> number of lemonades ordered
   3. Calculate the total cost
   4. Print final receipt
   5. Print a personalised thank-u msg'''

name=input("What's your name :")
price=60
total=0 

def greet():
    print("Hey",name,"\nWelcome to my Lemonade Stand!")
    print("Buy freshly made lemonade, just for you!")
greet()

print("\nThe price of a lemonade is",price,"INR.")
quantity=int(input("Enter the number of lemonades you wish to buy :"))

def Total(price,quantity):
    total=price*quantity
    return total
finalCost=Total(price,quantity)

print("\nYou will have to pay",finalCost,"INR.")
paid=int(input("Enter the amount paid by you :"))
def Change(fc,p):
    change=paid-finalCost
    return change
c=Change(finalCost,paid)

def Bill(name,quantity,finalCost,paid,c):
    print("\n=================================================================")
    print("                         CANDY'S LEMONADE")
    print(" Name              :",name)
    print(" Item              : Lemonade")
    print(" Quantity          :",quantity)
    print(" Cost of lemonades :",finalCost)
    print(" Amount paid       :",paid)
    print(" Change received   :",c)
    print("===================================================================\n")   
Bill(name,quantity,finalCost,paid,c)

print("Thanks for visiting my lemonade stall,",name,"\nHave a great day!")