import random

print("Rock Paper Scissors Game")

while True:
  
  print("Enter your choice \n 1. Rock \n 2. Paper \n 3. Scissors \n")
  
  choice = int(input("User turn: "))

  while choice > 3 or choice < 1:
    choice = int(input("Enter valid input: "))
        
  if choice == 1:
    choice_name = 'Rock'
  elif choice == 2:
    choice_name = 'Paper'
  else:
    choice_name = 'Scissors'

  print("User choice is: " + choice_name)
  print("\nNow its computer turn.......")

  comp_choice = random.randint(1, 3)
  
  while comp_choice == choice:
    comp_choice = random.randint(1, 3)

  if comp_choice == 1:
    comp_choice_name = 'Rock'
  elif comp_choice == 2:
    comp_choice_name = 'Paper'
  else:
    comp_choice_name = 'Scissors'

  print("Computer choice is: " + comp_choice_name)

  print(choice_name + " V/s " + comp_choice_name)

  if((choice == 1 and comp_choice == 2) or
     (choice == 2 and comp_choice ==1 )):
    print("Paper wins => ", end = "")
    result = "Computer"

  elif((choice == 1 and comp_choice == 3) or
       (choice == 3 and comp_choice == 1)):
    print("Rock wins =>", end = "")
    result = "User"
  else:
    print("Scissors wins =>", end = "")
    result = "Computer"

  if result == "Computer":
    print("<== Computer wins ==>")
  else:
    print("<== User wins ==>")

  print("Do you want to play again? (Y/N)")
  ans = input()


  if ans == 'n' or ans == 'N':
    break

print("\nThanks for playing")
