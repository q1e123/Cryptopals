import binascii


def xor(a, b):
    result = bytes([x^y for x, y in zip(a,b)])
    return result

string_1 = binascii.unhexlify('1c0111001f010100061a024b53535009181c')
string_2 = binascii.unhexlify('686974207468652062756c6c277320657965')
check = binascii.unhexlify('746865206b696420646f6e277420706c6179')
xored = xor(string_1, string_2)

if xored == check:
    print('OK')
else:
    print('WRONG')
    print(xored, check)