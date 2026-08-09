name="Tanya"
account=10234
balance=50000
print("Name : ",name)
print("Account no : ",account)
print("Bank Balance : Rs.",balance)
withdraw=int(input("Enter the amount to be withdrawn from your bank account : "))
balance-=withdraw
print("You have Rs",balance," in your bank account now")
deposit=int(input("Enter the amount to be deposited into your bank account : "))
balance+=deposit
print("You have Rs.",balance," in yout bank account now")