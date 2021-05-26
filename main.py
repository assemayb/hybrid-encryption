import random
import time
from Cryptodome.Cipher import AES

from Elgamal import encryption, gen_key, power, decryption
from AES import aes_encrypt, aes_decrypt
from SHA import create_hashed_values
from pt_input import get_plain_text
from check import is_same


def main():
    time_start = time.time()

    # Hashing the plain text1 using SHA
    plain_text = get_plain_text()
    hashed_values = create_hashed_values(plain_text)
    print("Hashed Values: ", hashed_values)

    # AES Algorithm Enc and Dec
    aes_encryption_result = aes_encrypt(plain_text)
    aes_dec_msg = aes_decrypt(aes_encryption_result)
    aes_private_or_sec_key = aes_encryption_result.get("private_key")
    aes_ciphered_text = aes_encryption_result.get("cipher_text")

    print("Decrypted Message:", aes_dec_msg)

    q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)
    key = gen_key(q)  # privte key for the reciever
    h = power(g, key, q)
    public_key = gen_key(q)  # public key

    # encrypting/decryption of the AES secret key using Elgamal
    aes_secret_key = bytes.decode(aes_private_or_sec_key)
    enc_secret_key, prvt_k, y = encryption(aes_secret_key, q, h, g, 0)
    dec_secret_key = decryption(enc_secret_key, prvt_k, key, q)

    # encrypting the hashed values of the original plaintext
    enc_secret_key, prvt_k, result = encryption(
        hashed_values, q, h, g, aes_dec_msg)
    dec_secret_key = decryption(enc_secret_key, prvt_k, key, q)

    is_enc_and_dec_valid = is_same(result, plain_text)
    time_end = time.time()
    if is_enc_and_dec_valid:
        print("Encryption and Decryption has been completed SUCCESSFULLY")
    else:
        print("Encryption or Decryption has FAILED!")

    print("Time of Execution:", time_end - time_start, "MS")


if __name__ == "__main__":
    main()
