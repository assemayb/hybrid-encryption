import random
from math import pow
a = random.randint(2, 10)

# Asymmetric (private + public)

# To fing gcd of two numbers


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
    ct = []
    k = gen_key(q)
    s = power(h, k, q)
    p = power(g, k, q)
    for i in range(0, len(msg)):
        ct.append(msg[i])
    print("g^k used= ", p)
    print("g^ak used= ", s)
    for i in range(0, len(ct)):
        ct[i] = s*ord(ct[i])
    return ct, p
# For decryption


def decryption(ct, p, key, q):
    pt = []
    h = power(p, key, q)
    for i in range(0, len(ct)):
        pt.append(chr(int(ct[i]/h)))
    return pt


def main():

    msg = 'encryption'
    print("Original Message :", msg)

    # A random large num
    q = random.randint(pow(10, 20), pow(10, 50))
    # random number
    g = random.randint(2, q)

    key = gen_key(q)  # Private key for receiver
    h = power(g, key, q)
    # print("g used : ", g)
    # print("g^a used : ", h)

    en_msg, p = encryption(msg, q, h, g)
    dr_msg = decryption(en_msg, p, key, q)
    dmsg = ''.join(dr_msg)

    print(en_msg)
    print("Decrypted Message :", dmsg)


if __name__ == '__main__':
    main()
