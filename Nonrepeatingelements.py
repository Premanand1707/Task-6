def first_non_repeating_element(numbers):
    # Create a dictionary to store the frequency of each element
    frequency = {}

    # Iterate through the list and count the frequency of each element
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Find the first non-repeating element
    for num in numbers:
        if frequency[num] == 1:
            return num

    # If no non-repeating element is found, return None
    return None

# Example list of integers
numbers = [1, 2, 3, 2, 1, 4, 5, 4, 6]

# Find the first non-repeating element
result = first_non_repeating_element(numbers)

if result is not None:
    print("The first non-repeating element is:", result)
else:
    print("No non-repeating elements found in the list.")
