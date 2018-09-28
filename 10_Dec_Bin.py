
dec = 11
# print(bin(dec))
# print(oct(dec))
# print(hex(dec))

def dec_other(num, other):
    l = []
    if num < 0:
        return '-' + dec_other(abs(num), other)
    while True:
        num, remainder = divmod(num, other)
        l.append(str(remainder))
        if num == 0:
            return ''.join(l[::-1])

def count_1(num):
    if num > 0:
        return dec_other(num, 2).count('1')
    else:
        return 32 - dec_other(abs(num), 2).count('1')

print(count_1(-11))

# print(dec_other(dec, 2))
# print(dec_other(dec, 8))