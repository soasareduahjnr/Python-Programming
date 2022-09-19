print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 



print ("Your mission is to find not just any treasure but a long lost treasure of old which has been spoken of for many eons.")
first_decision = input("You are currently at a decision-making crossroad, and it's up to you to decide. Where do you want to go? Type \"left\" or \"right\"? \n").lower()
if first_decision == "left":
  second_decision = input ("You've now come to a lake and can sight an Island in the middle of the lake. Type \"wait\" to wait for a boat or \"swim\" if you want to swim across to the Island? \n").lower()
  if second_decision == "wait":
    third_decision = input ("Your patience paid off, and your boat has now arrived.\nYou have been sailed to the Island unharmed and you now face a house with 3 doors of different colors; red, yellow and blue.... \nType the color of door you would like to go through? \n").lower()
    if third_decision == "yellow":
      print ("You are a genius! How did you guess right?\nAs a matter of fact, you found the Long Lost Treasure you've been searching for! Way to go camp :)")
    elif third_decision == "red":
      print ("Sorry, it's Game Over for you because you just got burnt into a crisp by the dragon that protects the treasure by opening that door :(")
    elif third_decision == "blue": 
      print ("Sorry, it's Game Over for you because you just opened door to the room of carnivorous trolls :(")
  else:
      print ("Sorry, it's Game Over for you!\nLittle did you know that the lake was full of sharks which used you for sumptuous meal :(")
else:
      print ("Sorry, it's Game Over for you! \n You fell into a ditch :(")