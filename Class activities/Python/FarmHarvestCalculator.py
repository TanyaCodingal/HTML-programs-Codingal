f1=int(input("Enter the weight of the harvest from the first farm in kgs : "))
f2=int(input("Enter the weight of the harvest from the second farm in kgs : "))
f3=int(input("Enter the weight of the harvest from the third farm in kgs : "))
f4=int(input("Enter the weight of the harvest from the fourth farm in kgs : "))
f5=int(input("Enter the weight of the harvest from the fifth farm in kgs : "))

total1=f1+f2+f3+f4+f5
avg1=total1/5

print("Total Harvest this year: ",total1)
print("Average of the Total Harvest this year per farm : ",avg1)

PricePerKg=25
totalEarnings1=total1*PricePerKg
print("Total Earnings this year : ",totalEarnings1)

bags=total1//25
leftoverHarvest1=total1%25

print("Total bags used (1 bag=25kg harvest) : ",bags)
print("Leftover Harvest : ",leftoverHarvest1)

total2=500
print("Better than last year's harvest : ",total1>total2)
print("Worse than last year's harvest : ",total1<total2)
print("Same as last year's harvest : ",total1==total2)

total1-=60

print("Total harvest after saving grains for next harvest : ",total1)
print("Final total bags used to pack grains : ",total1//25)
print("Final amount of grains left after packing : ",total1%25)