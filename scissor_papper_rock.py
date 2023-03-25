import random

user_wins = 0
computer_wins = 0
options =  ["scissor","paper","rock"]

while True:
    user_input = input("Type Scissor/Paper/Rock or Q to Quit").lower()
    if user_input == "q":
       break

    if user_input not in options:
        continue 
        
    random_number = random.randint(0,2)
    # scissor 0,paper 1,rock2

    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")

    if user_input =="rock" and computer_pick =="scissor":
        print("YOU WON!")
        user_wins += 1
        continue
    if user_input =="paper" and computer_pick =="scissor":
        print("YOU WON!")
        user_wins += 1
        continue
    if user_input =="scissor" and computer_pick =="paper":
        print("YOU WON!")
        user_wins += 1
        continue
    if user_input =="paper" and computer_pick =="rock":
        print("YOU WON!")
        user_wins += 1
        continue
    else:
        print("YOU LOST!")
        computer_wins += 1

print("YOU WON",user_wins, "times.")
print("COMPUTER WON",computer_wins, "times.")
print ("TQ GOOD BYE!")
