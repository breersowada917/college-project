import random

def get_random_code(n):
    alphabet = "0123456789abcdef"
    code = ""
    for i in range(n):
        code += random.choice(alphabet)
    return code