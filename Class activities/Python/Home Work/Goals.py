print("=====PERSONAL GOALS DISPLAY=====")
import keyword
name=input("Enter your name: ")
goal =input("Enter one skill you want to get better at: ")
target=input("Enter the month you want to reach it by: ")
practice=30
print("\nMY PERSONAL GOAL PLAN\n")
print("Name :",name)
print("Goal:",goal)
print("Target month :",target)
print("Daily practice :",practice,"minutes")
print("Status : Not Started")
print("Reminder - Practice Every Day!")


# ---------- PART 7: the sentence and the keywords ----------
# YOUR CODE HERE
print(name,"plans to work on",goal,"for",practice,"minutes every day until",target)
print("\nWords Python has reserved for itself :")
print(keyword.kwlist)