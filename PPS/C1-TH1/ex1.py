def my_bin_2_dec(b):
    d = 0

    for i in range (len(b)):
        a = b[-1 - i]
        d += a * (2 ** i)
    return d

print(my_bin_2_dec([1, 1, 1]))
print(my_bin_2_dec([1, 0, 1, 0, 1, 0, 1]))
print(my_bin_2_dec([1]*25))

