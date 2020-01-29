import random
r=random.randrange(1,100)
print("You have five chances")
guess = int(input("Enter your guess between 1 to 100"))
for i in range(4):
    if guess>r:
        print("Your guess is too high")
        print("try again")
        guess = int(input("Enter your guess"))
    elif guess<r:
        print("Your guess is too low")
        print("try again")
        guess = int(input("Enter your guess"))
    else:
        print("You WIN")
        break
print("Game Over")
