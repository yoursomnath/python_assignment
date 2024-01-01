# Write a Python class to reverse a string word by word. 

class StringReverser:
    def reverse_words(self, input_string):
        words = input_string.split()
        reversed_words = words[::-1]
        reversed_string = ' '.join(reversed_words)
        return reversed_string

# Example usage:
reverser = StringReverser()

# Reverse words in a string
input_str = "Hello World"
result_str = reverser.reverse_words(input_str)

print(f"Original String: {input_str}")
print(f"Reversed String: {result_str}")
