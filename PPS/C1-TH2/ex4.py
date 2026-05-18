def my_bin_adder(b1, b2):
    b = []
    c = 0

    i = len(b1) - 1
    j = len(b2) - 1

    while i >= 0 or j >= 0 or c > 0:
        if i >= 0:
            x = b1[i]
        else:
            x = 0

        if j >= 0:
            y = b2[j]
        else:
            y = 0

        t = x + y + c

        bit = t % 2
        c = t // 2

        b.append(bit)

        i -= 1
        j -= 1

    b.reverse()
    return b


print(my_bin_adder([1, 1, 1, 1, 1], [1]))
print(my_bin_adder([1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 0]))
print(my_bin_adder([1, 1, 0], [1, 0, 1]))