def exact_match(a, b):
    """
    Perform an exact match comparison between two binary strings a and b.

    Args:
    - a: Binary string representing the first input.
    - b: Binary string representing the second input.

    Returns:
    - 1 if the strings are equal, 0 otherwise.
    """
    # Ensure the lengths of the strings are the same
    if len(a) != len(b):
        raise ValueError("The lengths of the input strings must be equal")

    # Initialize the result variable
    result = 1

    # Iterate over each index
    for i in range(len(a)):
        # Compute the value of (1 + a[i] + b[i]) modulo 2
        value = (1 + int(a[i]) + int(b[i])) % 2
        
        # Multiply the result by the calculated value
        result *= value

    return result

# Example usage
a = "101011"
b = "101011"
print("Exact match result:", exact_match(a, b))
