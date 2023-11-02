# Given list of numbers
numbers = [10.501, 22, 37, 100, 999, 87, 351]

# Initialize empty lists to store even and odd numbers
even_numbers = []
odd_numbers = []

# Loop through the numbers in the given list
for num in numbers:
    # Check if the number is even
    if num % 2 == 0:
        even_numbers.append(num)
    # If the number is not even, it's considered odd
    else:
        odd_numbers.append(num)

# Print the lists of even and odd numbers
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
