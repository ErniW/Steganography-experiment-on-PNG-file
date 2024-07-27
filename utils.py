def is_even(val):
    return 1 if val % 2 == 0 else 0

def set_bit(value, bit):
    return value | bit

def to_bits_array(value, size):
    bits_array = []
    
    for i in reversed(range(size)):
        bit = (value >> i) & 1
        bits_array.append(bit)
    
    return bits_array
