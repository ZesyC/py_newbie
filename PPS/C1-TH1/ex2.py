def my_dec_2_bin(d):
    a = []
    while d > 0:
        i = d % 2
        a.append(i)
        d //= 2
    a.reverse()
    return a

print(my_dec_2_bin(0))
print(my_dec_2_bin(23))
print(my_dec_2_bin(2097))