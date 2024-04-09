def sort_numbers_from_input():
    # Ask the user to input numbers separated by spaces
    input_str = input("Enter numbers separated by spaces: ")

    # Split the input string into a list of strings representing numbers
    numbers_str = input_str.split()

    # Convert the list of strings to a list of integers
    numbers = [int(num) for num in numbers_str]

    # Sort the list of numbers
    sorted_numbers = sorted(numbers)

    return sorted_numbers

# Call the function to get sorted numbers from user input
sorted_numbers = sort_numbers_from_input()

# Print the sorted numbers
print("Sorted Numbers:", sorted_numbers)

