#number guessing game
import random
import time

print("""
**********************

Number Guessing Game
Guess numbers from 1 to 40.

*************************""")

random_number=random.randint(1,40)
guess_right=5

while True:

    number=int(input("please enter number "))

    if (number < random_number):
        print("loading ...")
        time.sleep(1)

        print("please enter  larger number.")
        guess_right -=1
    elif (number > random_number):
        print("loading ...")
        time.sleep(1)

        print("please enter smaller number.")  
        guess_right -=1
    else:
        print("loading ...")
        time.sleep(1)

        print("Tebriks. You guessed right !",random_number)
        break
    if(guess_right==0):
        print("Your guess is over")
        print("Correct number is ",random_number)







