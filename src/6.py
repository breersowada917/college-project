import random
def get_random_code():
    # Generate a random 6-digit code
    code = ''.join(random.choice('1234567890') for i in range(6))
    return code