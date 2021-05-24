from elgamal2 import PublicKey
from Cryptodome.Cipher import AES
from Elgamal import gen_key
from AES import aes_encrypt, aes_decrypt
from SHA import create_hashed_values
import random
import string


plain_text = "snfjkasjkbfkjsabfaasf"


length = 16
private_key = "".join(random.choice(string.ascii_lowercase) for x in range(length))
public_key =  "".join(random.choice(string.ascii_lowercase) for x in range(length))

# SHA
hashed_values = create_hashed_values(plain_text)
print("hashed values", hashed_values)

# AES ()
aes_enc_msg = aes_encrypt(plain_text, "123456")
aes_dec_msg = aes_decrypt(aes_enc_msg, "123456")

# # Elgamal
# # digital_signature = str(public_key) + hashed_values