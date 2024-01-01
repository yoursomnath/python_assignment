# Write a Python class to convert an integer to a roman numeral. 
class IntegerToRoman:
    def __init__(self):
        self.map = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
                    50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    def to_roman(self, n):
        if not(1 <= n <= 3999): raise ValueError("Input must be 1 to 3999")
        result = ""
        for v, r in sorted(self.map.items(), key=lambda x: x[0], reverse=True):
            while n >= v: result, n = result + r, n - v
        return result

# Example usage:
converter = IntegerToRoman()
number, roman = 3549, converter.to_roman(3549)
print(f"The Roman numeral for {number} is: {roman}")
