print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


love_score = 0

lower_name1 = name1. lower()
lower_name2 = name2. lower()

T_times_name1 = lower_name1. count ("t")
R_times_name1 = lower_name1. count ("r")
U_times_name1 = lower_name1. count ("u")
E_times_true_name1 = lower_name1. count ("e")
L_times_name1 = lower_name1. count ("l")
O_times_name1 = lower_name1. count ("o")
V_times_name1 = lower_name1. count ("v")
E_times_love_name1 = lower_name1. count ("e")

T_times_name2 = lower_name2. count ("t")
R_times_name2 = lower_name2. count ("r")
U_times_name2 = lower_name2. count ("u")
E_times_true_name2 = lower_name2. count ("e")
L_times_name2 = lower_name2. count ("l")
O_times_name2 = lower_name2. count ("o")
V_times_name2 = lower_name2. count ("v")
E_times_love_name2 = lower_name2. count ("e")

sum_true = str(T_times_name1+R_times_name1+U_times_name1+E_times_love_name1+T_times_name2+R_times_name2+U_times_name2+E_times_love_name2)
sum_love = str(L_times_name1+O_times_name1+V_times_name1+E_times_love_name1+L_times_name2+O_times_name2+V_times_name2+E_times_love_name2)


love_score = int(sum_true + sum_love)

if love_score < 10 or love_score > 90:
  print (f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print (f"Your score is {love_score}, you are alright together.")
else:
  print (f"Your score is {love_score}.")
