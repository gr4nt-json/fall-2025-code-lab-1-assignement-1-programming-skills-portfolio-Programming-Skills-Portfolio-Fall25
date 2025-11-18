#The number of questions
questions_left = 10

#The loop continues if there are questions left
while questions_left > 0:

    #Assigns the country and its capital
    if questions_left == 10:
        capital = "France"
        correct_answer = "paris"
    elif questions_left == 9:
        capital = "United Kingdom"
        correct_answer = "london"
    elif questions_left == 8:
        capital = "Germany"
        correct_answer = "berlin"
    elif questions_left == 7:
        capital = "Italy"
        correct_answer = "rome"
    elif questions_left == 6:
        capital = "Spain"
        correct_answer = "madrid"
    elif questions_left == 5:
        capital = "Netherlands"
        correct_answer = "amsterdam"
    elif questions_left == 4:
        capital = "Switzerland"
        correct_answer = "bern"
    elif questions_left == 3:
        capital = "Greece"
        correct_answer = "athens"
    elif questions_left == 2:
        capital = "Portugal"
        correct_answer = "lisbon"
    else:
        capital = "Sweden"
        correct_answer = "stockholm"

    #Decrease the number of questions left by 1 at the end of each loop
    questions_left = questions_left - 1

    #Asks the user for the capital of the given country
    answer = input(f"What is the capital of {capital}? ")
    answer = answer.lower()

    #Checks if the user's answer matches the correct one
    if answer == correct_answer:
        answer = answer.capitalize()  #Proper format for display
        print(f"{answer} is correct")
    else:
        print(f"{answer} is wrong")