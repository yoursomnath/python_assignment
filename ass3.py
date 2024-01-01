# Write a Python class to implement pow(x, n).

class PowerCalculator:
    def pow(self, x, n):
        if n < 0:
            x, n = 1 / x, -n
        result = 1
        while n:
            if n % 2:
                result *= x
            x, n = x * x, n // 2
        return result

# Example usage:
calculator = PowerCalculator()

# Calculate power: 2^3
base, exponent = 2, 3
result = calculator.pow(base, exponent)

print(f"{base}^{exponent} = {result}")
