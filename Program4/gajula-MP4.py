import os
import sys
import qrcode
import secrets
import string 
import hmac
import time
import hashlib
import math
import struct
import base64

def generateQR(key):
    #Create URI
    uri = 'otpauth://totp/' + 'Google' + ':' + 'example@example.com' + '?secret=' + str(key) + '&issuer=' + 'Google'

    #Create QR Code
    qr = qrcode.make(uri)
    print("Generating QR Code...")
    qr.save("testQR.jpg")

def truncate_h(h):
    int_h = int(h, base=16)
    offset = int_h & 0xf
    offset = offset * 2
    
    hex_bits = h[offset:offset + 8] 
    int_hex = int(hex_bits, base=16)
    int_hex = int_hex & 0x7fffffff

    modded_val = (int_hex % 10**6)
    print("%06d" % modded_val) 


def HOTP(key):
    while(1):
        unix_t = time.time()
        unix_t = unix_t/30
        unix_t = int(unix_t)
        unix_t = struct.pack('>Q', unix_t)

        h = hmac.new(key, unix_t, hashlib.sha1)
        h = h.hexdigest()
        truncate_h(h)

        time.sleep(30 - (time.time()%30))
               
def main():
    key = "AAAAAAAAAAAAAAAA"
    key = bytes(key, 'UTF-8') 

    arg1 = sys.argv[1]
    if (arg1 == "--generate-qr"):  
        key = base64.b32encode(key)
        key = key.split(b"=")[0]
        key = key.decode('utf-8')
        generateQR(key)
    
    if (arg1 == "--get-otp"): 
        HOTP(key)  

main()

