from string import ascii_letters
import re

def abbreviate(words):
    allowed = set(ascii_letters + ' -')
    clean_word = ''.join([char for char in words if char in allowed])
    return ''.join([x[0].upper() for x in re.split('-| ',clean_word) if len(x) > 0])
