from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from base64 import b64encode

# from Crypto.Cipher import 

# open all files
plaintextFile = open("plaintext.txt", "r")
keysFile = open("keys.txt", "w")
ciphertextFile = open("ciphertext.txt", "wb")

blockSize = 16
algorithmCtr = 0

while True:
    # generate plaintext
    plaintextBlock = plaintextFile.read(blockSize)
    plaintext = b''

    if plaintextBlock == '':
        break

    elif (algorithmCtr%3 == 0):
        # update size to be read
        blockSize = 8

        # generate random key 
        key = get_random_bytes(16) # key size = 16 bytes

        # implement AES
        cipher = AES.new(key, AES.MODE_ECB)

        # check if padding is needed
        if len(plaintextBlock) < 16 :
            plaintext = pad(plaintextBlock.encode('UTF-8'), 16)
        else :
            plaintext = plaintextBlock.encode('UTF-8')

    elif (algorithmCtr%3 == 1):
        # update size to be read
        blockSize = 8

        # generate random key 
        key = get_random_bytes(8) # key size = 8 bytes
        # implement DES
        cipher = DES.new(key, DES.MODE_ECB)

        # check if padding is needed
        if len(plaintextBlock) < 8 :
            plaintext = pad(plaintextBlock.encode('UTF-8'), 8)
        else :
            plaintext = plaintextBlock.encode('UTF-8')

    else :  
        # update size to be read
        blockSize = 16 

        # generate random key 
        key = get_random_bytes(8) # key size = 8 bytes


        # implement blowfish
        cipher = Blowfish.new(key, Blowfish.MODE_ECB)

        # check if padding is needed
        if len(plaintextBlock) < 8 :
            plaintext = pad(plaintextBlock.encode('UTF-8'), 8)
        else :
            plaintext = plaintextBlock.encode('UTF-8')


    
    # write key to file
    #keysFile.write(key) # or key.decode("cp437")
    keysFile.write(b64encode(key).decode("UTF-8")+'\n')
    # encrypt and write to file
    ciphertext = cipher.encrypt(plaintext)
    ciphertextFile.write(ciphertext)

    # increment to next algorithm
    algorithmCtr+= 1

