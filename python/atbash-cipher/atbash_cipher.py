import string


def atbash_map(str):
    mapping = {}
    reversed_chars = string.ascii_lowercase[::-1]
    valid_chars = string.ascii_lowercase + '0123456789'

    for i, char in enumerate(string.ascii_lowercase):
        mapping[char] = reversed_chars[i]

    for char in  '0123456789':
        mapping[char] = char
    
    return ''.join([mapping[x.lower()] for x in str if x.lower() in valid_chars])

def encode(plain_text):
    mapped = atbash_map(plain_text)
    return ' '.join([mapped[i:i+5] for i in range(0, len(mapped), 5)])
    
 
    
def decode(ciphered_text):
    return atbash_map(ciphered_text)
