# Write a python program to store 100 numbers in to file.txt and check
# whether the number if Odd then store into odd.txt and Even number store
# into even.txt

import random

def generate_numbers_and_store():
    # Generate 100 random numbers
    numbers = [random.randint(1, 1000) for _ in range(100)]

    # Write numbers to numbers.txt
    with open('numbers.txt', 'w') as numbers_file:
        for number in numbers:
            numbers_file.write(f"{number}\n")

    # Separate odd and even numbers
    odd_numbers = [num for num in numbers if num % 2 != 0]
    even_numbers = [num for num in numbers if num % 2 == 0]

    # Write odd numbers to odd.txt
    with open('odd.txt', 'w') as odd_file:
        for odd_number in odd_numbers:
            odd_file.write(f"{odd_number}\n")

    # Write even numbers to even.txt
    with open('even.txt', 'w') as even_file:
        for even_number in even_numbers:
            even_file.write(f"{even_number}\n")

if __name__ == "__main__":
    generate_numbers_and_store()
    print("Numbers stored in numbers.txt, odd numbers in odd.txt, and even numbers in even.txt.")
