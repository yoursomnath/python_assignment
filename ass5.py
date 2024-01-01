# Write a Python program to calculate the average of numbers in a given list
def calculate_average(numbers):
    if not numbers:
        return None  # Return None for an empty list

    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return average

# Example usage:
number_list = [10, 20, 30, 40, 50]
average_result = calculate_average(number_list)

if average_result is not None:
    print(f"The average of the numbers is: {average_result}")
else:
    print("The list is empty, cannot calculate the average.")
