# Function to find the sum of the first and last digits of an integer
def sum_of_first_and_last_digit(number):
    # Convert the integer to a string to easily extract digits
    num_str = str(number)
    
    # Extract the first and last digits
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    
    # Calculate the sum of the first and last digits
    total = first_digit + last_digit
    
    return total

# Input an integer
num = int(input("Enter an integer: "))

# Calculate the sum of the first and last digits
result = sum_of_first_and_last_digit(num)

# Print the result
print("Sum of the first and last digits:", result)
