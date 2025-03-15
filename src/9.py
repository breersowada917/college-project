def get_random_integer(minimum, maximum):
    return random.randint(minimum, maximum)

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def get_random_boolean():
    return random.randint(0, 1) == 1
