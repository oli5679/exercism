from string import ascii_lowercase

def is_isogram(string):
    chars = [c.lower() for c in string if c.lower() in ascii_lowercase]
    return len(chars) == len(set(chars)) 