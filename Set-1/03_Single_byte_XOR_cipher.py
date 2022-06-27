import binascii
from collections import Counter
from queue import PriorityQueue

def single_byte_xor(text, key):
    return bytes([ch ^ key for ch in text])

def get_fitting_quotient(text, language_frequency_dictionary):
    language_frequency_list = list(language_frequency_dictionary.values())
    counter = Counter(text)
    text_frequency = [
        (counter.get(ord(ch), 0) * 100) / len(text) for ch in language_frequency_dictionary
    ]
    absolute_frequency_difference_list = [abs(a-b) for a,b in zip(text_frequency, language_frequency_list)]
    return sum(absolute_frequency_difference_list) / len(language_frequency_list)

def get_decoded_heap(text, language_frequency_dictionary):
    decoded_heap = PriorityQueue()
    for key in range(256):
        decoded = single_byte_xor(secret, key)
        fitting_quotient = get_fitting_quotient(decoded.lower(), language_frequency_dictionary)
        priority = fitting_quotient
        decoded_heap.put((priority, decoded))
    return decoded_heap

language_frequency_english = {
    'a': 8.2389258,    'b': 1.5051398,    'c': 2.8065007,    'd': 4.2904556,
    'e': 12.813865,    'f': 2.2476217,    'g': 2.0327458,    'h': 6.1476691,
    'i': 6.1476691,    'j': 0.1543474,    'k': 0.7787989,    'l': 4.0604477,
    'm': 2.4271893,    'n': 6.8084376,    'o': 7.5731132,    'p': 1.9459884,
    'q': 0.0958366,    'r': 6.0397268,    's': 6.3827211,    't': 9.1357551,
    'u': 2.7822893,    'v': 0.9866131,    'w': 2.3807842,    'x': 0.1513210,
    'y': 1.9913847,    'z': 0.0746517
}


secret = binascii.unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
decoded_heap = get_decoded_heap(secret, language_frequency_english)
while(not decoded_heap.empty()):
    item = decoded_heap.get()
    priority = item[0]
    message_bytes = item[1]
    try:
        message = message_bytes.decode()
        print(priority, message)
    except:
        continue