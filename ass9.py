# Write a python program to calculate the length of a string without using a
# library function. 

def calculate_string_length(input_string):
    length = 0

    for _ in input_string:
        length += 1

    return length

# Example usage:
input_str = "Hello, World!"
string_length = calculate_string_length(input_str)

print(f"The length of the string is: {string_length}")
