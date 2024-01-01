# Write a python program to count the number of vowels and consonants in
# a string. 

def count_vowels_and_consonants(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

# Example usage:
input_str = "Hello World"
vowels, consonants = count_vowels_and_consonants(input_str)

print(f"The number of vowels: {vowels}")
print(f"The number of consonants: {consonants}")

