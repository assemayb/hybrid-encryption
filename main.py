import random
import string
from elgamal2 import PublicKey
from Cryptodome.Cipher import AES
from Elgamal import gen_key
from AES import aes_encrypt, aes_decrypt
from SHA import create_hashed_values

from string_key import generate_random_key



plain_text = "thisisarandomplaintext"
password = "1234567" # the password used for AES private key

# hashing the plain text
hashed_values = create_hashed_values(plain_text)

# AES ()
aes_encryption_result = aes_encrypt(plain_text, password)
aes_dec_msg = aes_decrypt(aes_encryption_result, password)

aes_private_key = aes_encryption_result.get("private_key")

# x = aes_private_key.decode('UTF-8')
x = str(aes_private_key, 'UTF-16')
print(x.__len__())