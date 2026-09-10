print("===ATM Cash Dispenser===")
t100=t50=t20=t10=t5=t1=0

cserved=0
tdispensed=0

serving=True
while serving==True:
    name=input("Enter your name :")
    amt=int(input("Enter Withdrawal Amount :"))
    if amt<=0:
        print("Please give a valid amount.")
        continue
    print("Dispensing",amt,"for",name)
    remaining=amt
    ix=1
    while ix<=6:
        if ix==1:
            value=100
        elif ix==2:
            value=50
        elif ix==3:
            value=20
        elif ix==4:
            value=10
        elif ix==5:
            value=5
        else:
            value=1
        count=remaining//value
        if count>0:
            print(count,"multiplied by",value,"unit note(s) :",count*value)
            remaining-=count*value
            if value==100:
                t100+=count
            elif value==50:
                t50+=count
            elif value==20:
                t20+=count
            elif value==10:
                t10+=count
            elif value==5:
                t5+=count
            else:
                t1+=count
        ix+=1
        cserved+=1
        tdispensed+=amt

    print("Transaction completed. Hope you come back soon,",name)
    again=input("Is there another customer in the queue (yes/no) :").strip().lower()
    if again!="yes":
        serving=False
        break

print("\n\n====Daily Domination Report====")
for i in range(1,7):
    if i==1:
        value,total=100,t100
    elif i==2:
        value,total=50,t50
    elif i==2:
        value,total=20,t20
    elif i==2:
        value,total=10,t10
    elif i==2:
        value,total=5,t5
    else:
        value,total=1,t1
    if total>0:
        print(value,"unit notes dispensed :",total)

print("Customer Served :",cserved)
print("Total Dispensed :",tdispensed)