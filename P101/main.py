
import random
rollAgain = input("Would you like to roll a D6? (yes/no) ")
if rollAgain.lower() == "yes":
    rollAgain = True 
elif rollAgain.lower() == "no":
    rollAgain = False

dice = [" "]*9

while rollAgain == True:
  dice = [" "]*9
  num = random.randint(1,6)
  print(num)
  if num == 1:
    dice[4] = "•"
  elif num == 2:
    dice[0] = "•"
    dice[8] = "•"
  elif num == 3:
    dice[0] = "•"
    dice[4] = "•"
    dice[8] = "•"
  elif num == 4:
    dice[0] = "•"
    dice[2] = "•"
    dice[6] = "•"
    dice[8] = "•"
  elif num == 5:
    dice[0] = "•"
    dice[2] = "•"
    dice[4] = "•"
    dice[6] = "•"
    dice[8] = "•"
  elif num == 6:
    dice[0] = "•"
    dice[2] = "•"
    dice[3] = "•"
    dice[5] = "•"
    dice[6] = "•"
    dice[8] = "•"  
  print(" _____")
  print('|' + dice[0] + ' ' + dice[1] + ' ' + dice[2] + '|')
  print('|' + dice[3] + ' ' + dice[4] + ' ' + dice[5] + '|')
  print('|' + dice[6] + ' ' + dice[7] + ' ' + dice[8] + '|')
  print(" ‾‾‾‾‾")
  userInput = input("Do you want to roll again? (yes/no) ")
  if userInput.lower() == "yes":
    rollAgain = True 
  elif userInput.lower() == "no":
    rollAgain = False
print("Thank you for rolling!")