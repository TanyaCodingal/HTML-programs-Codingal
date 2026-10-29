sunny=0
rainy=0

weather=(0,1,0,0,0,1,1,1,1,1,0,0,0,0,0)

for i in weather:
    if i==0:
        sunny+=1
    else:
        rainy+=1

if sunny>rainy:
    print("The weather will be sunny today☀️")
else:
    print("The weather will be rainy today🌧️")