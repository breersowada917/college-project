import random

def get_random_integer(start, end):
    return random.randint(start, end)

def get_random_float(start, end):
    return random.uniform(start, end)

def get_random_string(length):
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890') for i in range(length))

def get_random_boolean():
    return random.choice([True, False])