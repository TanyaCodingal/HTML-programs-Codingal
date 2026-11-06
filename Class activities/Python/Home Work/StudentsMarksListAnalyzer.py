l1=[]
print(l1)

marks=[85,72,90,66,78]
print("Student marks :",marks)

sample=[10,20,30]*2
print("Repeated list :",sample)

print("Entries :",len(marks))

print("First entry :",marks[0])
print("Last entry :",marks[-1])

firstThree=marks[0:3]
print("First three entries :",firstThree)

reversed=marks[::-1]
print("Reversed entries :",reversed)

def Match(markS):
    count=0
    matched=[]
    #----------
    for mark in markS:
        markT=str(marks)
        #----------
        if len(markT)>1 and markT[0]==markT[-1]:
            count+=1
            matched.append(mark)
            #----------
    print("Entries with flipflop digits :",matched)
    return count
#----------
sameCount=Match([88,72,99,65,77])
print("Number of flipflop entries :",sameCount)

total=0
#----------
for mark in marks:
    total+=mark
#----------
average=total/len(marks)
#----------
print("Sum of marks :",total)
print("Average marks :",average)

marks.sort()
#----------
print("Lowest marks :",marks[0])
print("Highest marks :",marks[-1])

print("\nSTUDENT MARKS LIST ANALYZER \nSorted marks :",marks,"\nTotal marks :",total,"\nAverage :",average,"\nLowest marks :",marks[0],"\nHighest marks :",marks[-1])