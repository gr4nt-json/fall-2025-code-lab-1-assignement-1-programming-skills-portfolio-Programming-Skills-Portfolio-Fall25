#Function to determine if a number is even or odd
def check_odd_even(number):
    if number / 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

#Main function
def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    
    # Pass the number to the function and get the result
    result = check_odd_even(num)
    
    # Print the result
    print(result)

#Executes the main function
main()
