#nested dictionaries
#.get(),.getitems()

studentData={
    19:{"name":"Sri Sai Arya","subject":"Civics","marks":89},
    20:{"name":"Tanya","subject":"English","marks":98},
    21:{"name":"Vismay","subject":"Math","marks":95},
    22:{"name":"Yeelena","subject":"Science","marks":99}
}
print(studentData)

studentData[23]={"name":"Pakhi","subject":"Hindi","marks":"100"}
print(studentData)

studentData[21]["subject"]="Geography"
print(studentData)

studentData.pop(19)
print(studentData)

print(len(studentData))