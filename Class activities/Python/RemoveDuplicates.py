studentData={
    "id1":{"name":"ABCD","class":"8","favSubject":"english,math,science"},
    "id2":{"name":"EFGH","class":"8","favSubject":"english,math,science"},
    "id3":{"name":"IJKL","class":"8","favSubject":"english,math,science"},
    "id4":{"name":"ABCD","class":"8","favSubject":"english,math,science"}
}
result={}
seenKeys=[]

for i,j in studentData.items():
    uniqueKey=(j["name"],j["class"],j["favSubject"])
    if uniqueKey not in seenKeys:
        seenKeys.append(uniqueKey)
        result[i]=j

for k,v in result.items():
    print(k,":",v)