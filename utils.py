def number_to_bits_array(value, size):
    bits_array = []

    for i in reversed(range(size)):
        bit = (value >> i) & 1
        bits_array.append(bit)

    return bits_array


def is_even(val):
    return val % 2 == 0


def set_bit(value, bit):
    
    if (value & 1) == bit:
        value ^= 1

    return value

# def get_bits():
#     pass