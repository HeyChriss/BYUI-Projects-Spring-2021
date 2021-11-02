# import random
# 
# Game = "yes"
# while Game == "yes":
#     Number = random.randint(1, 100)
#     Count = 0
#     guess = -1
# 
#     while guess != Number:
#         guess = int(input("What is your guess? "))
#         Count = Count + 1
# 
#         if guess < Number:
#             print("Higher")
#         elif guess > Number:
#             print("Lower")
#         else:
#             print("You guessed it!")
# 
#     print(f"You did {Count} guesses, the number was {Number}")
#     Game = input("Would you like to play again (yes/no)? ")
# print("Thank you for playing.")

value = 20
while value < 20:
   value = value + 1
print(value)