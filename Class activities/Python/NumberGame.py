import random

print("======Number Guessing Game======")
print("RULES :\n⭐Enter JUST the number : No decimals, letters or symbols\n⭐Range -> 1-15 : The number can be anywhere between this\n⭐You have THREE guesses. Any more won't be entertained.")
print("HAVE FUNN!!\n")


num=random.randint(1,15)
lives=3

guess=int(input("Enter your guess :"))
while True:
    if guess==num:
        print("You have guessed the number 🥳")
        break

    elif guess<num:
        print("The number's a BIT higher 🤭")
        lives-=1

    elif guess>num:
        print("A number of a little lesser value 🤭")
        lives-=1

    elif lives==0:
        print("Oops!! You ran out of guesses 😭😭")
        print("The number was",num)
        break

    guess=int(input("Enter your guess :"))