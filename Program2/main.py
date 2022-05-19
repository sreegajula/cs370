import os
import binascii
import string 

from cryptography.hazmat.primitives import (
    hashes
)

from cryptography.hazmat.backends.openssl.backend import backend

def get_hash(input_txt):
    input_txt = bytes(input_txt)
    digest = hashes.Hash(hashes.SHA256(), backend)
    digest.update(input_txt)
    digest = digest.finalize()

    digest = binascii.hexlify(digest)
    digest = int(digest, 16)
    return digest


def main():
# create bit array in the millions (DONE)
# set each value to 0 (DONE)
# set dictionary index value 
# check sample input value with dictionary valiue after hashing them both
# hexlify to convert hash to number (DONE)
# hash each word in dictionnary and use that int as a index for a bit array (set to 1)

    # create and populate bit array
    bit_array = []
    for i in range(1000000):
        bit_array.append(0)

    # get words from dictionary
    with open('dictionary.txt') as dictionary:
        line = dictionary.readline()
        line = line.strip("\n")
        for line in dictionary:
            print(line)
            hashed_line = get_hash(line)
            bit_array[hashed_line] = 1



    # comparing to input after creating filter
    with open('sample_input.txt') as dictionary:
        line = words.readline()
        line = line.strip("\n")






main()