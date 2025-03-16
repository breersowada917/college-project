import random

def get_random_code(length=10):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return ''.join(random.choice(alphabet) for _ in range(length))