import random

low = int(input("Pick the lowest number in range: "))
high = int(input("Pick the highest number in range: "))
n = random.randint(low, high)
guess = int(input("Enter a number: "))
while True:
  if guess < n:
    print ("Guess is low!")
    guess = int(input("Enter a number: "))
  elif guess > n:
    print ("Guess is high!")
    guess = int(input("Enter a number: "))
  else:
    print ("You guessed it!")
    break
