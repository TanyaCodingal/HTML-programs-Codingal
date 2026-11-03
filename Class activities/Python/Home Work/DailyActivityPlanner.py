print("=====Daily Activity Planner=====")

hwTime=int(input("Enter the homework time in minutes :"))

if hwTime>60:
    plan="start homework now"
    print("That is a long homework session.")
else:
    plan="finish homework quickly"
    print("Thai is a short homework session.")

fTime=input("Is there free time after homework (yes/no) :").lower()
if fTime=="yes":
    print("Pick a hobby soon.")

print("===== DAILY PLAN =====")
print("HOMEWORK MINUTES :",hwTime,"\nPLAN :",plan,"\nFREE TIME :",fTime)