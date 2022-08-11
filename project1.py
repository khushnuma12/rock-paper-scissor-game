import random
user=input("enter your choice(rock,paper,scissor):")
possible_choice=["rock","paper","scissor"]
computer_action=random.choice(possible_choice)
print(f"\n you choose {user},opponent choose {computer_action}.\n")

if user==computer_action:
    print(f"\n both player selected{user}it's Tie\n")
elif user=="rock":
        if computer_action=="scissor":
             print("rock breaks scissor!you win")
        else:
            print("paper cover rock!you loss")
elif user=="paper":
        if computer_action=="rock":
             print("paper cover rock!you win")
        else:
            print("scissor cuts paper!you loss")
elif user=="scissor":
        if computer_action=="paper":
            print("scissor cuts paper!you win")
        else:
            print("rock breaks scissor!you loss")
