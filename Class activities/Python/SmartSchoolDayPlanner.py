print("===============Smart School Day Planner===============")
day=input("Enter the day (Monday-Friday) : ").strip().lower()
weather=input("Enter the weather (Rainy/Sunny/Cloudy) : ").strip().lower()
hw=input("Homework completed (yes/no) : ").strip().lower()

print("\nDAY PLANNER FOR",day.upper())

if day in ("saturday","sunday"):
    print(" DAY : WEEKEND")
elif day=="monday":
    print(" DAY : FIRST DAY OF SCHOOL")
elif day=="friday":
    print(" DAY : LAST DAY OF SCHOOL")
elif day in ("tuesday","wednesday","thursday"):
    print(" DAY : REGULAR SCHOOL DAY")

if weather=="sunny" and hw=="yes":
    print(" After school, you may go down and play")
if weather=="sunny" and hw=="no":
    print(" After school you must finish your homework")

if weather=="cloudy" or weather=="rainy":
    if hw=="yes":
        print(" You may go down to play but you must take an umbrella")
    if hw=="no":
        print(" You must complete your homework")

if day in ("saturday","sunday"):
    if weather=="sunny":
        print("It's the perfect day to go on an outing!!")