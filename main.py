import random

def get_choices():
    person_choice = input("Enter a Choice:(rock, paper, scissors)")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {"person" : person_choice, "computer" : computer_choice}
    return choices

choices = get_choices()
print(choices)