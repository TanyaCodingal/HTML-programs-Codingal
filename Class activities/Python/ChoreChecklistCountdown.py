total=4
og=total


print("You have",og,"chores left to complete.")
comp=0
num=1


while num<=total:

    if num==1:
        next="Make your bed"
    elif num==2:
        next="Water the plants"
    elif num==3:
        next="Get ready for school"
    else:
        next="Go to school"

    ans=input("Have you completed the chore (yes/no) :").lower()
    if ans=="yes":
        comp+=1
        num+=1
        print("Great job!! You completed the chore 🥳")
    else:
        print("Complete the chores to get an EXTRA SPECIAL REWARD")

    print("Remaining chores :",total-comp,"\n")


print("🎆⭐ALL CHORES COMPLETED🎆")
print("Amazing job!!\n")


print("==CHORE CHECKLIST SUMMARY==")
print("Chores assigned today :",4)
print("Chores completed :",comp)
print("Chores remaining :",total-comp)


#print("========INFINITE LOOPS IN PYTHON========")
test=0
safety=0
while test<=0:
    print("I n f i n i t e  l o o p ")
    safety+=1
    if safety==3:
        break
