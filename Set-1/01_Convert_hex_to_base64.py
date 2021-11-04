import base64
import binascii

hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
check = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

hex_bytes = binascii.unhexlify(hex_string)
base_64_string = base64.b64encode(hex_bytes)

if base_64_string == check:
    print('OK')
else:
    print('WRONG')
    print(base_64_string)
    print(check)
