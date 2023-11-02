# Function to check if a number is a happy number
def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

# Given list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Initialize a variable to count happy numbers
happy_count = 0

# Loop through the numbers in the given list
for num in numbers:
    if is_happy_number(num):
        happy_count += 1

# Print the count of happy numbers
print("Count of Happy Numbers:", happy_count)
