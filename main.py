import random

def get_choices():
    person_choice = input("Enter a Choice:(rock, paper, scissors)")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {"person" : person_choice, "computer" : computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose: {player} \nComputer chose: {computer}")
    if player == computer:
        return "It's a Tie!"
    elif player == "rock" and computer == "scissors":
        return "Boom Player's Rock smashes Computer Scissors! You Win!"
    elif player == "rock" and computer == "paper":
        return "Sorry! Computer Paper covers Person's Rock! You Lose."

choices = check_win('rock', 'paper')



"""Concept of if and elif(else if) statement"""
# age = 20

# if age >= 18:
#     print("Your an Adult.")
# elif age >=12:
#     print("You're a Teenager.")
# elif age>=1:
#     print("You're a Child.")
# else:
#     print("You're a Baby.")

"""For Testing the {def get_choices()} function"""
# choices = get_choices() 
# print(choices)