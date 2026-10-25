def match(word):
    c=0
    lst=[]
    for i in word:
        if len(i)>1 and i[0]==i[-1]:
            c+=1
            lst.append(i)
    print("List with same first and last letters :",lst)
    return c

tLen=match(["tanya","anika","mom","ash"])
print(tLen)