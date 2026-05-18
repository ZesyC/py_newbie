def my_bin_2_dec(b):
    d = 0

    for i in range(len(b)):
        a = b[-1 - i]
        d += a * (2 ** i)

    return d


def my_dec_2_bin(d):
    b = []

    while d > 0:
        i = d % 2
        b.append(i)
        d //= 2

    b.reverse()
    return b


d = my_bin_2_dec(my_dec_2_bin(12654))
print(d)

print("Có!")