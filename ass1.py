# Write a python program to put even and odd elements in a list into two
# different lists. 

def separate_even_odd(input_list):
    even_list = []
    odd_list = []

    for num in input_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    return even_list, odd_list

# Example usage:
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers, odd_numbers = separate_even_odd(input_list)

print("Original List:", input_list)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
