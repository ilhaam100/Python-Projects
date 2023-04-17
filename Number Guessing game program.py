'''Number guessing game'''

from random import randint

n = randint(1,100)
user_input = input("Enter a number between 1 and 100 \n To exit the game enter any letter: ")

while True:
    if user_input.isdigit():
      user_input = int(user_input)       
      if user_input < n:
        print("Too low")
        user_input = input("Enter a number between 1 and 100 \n To exit the game enter any letter: : ")
      elif user_input > n:
        print("Too high")
        user_input = input("Enter a number between 1 and 100 \n To exit the game enter any letter: : ")
      else:
        print("You've guessed it right! Bye")
        break
    else:
        print(f'The correct number is {n}')
        break
