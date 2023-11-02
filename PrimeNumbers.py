# Given list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Initialize a list to store prime numbers
prime_numbers = []

# Initialize a variable to count prime numbers
prime_count = 0

# Loop through the numbers in the given list
for num in numbers:
    if is_prime(num):
        prime_numbers.append(num)
        prime_count += 1

# Print the count of prime numbers and the list of prime numbers
print("Count of Prime Numbers:", prime_count)
print("Prime Numbers:", prime_numbers)
