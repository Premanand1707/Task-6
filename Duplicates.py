# Define three example lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
list3 = [6, 7, 8, 9, 10]

# Initialize sets to store unique elements and duplicates
unique_elements = set()
duplicates = set()

# Iterate through the first list
for item in list1:
    if item in unique_elements:
        duplicates.add(item)
    else:
        unique_elements.add(item)

# Iterate through the second list
for item in list2:
    if item in unique_elements:
        duplicates.add(item)
    else:
        unique_elements.add(item)

# Iterate through the third list
for item in list3:
    if item in unique_elements:
        duplicates.add(item)
    else:
        unique_elements.add(item)

# Convert the set of duplicates to a list for better formatting
duplicates_list = list(duplicates)

# Print the list of duplicates
print("Duplicates in the three lists:", duplicates_list)
