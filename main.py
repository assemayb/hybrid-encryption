import random
from elgamal2 import PublicKey
from Cryptodome.Cipher import AES

from Elgamal import encryption, gen_key, power, decryption
from AES import aes_encrypt, aes_decrypt
from SHA import create_hashed_values
from string_key import generate_random_key
from pt_input import get_plain_text


plain_text = get_plain_text()
password = "1234567" # the password used for AES private key

# hashing the plain text
hashed_values = create_hashed_values(plain_text)

# AES 
aes_encryption_result = aes_encrypt(plain_text, password)
aes_dec_msg = aes_decrypt(aes_encryption_result, password)

aes_private_or_sec_key = aes_encryption_result.get("private_key")


#Elgamal
q = random.randint(pow(10, 20), pow(10, 50))
g = random.randint(2, q)

key = gen_key(q)  # Private key for receiver
h = power(g, key, q)

en_msg, prvt_k = encryption(plain_text, q, h, g)
dr_msg = decryption(en_msg, prvt_k, key, q)

print("enc message", en_msg)
print("private key", prvt_k)
print(dr_msg)
# key_two = gen_key(q) # Public key
# h_two = power(g, key, q)



