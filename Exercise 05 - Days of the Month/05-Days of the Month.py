#Dictionary mapping each month number to its number of days
monthday = {
    1: 31,
    2: [28, 29],
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

#Asks the user for a month number
month = int(input("Input a month number: "))

#If the chosen month is February
if month == 2:
    #Variable to control the validation loop
    invalid = 1
    #The loop continues until the user inputs a valid answer
    while invalid == True:
        leap = str(input("Is it a leap year? (yes or no): "))
        leap = leap.lower()  #Makes the input lowercase

        #If the user says yes, February has 29 days
        if leap == "yes":
            print("There are 29 days in the month.")
            invalid = False
        #If the user says no, February has 28 days
        elif leap == "no":
            print("There are 28 days in the month.")
            invalid = False
        #Asks the user to try again if input is invalid
        else:
            print("Invalid input, try again")

#Prints the number of days
else:
    print(f"There are {monthday[month]} days in the month.")
