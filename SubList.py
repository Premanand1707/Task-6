def has_sublist_with_zero_sum(numbers):
    # Create a set to store cumulative sums
    cumulative_sum_set = set()
    cumulative_sum = 0

    # Iterate through the list
    for num in numbers:
        cumulative_sum += num

        # If the cumulative sum is zero or has been seen before, there is a sub-list with a sum of zero
        if cumulative_sum == 0 or cumulative_sum in cumulative_sum_set:
            return True

        # Add the cumulative sum to the set
        cumulative_sum_set.add(cumulative_sum)

    # If the loop completes without finding a sub-list with zero sum, return False
    return False

# Given list of numbers
numbers = [4, 2, -3, 1, 6]

# Check if there is a sub-list with a sum of zero
result = has_sublist_with_zero_sum(numbers)

if result:
    print("There is a sub-list with a sum of zero.")
else:
    print("There is no sub-list with a sum of zero.")
