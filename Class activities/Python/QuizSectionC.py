'''Number Guessing Game

Build a game where the computer picks a secret number between 1 and 50. You have 5 attempts to guess it.
After every wrong guess your program shows a hint telling you how close you are. Remaining lives are shown as hearts after each attempt.
💡 Hint: Store your secret number in a variable — for example: secret = 27
If you already know the random module, feel free to use it! This test checks your logic (conditions, loops, input/output).
What you need to use
------------------------------------------------------------------------
1.  int(input())       →  to read the player's guess
2.  while loop         →  stops after 5 attempts or when player wins
3.  if/elif/else       →  hint system —
🧊 ice cold, 🥶 cold, 🌡️ warm, or 🔥 hot
4.  for loop           →  shows 
remaining ❤️ hearts
after each wrong guess
5.  win/loss message   →  reveals the secret number if attempts run out
------------------------------------------------------------------------
What you'll be marked on
------------------------------------------------------------------------
1.  Program runs without any errors                          →   5 marks
2.  int(input()) used to read the player's guess             →   5 marks
3.  while loop stops after 5 attempts or on correct guess    →  10 marks
4.  Hint system prints ice cold / cold / warm / hot          →  10 marks
5.  for loop shows correct hearts after each wrong guess     →   5 marks
6.  Win message shown / secret revealed if attempts run out  →   5 marks
========================================================================
Total  →  40 marks
========================================================================'''

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