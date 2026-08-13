name=input("Enter agent name : ")
gadget=input("Enter favourite gadget : ")
number=7
rating=9.5
missions=12
height=1.74
isActive=True

print("Agent Name : ",name," Type : ",type(name))
print("Favourite Gadget : ",gadget," Type : ",type(gadget))
print("Agent ID : ",number," Type : ",type(number))
print("Agent Rating : ",rating," Type : ",type(rating))
print("Missions Completed : ",missions," Type : ",type(missions))
print("Agent Height : ",height," Type : ",type(height))
print("Agent Status : ",isActive," Type : ",type(isActive))

numberstr=str(number)
ratingstr=str(rating)
heightstr=str(height)
missionsstr=str(missions)

print("Agent ID in text : ",numberstr," Type : ",type(numberstr))
print("Agent Ratings in text : ",ratingstr," Type : ",type(ratingstr))
print("Agent Height in text : ",heightstr," Type : ",type(heightstr))
print("Agent Missions in text : ",missionsstr," Type : ",type(missionsstr))

ftl=name[0:3]
ll=name[-1]
agentName=ftl+ll

print("First three letters : ",ftl)
print("Last letter : ",ll)
print("Code Name : ",agentName)

revGad=gadget[::-1]#reverse any string
print("Reversed gadget name : ",revGad)

print("\n")
print("======================================================================")
print(" AGENT "+agentName.upper())
print(" ID "+numberstr)
print(" SPEED "+numberstr)
print(" MISSION "+missionsstr)
print(" IS ACTIVE : ",isActive)
print("SECRET GADGET CODE : "+revGad.upper())
print("======================================================================")