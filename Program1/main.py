import os
import binascii
import string 

from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

from cryptography.hazmat.backends.openssl.backend import backend

def encrypt(key, plaintext):
    iv = b'\x00' * 16

    # Construct an AES-CBC Cipher object with the given key and a
    # randomly generated IV.
    encryptor = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend
    ).encryptor()


    # Encrypt the plaintext and get the associated ciphertext.
    ciphertext = encryptor.update(plaintext) + encryptor.finalize() 

    return (ciphertext)


def main():

  #key = b"thisisthekey    "
  plaintext = b"This is a top secret.           "
  cipherinput = "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9"


  #ciphertext = encrypt(key, plaintext)
  #ciphertext_hex = binascii.hexlify(ciphertext)
  #ciphertext_hex = ciphertext_hex.decode('UTF-8')
  #key = key.decode('UTF-8')

  with open('words.txt') as words:
    line = words.readline()
    line = line.strip("\n")
    while line:
        line = line.encode('UTF-8')
        print(line)

        if (len(line) < 16):
            while len(line) < 16:
                line+=' '
            ciphertext = encrypt(line, plaintext)
            ciphertext_hex = binascii.hexlify(ciphertext)
            ciphertext_hex = ciphertext_hex.decode('UTF-8')

            if (cipherinput[:32] == ciphertext_hex[:32]):
                print("\nCiphertext : ", ciphertext_hex)
                print("Key        : ", line, "\n")
                return

        line = words.readline()







main()