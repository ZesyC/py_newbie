def int_to_bin(n, length):
    bits = ""

    while n > 0:
        bits = str(n % 2) + bits
        n //= 2

    while len(bits) < length:
        bits = "0" + bits

    return bits


def hex_digit_to_bin(h):
    table = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "a": "1010",
        "b": "1011",
        "c": "1100",
        "d": "1101",
        "e": "1110",
        "f": "1111"
    }

    return table[h]


def my_dec_2_ieee(d):
    d = float(d)

    if d == 0:
        return "0" * 64

    if d < 0:
        sign = "1"
        d = -d
    else:
        sign = "0"

    h = d.hex()

    parts = h.split("p")
    number_part = parts[0]
    exponent = int(parts[1])

    biased_exponent = exponent + 1023
    exponent_bits = int_to_bin(biased_exponent, 11)

    fraction_hex = number_part.split(".")[1]

    fraction_bits = ""
    for digit in fraction_hex:
        fraction_bits += hex_digit_to_bin(digit)

    while len(fraction_bits) < 52:
        fraction_bits += "0"

    fraction_bits = fraction_bits[:52]

    ieee = sign + exponent_bits + fraction_bits

    return ieee
d = 1.518484199625
print(my_dec_2_ieee(d))

d = -309.141740
print(my_dec_2_ieee(d))

d = -25252
print(my_dec_2_ieee(d))