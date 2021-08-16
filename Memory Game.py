import random
import time
import os
score = 0
def game(score):
  print("Your Score Is Currently {}.".format(score))
  words = ["dog", "cat", "rat", "rhino", "bear", "zebra", "bison", "bull", "ram", "iguana", "lizard", "parrot", "porcupine", "armadillo", "gecko", "penguin", "owl", "racoon", "skunk", "fox", "grasshopper", "butterfly", "frog", "toad", "cockroach", "whale", "panda", "wolverine", "tadpole", "otter", "tiger", "lion", "wolf", "worm", "earthworm", "coyote", "ant", "beetle", "woodpecker", "squirrel", "lemur", "fish", "salmon"]
  outputWords = ""
  for i in range(5):
    x = random.choice(words)
    outputWords = outputWords + x + " "
  print(outputWords)
  loop = 11
  for i in range(10):
    loop -= 1
    print(loop)
    time.sleep(1)
  os.system("clear")
  answer = input("Type: ")
  answer = answer.strip()
  if answer == outputWords.strip():
    print("You Win!!!")
    score =+ 1
    print("Your Score Is Now {}".format(score))
  else:
    print("The Correct Answer Was {}".format(outputWords))
  again = input("Would You Like To Play Again(y/n): ")
  again = again.lower()
  if again == "y":
    game(score)
  elif again == "n":
    print("Thank You For Playing!")
  else:
    print("Invalid Input, Try Again")
game(score)
