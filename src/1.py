  import random

def get_random_code(length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(length):
        result += random.choice(letters)
    return result