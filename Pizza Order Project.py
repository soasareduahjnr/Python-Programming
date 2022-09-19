print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")



if size == "S":
  bill = 15
elif size == "M":
  bill = 20
elif size == "L":
  bill = 25
  
if add_pepperoni == "Y":
  if bill == 15:
    bill += 2
  elif bill == 20 or 25:
    bill += 3
else:
  bill += 0
  print ("Kindly input a valid pepperoni request code.")
  
if extra_cheese == "Y":
  bill +=1
  print (f"Your final bill is: ${bill}.")
elif extra_cheese == "N":
  print (f"Your final bill is: ${bill}")
else:
  print ("Kindly input a valid extra cheese request code.")