temp=int(input("Enter the temperature : "))
if temp<=20:
    outfit="Jacket"
    print("It's cold outside, wear a ",outfit)
else:
    outfit="T-shirt"
    print("It's warm outside, wear a ",outfit)

rain=input("Is it raining (yes/no) : ").lower()
if rain=="yes":
    print("Take an umbrella, it is raining")

windSpeed=int(input("Enter the speed of the wind in kmph : "))
if windSpeed>=30:
    windNeed="yes"
    print("It is very windy, wear a windbreaker over your ",outfit)
else:
    windNeed="no"
    print("No windbreaker needed over your ",outfit)

puddles=input("Are there puddles (yes/no) : ").lower()
if puddles=="yes":
    shoes="Gumboots"
    print("You need to wear ",shoes," as there are puddles everywhere")
else:
    shoes="Sneakers"
    print("As there are no puddles, you can wear ",shoes)

print("\n\nWeather Check Complete!")
print("=== WEATHER OUTFIT PICKER ===")
print("Temperature:",temp)
print("Outfit chosen:",outfit)
print("Rain status:",rain)
print("Windbreaker needed:",windNeed)
print("Shoes chosen:",shoes)