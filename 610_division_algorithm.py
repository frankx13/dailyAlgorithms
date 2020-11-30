# This question was asked by ContextLogic.
# Implement division of two positive integers without using the division, multiplication, or modulus operators.
# Return the quotient as an integer, ignoring the remainder.

def divide(dividend, divisor):
    quotient = 0

    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    return quotient


print(divide(1555, 200))  # Return 7
print(divide(100, 10))  # Return 10
print(divide(50, 1))  # Return 50
