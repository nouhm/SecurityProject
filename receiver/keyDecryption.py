from Crypto.PublicKey import RSA 
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from base64 import b64encode
import os
import xxtea
from Crypto.Util.Padding import unpad
import math



# open all files
decryptedKeyFile = open("receiver/decryptedKeys.txt", "wb")
cipherkeyFile = open("encryptedKey.txt" , "rb")

# decrypt master key
receiverPrivateKeyFile = open("receiver/receiverPrivateKey.txt", "rb")
encryptedMasterKeyFile = open("encryptedMasterKey.txt", "rb")


privateKey = RSA.import_key(receiverPrivateKeyFile.read())
cipher_rsa2 = PKCS1_OAEP.new(privateKey)
decryptedMasterKey = cipher_rsa2.decrypt(encryptedMasterKeyFile.read())

#print(decryptedMasterKey)
print(os.stat("encryptedKey.txt"))



# decrypt the encrypted file of keys using the master key
encryptedKeyBlock = cipherkeyFile.read()
decryptedKeys = xxtea.decrypt(encryptedKeyBlock, decryptedMasterKey)

# unpad key file to a multiple of 32
# blocksize = 32 * math.ceil(os.stat("encryptedKey.txt").st_size / 32)
# try:
#     unpaddedKeys = unpad(decryptedKeys, blocksize)    
# except ValueError:
#     unpaddedKeys = decryptedKeys


decryptedKeyFile.write(decryptedKeys)

decryptedKeyFile.close()
cipherkeyFile.close()



