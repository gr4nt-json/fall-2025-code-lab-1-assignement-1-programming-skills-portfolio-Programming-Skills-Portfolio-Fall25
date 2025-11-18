#Sets the correct password
correct_password = "12345"

#Asks the user for the password
password = str(input("Input password: "))

#The number of attempts
attempts = 5

#Repeats if the entered password is wrong AND there is more than 1 attempt left
while password != correct_password and attempts > 1:
    #Subtracts the number of attempts by one if the user is wrong
    attempts = attempts - 1
    #Ask the user to try again, while showing the remaining attempts
    password = str(input(f"Wrong password, you have {attempts} attempts left: "))

#After the loop, checks one last time if the password is still wrong
if password != correct_password:
    #User fails
    print("0 attempts left. You will go to jail.")
else:
    #Password is correct
    print("Password is correct.")
