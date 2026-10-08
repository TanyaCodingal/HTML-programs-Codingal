def calcBill(food,drinks,dessert):
    total=food+drinks+dessert
    print("Total bill :",total)

def seatingArrangement(numPeople):
    if numPeople==0 or numPeople==1:
        return 1
    else:
        return numPeople*seatingArrangement(numPeople-1)

calcBill(2000,500,1000)
print("Number of possible seating arrangements :",seatingArrangement(4))
