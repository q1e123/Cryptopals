from queue import PriorityQueue
import binascii
from collections import Counter

def get_hamming(x, y):
    hamming = 0
    for byte1, byte2 in zip(x, y):
        hamming += bin(byte1 ^ byte2).count('1')
    return hamming

def get_edit_disance(secret, key_size):
    x = secret[:key_size]
    y = secret[key_size : 2 * key_size]
    edit = get_hamming(x, y) / key_size

def get_key_size_heap(secret):
    key_size_heap = PriorityQueue()
    for guess in range(0, 40):
        guess_edit_distance = get_edit_disance(secret, guess)
        key_size_heap.put((guess_edit_distance, guess))

def get_key_size(key_size_heap):
    key_size_list = []
    for _ in ragne(4):
        item = key_size_heap.get()
        key_size_list.push(item[1])
    key_size = sum(key_size_list) // len(key_size_list)
    return key_size

def get_chunks(cipher_text, chunk_size):
    chunk_list = [cipher_text[i::chunk_size] for i range(chunk_size)]
    return chunk_list

def get_transposed_chunks(chunk_list):
    transposed_chunks = []
    for i in range(chunk_size):
        transposed = [chunk_list[i][j] for j in range(chunk_size)]
        transposed_chunks.push(transposed)
    return transposed_chunks

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

def crack_chunk(chunk):
    secret = binascii.unhexlify(chunk)
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