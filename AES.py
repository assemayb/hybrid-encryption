import os
import time
from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

from string_key import generate_random_key

def aes_encrypt(plain_text, password):
    salt = get_random_bytes(AES.block_size)
    # use the Scrypt KDF to get a private key from the password
    # private_key = hashlib.scrypt(
    #     password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    private_key = generate_random_key(16)
    # private_key = str.encode(private_key, "UTF-8")
    private_key = str.encode(private_key)
    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)
    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(
        bytes(plain_text, 'utf-8'))

    return {
        "private_key": private_key,
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    }


def aes_decrypt(enc_dict, password):
    # decode the dictionary entries from base64
    salt = b64decode(enc_dict['salt'])
    cipher_text = b64decode(enc_dict['cipher_text'])
    nonce = b64decode(enc_dict['nonce'])
    tag = b64decode(enc_dict['tag'])
    private_key = enc_dict['private_key']

    # generate the private key from the password and salt
    # private_key = hashlib.scrypt(
    #     password.encode('utf-8').strip(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)

    return bytes.decode(decrypted)

def main():

    start = time.time()

    password = "123456"
    plain_text = "this is the message to encrypt"
    encrypted = aes_encrypt(plain_text, password)
    print("cipher text", encrypted.get("cipher_text"))
    decrypted = aes_decrypt(encrypted, password)
    print(decrypted)

    end = time.time()
    print("time is ms",  end-start)

main()
"""

"""