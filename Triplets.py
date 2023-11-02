def find_triplet_with_sum(numbers, target_sum):
    n = len(numbers)

    # Sort the list to make it easier to find triplets
    numbers.sort()

    # Initialize a result list to store triplets
    triplets = []

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = numbers[i] + numbers[left] + numbers[right]

            if current_sum == target_sum:
                triplets.append([numbers[i], numbers[left], numbers[right]])
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return triplets

# Given list of numbers and target sum
numbers = [10, 20, 30, 9]
target_sum = 59

# Find the triplets with the given sum
triplets = find_triplet_with_sum(numbers, target_sum)

if triplets:
    print("Triplets with sum", target_sum, "are:")
    for triplet in triplets:
        print(triplet)
else:
    print("No triplets found with the sum", target_sum)
