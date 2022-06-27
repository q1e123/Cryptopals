import binascii

def xor_repeting_key(a, key):
    text = a
    repetitions = 1 + (len(text) // len(key))
    key = key * repetitions
    key = key[:len(text)]

    # XOR text and key generated above and return the raw bytes
    return bytes([b ^ k for b, k in zip(text, key)])

message_list = [
    b"Burning 'em, if you ain't quick and nimble",
    b"I go crazy when I hear a cymbal"
]
check_list = [
    '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272',
    'a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
]
key = b'ICE'

for message, check in zip(message_list, check_list):
    secret = xor_repeting_key(message, key)
