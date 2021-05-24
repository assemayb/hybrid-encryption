import random
import string

def generate_random_key(length):
    k = "".join(random.choice(string.ascii_lowercase) for x in range(length))
    return k
