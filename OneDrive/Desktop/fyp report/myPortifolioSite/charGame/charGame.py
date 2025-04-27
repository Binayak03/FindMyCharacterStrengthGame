import random, os,time 

def diceRoll(side):
  result = random.randint(1, side)
  return result

def health():
  healthStat = ((diceRoll(6) * diceRoll(12)/2)+10 )
  return healthStat 

def strength():
  charStrength = ((diceRoll(6) * diceRoll(8)/2)+12 )
  return charStrength



while True:

  print("******Find Your Charater Strength******")

  name = input("Enter character name: ")
  char = input("""WHat is your character's type??
    1. Human
    2 Elf
    3. Monster
    4. Wizard\n""")
  print()
  if char == "Human" or char == "human" or char == "elf" or char    == "Char" or char == "monster" or char == "Monster" or char ==    "wizard" or char == "Wizard":
     
      print("Hello", name, "Your Character type is ", char)
      print("Your Health is: ", health())
      print("Your Strength is: ", strength())
      print()
  else:
      print("Unknown Character Type, Please run the program again")
      print()

  again = input("do you want to play again? ")
  if again =="yes" or again == "y":
    continue
  else: 
    print("Bye")
    break

time.sleep(3)
os.system('clear')
    