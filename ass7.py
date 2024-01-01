# Write a python program to create a list of tuples with the first element as
# the number and second element as the square of the number. 

def create_tuples(n):
    tuple_list = [(num, num**2) for num in range(1, n + 1)]
    return tuple_list

# Example usage:
number_limit = 5
result_list = create_tuples(number_limit)

print("List of Tuples:")
for tpl in result_list:
    print(tpl)
