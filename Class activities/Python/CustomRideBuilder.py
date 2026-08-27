print("=== CUSTOM RIDE BUILDER ===")
print("Bike - 1 \nCar - 2")

choice1=int(input("Enter your choice : "))

if choice1==1:
    print("Scooty - 1 \nMountain Bike - 2")
    choice2=int(input("Enter your choice :"))

    if choice2==1:
        print("\nVehicle chosen : Scooty")
        print("Top speed      : 80 km/h")
        print("Best for       : City roads")

    elif choice2==2:
        print("\nVehicle chosen : Bike")
        print("Top speed      : 40 km/h")
        print("Best for       : Offroad trails")

    else:
        print("INVALID INPUT")

elif choice1==2:
    print("SUV - 1 \nSwift - 2")
    choice2=int(input("Enter your choice :"))
    
    if choice2==1:
        print("\nVehicle chosen     : SUV")
        print("Passengers allowed : 7")
        print("Best for           : Adventures")
    
    elif choice2==2:
        print("\nVehicle chosen      : Swift")
        print("Passengers  allowed : 4")
        print("Best for            : Family outings")
    
    else:
        print("INVALID INPUT")

else:
    print("INVALID CHOICE!!")

print("\n=============================================")
print("            Your custom ride is ready!!\n            Enjoy your trip!!")
print("\n=============================================")