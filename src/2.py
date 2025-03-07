import random

def get_random_code(length):
    code = ''
    for i in range(length):
        code += chr(random.randint(65, 90))
    return code
