from Crypto.PublicKey import RSA 
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from base64 import b64encode
from Crypto.Util.Padding import pad
import math


import os
import xxtea
import binascii

# open all files
plainkeyFile = open("sender/keys.txt", "r")
cipherkeyFile = open("encryptedKey.txt" , "wb")

receiverPublicKeyFile = open("receiverPublicKey.txt", "rb")
encryptedMasterKeyFile = open("encryptedMasterKey.txt", "wb")

publicKey = RSA.import_key(receiverPublicKeyFile.read())

masterKey = os.urandom(16)
plainKeyBlock = plainkeyFile.read()
encryptedKeys = xxtea.encrypt(plainKeyBlock, masterKey)
cipherkeyFile.write(encryptedKeys)


# pad key file to a multiple of 32
# blocksize = 32 * math.ceil(os.stat("encryptedKey.txt").st_size / 32)
# if len(plainKeyBlock) < blocksize :
#     plaintext = pad(plainKeyBlock.encode('UTF-8'), blocksize)
# else :
#     plaintext = plainKeyBlock.encode('UTF-8')


# Encrypt the session key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(publicKey)
encryptedMasterKey = cipher_rsa.encrypt(masterKey)
encryptedMasterKeyFile.write(encryptedMasterKey)

plainkeyFile.close()
cipherkeyFile.close()

print(masterKey)

