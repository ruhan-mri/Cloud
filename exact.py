def is_equal(a, b):
    """
    Check if two binary strings a and b are equal.

    Args:
    - a: Binary string represented as a list of bits.
    - b: Binary string represented as a list of bits.

    Returns:
    - True if a and b are equal, False otherwise.
    """
    # Ensure both binary strings have the same length
    mu = min(len(a), len(b))
    
    # Initialize the result variable
    result = 1

    # Iterate over each bit position
    for i in range(mu):
        # Compute the value of (1 + a[i] + b[i]) modulo 2
        value = (1 + a[i] + b[i]) % 2
        print(value)
        
        # Multiply the result by the computed value
        result *= value

    # If the result is 0, the strings are equal; otherwise, they are not equal
    return result == 0

# Example usage
a = [1, 0, 1, 1]  # Example binary string a
b = [1, 1, 0, 1]  # Example binary string b
equal = is_equal(a, b)
print("Are the binary strings equal?", equal)
