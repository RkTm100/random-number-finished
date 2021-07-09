import random
#winner=random.randint(1,9)

chance=0

print("Number guessing game")
winner=random.randint(1,9)
print(winner)

while chance<5:
  guess=int(input("What is the number: "))

  if guess==winner:
    print("you Win")
    break
  elif   guess<winner:
    print("Incorrect, try again. Guess a number higher than " + str(guess))
    
  else:
    print("Incorrect, try again. Guess a number lower than " + str(guess))
  chance=chance+1
  if  chance==5:
    print("You lose, the correct number is:  " + str(winner))
    
