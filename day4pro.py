rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

 
user_pick =int(input("pick 0 for rock 1 for paper 2 for scissors \n"))

if user_pick > 2: 
    print("number not valid")

else:
    import random
    hands = [rock,paper,scissors]
    compt_pick = random.randint(0,2)
    print(f"computer picked {hands[compt_pick]}")
    print(f"you picked {hands[user_pick]}")
    if user_pick ==  compt_pick  :
        print("its a draw")
    elif user_pick == 0 and compt_pick == 1 :
        print("computer win 🤣😂😂🤣🤣😜")
    elif user_pick == 1 and compt_pick == 0 :
        print("you win")
    elif user_pick == 0 and compt_pick == 2 :
        print("you win")
    elif user_pick == 2 and compt_pick == 0 :
        print("computer win 🤣😂😂🤣🤣😜")
    elif user_pick == 1 and compt_pick == 2 :
        print("computer win 🤣😂😂🤣🤣😜")
    elif user_pick == 2 and compt_pick == 1 :
        print("you win")

