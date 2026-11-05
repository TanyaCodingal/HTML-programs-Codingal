demo={"chocolates":7,"snacks":6,"iceCream":6,"bananas":7,"apples":7}

print("Original dictionary :",demo)

k=7

res=0
for i in demo:
    if demo[i]==k:
        res+=1

print("Frequency of",k,"in dictionary is",res)