import random
lives=5
secret=random.randint(1,50)
print("Guess the SECRET Number.... if you can 🤭")
print("❤️ ❤️ ❤️ ❤️ ❤️")
while lives<=5 and lives>=0:
    guess=int(input("Enter number :"))
    if guess!=secret:
        for i in range(1,lives):
            print("❤️",end=" ")
        lives=lives-1
        if guess<secret:
            print("\nEnter a higher number.")
        elif guess>secret:
            print("\nEnter a lower number.")
    else:
        print("Well done! The secret number was",secret)
        break
    if lives==0:
        print("You LOST! The secret number was",secret)
        break