def IsEqual(CTwi, Tw):
    # Get the length of the arrays
    m = len(CTwi)
    
    # Initialize the result array
    result = []
    
    # Iterate over each element of the arrays
    for i in range(m):
        # Convert the characters to integers
        CTwi_bit = int(CTwi[i])
        Tw_bit = int(Tw[i])
        
        # Compute the product (1 + CTwi_bit + Tw՛_bit) modulo 2
        prod_mod_2 = (1 + CTwi_bit + Tw_bit) % 2
        
        # Append the result to the output list
        result.append(prod_mod_2)
    
    return result


# Given numbers
CTw = 73636214
Tw = 42533

# Convert the numbers to binary strings
CTw_binary = bin(CTw)[2:]  # Remove '0b' prefix
Tw_binary = bin(Tw)[2:]    # Remove '0b' prefix

# Ensure that both binary strings have the same length by padding with zeros if necessary
max_len = max(len(CTw_binary), len(Tw_binary))
CTw_binary = CTw_binary.zfill(max_len)
Tw_binary = Tw_binary.zfill(max_len)

print(CTw_binary)
print(Tw_binary)

# Example usage
CTwi = [0, 1, 0, 1, 1]
Tw = [1, 0, 1, 0, 1]
m = IsEqual(CTw_binary, Tw_binary)
print(m)
