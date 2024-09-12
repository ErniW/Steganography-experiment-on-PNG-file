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

def get_message_length(image):
    length = 0

    for i in range(16):
        bit = is_even(image[i * 3])
        length = (length << 1) | bit

    return length

def get_message(image, length):
    message = ""

    current_value = 16 * 3

    for char_index in range(length):

        char = 0

        for _ in range(8):

            bit = is_even(image[current_value])
            char = (char << 1) | bit

            current_value += 3

        message += chr(char)

    return message
    