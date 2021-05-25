import random
from math import pow

# Asymmetric (private + public)


a = random.randint(2, 10)

# To fing gcd(greatest common divisor) of two numbers
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


# For key generation i.e. large random number
def gen_key(q):
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
    return key


def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x*y) % c
        y = (y*y) % c
        b = int(b/2)
    return x % c


# For asymetric encryption
def encryption(msg, q, h, g):
    en_msg = []
    k = gen_key(q)  # private key for sender
    s = power(h, k, q)
    p = power(g, k, q)
    for i in range(0, len(msg)):
        en_msg .append(msg[i])
    for i in range(0, len(en_msg)):
        en_msg[i] = s*ord(en_msg[i])
    return en_msg, p


# For decryption
def decryption(ct, p, key, q):
    pt = []
    h = power(p, key, q)
    for i in range(0, len(ct)):
        pt.append(chr(int(ct[i]/h)))
    return ''.join(pt)


# def main():
#     msg = 'this is the message to enc'
#     q = random.randint(pow(10, 20), pow(10, 50))
#     g = random.randint(2, q)
#     key = gen_key(q)  # Private key for receiver

#     h = power(g, key, q)

#     en_msg, p = encryption(msg, q, h, g)
#     # dr_msg = decryption(en_msg, p, key, q)
#     # print("Encrypted Message", en_msg)
#     # print("Decrypted Message :", dr_msg)


# if __name__ == '__main__':
#     main()
    
