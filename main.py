def get_choices():
    person_choice = input("Enter a Choice:(rock, paper, scissor)")
    computer_choice="paper"
    choices = {"person" : person_choice, "computer" : computer_choice}
    return choices

choices = get_choices()
print(choices)