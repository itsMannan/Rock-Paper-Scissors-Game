import random

def get_choices():
    person_choice = input("Enter a Choice:(rock, paper, scissors)")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {"player" : person_choice, "computer" : computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose: {player} \nComputer chose: {computer}")
    if player == computer:
        return "It's a Tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock Smashes Scissors! You Win!"
        else:
            return "Paper Covers Rock! You lose." 
    elif player == "paper":
        if computer == "rock":
            return "Paper covers Rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock Smashes Scissors! You lose."
        
choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)

