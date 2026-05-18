def my_ieee_2_dec(ieee):
    sign_bit = int(ieee[0])
    exponent_bits = ieee[1:12]
    fraction_bits = ieee[12:]

    exponent = 0
    for bit in exponent_bits:
        exponent = exponent * 2 + int(bit)

    fraction = 0
    for i in range(len(fraction_bits)):
        fraction += int(fraction_bits[i]) * (2 ** (-(i + 1)))

    bias = 1023

    sign = (-1) ** sign_bit

    d = sign * (1 + fraction) * (2 ** (exponent - bias))

    return d

ieee ="1100000001001000000000000000000000000000000000000000000000000000"
print(my_ieee_2_dec(ieee))

ieee ="0100000000001011001100110011001100110011001100110011001100110011"
print(my_ieee_2_dec(ieee))