import random

print("=========================Rock Paper Scissor Game V/S a Computer : Can you outsmart it??=========================")
print("RULES:\n⭐Entirely the same as a regular rock-paper-scissors game\n⭐This game plays by the rules and does not have an inbuilt program to automatically win\n⭐HAVE FUN!\n")

lis=["rock","paper","scissors"]

cMove=random.choice(lis)
uMove=input("Enter your move :").lower()

if cMove==uMove:
    print("It's a draw. Too bad.")
elif cMove=="rock" and uMove=="paper":
    print("You win! Congrats!")
elif cMove=="paper" and uMove=="scissors":
    print("You win! COngrats!")
elif cMove=="scissors" and uMove=="rock":
    print("You win! Congrats!")
else:
    print("Computer wins! Tough luck.")

print("Your move :",uMove)
print("Computer's move :",cMove)