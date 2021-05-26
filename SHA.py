import hashlib

def create_hashed_values(string):
    result = hashlib.sha384(string.encode())
    return result.hexdigest()
