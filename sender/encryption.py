from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from base64 import b64encode
from sys import getsizeof

# from Crypto.Cipher import 

# open all files

def encryption (ptext):

    #plaintextFile = open("sender/plaintext.txt", "r")
    keysFile = open("sender/keys.txt", "w")
    ciphertextFile = open("ciphertext.txt", "wb")

    plaintextFile = open(ptext, "r")
    #keysFile = open(keys, "w")
    #ciphertextFile = open(ctext, "wb")

    blockSize = 16
    algorithmCtr = 0

    #generate random keys for the 3 algorithms: 16bytes, 8bytes, & 8bytes respectively
    keyAES = get_random_bytes(16) # key size = 16 bytes
    keyDES = get_random_bytes(8) # key size = 8 bytes
    keyBlowFish = get_random_bytes(8) # key size = 8 bytes

    # write key to file
    #keysFile.write(key) # or key.decode("cp437")
    keysFile.write(b64encode(keyAES).decode("UTF-8")+'\n')
    keysFile.write(b64encode(keyDES).decode("UTF-8")+'\n')
    keysFile.write(b64encode(keyBlowFish).decode("UTF-8")+'\n')


    while True:
        # generate plaintext
        plaintextBlock = plaintextFile.read(blockSize)
        plaintext = b''

        if len(plaintextBlock) == 0:
            break

        elif (algorithmCtr%3 == 0):
            # update size to be read
            blockSize = 8

            # implement AES
            cipher = AES.new(keyAES, AES.MODE_ECB)

            # check if padding is needed
            if len(plaintextBlock) < 16 :
                plaintext = pad(plaintextBlock.encode('UTF-8'), 16)
            else :
                plaintext = plaintextBlock.encode('UTF-8')

        elif (algorithmCtr%3 == 1):
            # update size to be read
            blockSize = 8

            # generate random key 
            #key = get_random_bytes(8) # key size = 8 bytes
            # implement DES
            cipher = DES.new(keyDES, DES.MODE_ECB)

            # check if padding is needed
            if len(plaintextBlock) < 8 :
                plaintext = pad(plaintextBlock.encode('UTF-8'), 8)
            else :
                plaintext = plaintextBlock.encode('UTF-8')

        else :  
            # update size to be read
            blockSize = 16 

            # generate random key 
            #key = get_random_bytes(8) # key size = 8 bytes


            # implement blowfish
            cipher = Blowfish.new(keyBlowFish, Blowfish.MODE_ECB)

            # check if padding is needed
            if len(plaintextBlock) < 8 :
                plaintext = pad(plaintextBlock.encode('UTF-8'), 8)
            else :
                plaintext = plaintextBlock.encode('UTF-8')


        # encrypt and write to file
        ciphertext = cipher.encrypt(plaintext)
        ciphertextFile.write(ciphertext)

        # increment to next algorithm
        algorithmCtr+= 1



    plaintextFile.close()
    keysFile.close()
    ciphertextFile.close()