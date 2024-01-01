# Write a Python program to read a list of words and return the length of the
# longest one. 
def find_longest_word_length(word_list):
    if not word_list:
        return 0  # Return 0 for an empty list

    longest_length = len(word_list[0])

    for word in word_list[1:]:
        current_length = len(word)
        if current_length > longest_length:
            longest_length = current_length

    return longest_length

# Example usage:
word_list = ["apple", "banana", "grape", "kiwi", "orange"]
longest_length = find_longest_word_length(word_list)

print(f"The length of the longest word is: {longest_length}")

