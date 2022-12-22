from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
# from Crypto.Cipher import 

# open all files
plaintextFile = open("plaintext.txt", "r")
keysFile = open("keys.txt", "wb")
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
        blockSize = 16

        # generate random key 
        key = get_random_bytes(blockSize) # key size = 16 bytes

        # implement AES
        cipher = AES.new(key, AES.MODE_ECB)

    elif (algorithmCtr%3 == 1):
        # update size to be read
        blockSize = 8

        # generate random key 
        key = get_random_bytes(blockSize) # key size = 8 bytes

        # implement DES
        cipher = DES.new(key, DES.MODE_ECB)

    else :  
        # update size to be read
        blockSize = 8 

        # generate random key 
        key = get_random_bytes(blockSize) # key size = 8 bytes

        # implement blowfish
        cipher = Blowfish.new(key, Blowfish.MODE_ECB)

    
    # check if padding is needed
    if len(plaintextBlock) < blockSize :
        plaintext = pad(plaintextBlock.encode('UTF-8'), blockSize)
    else :
        plaintext = plaintextBlock.encode('UTF-8')
    
    # write key to file
    keysFile.write(key) # or key.decode("cp437")

    # encrypt and write to file
    ciphertext = cipher.encrypt(plaintext)
    ciphertextFile.write(ciphertext)

    # increment to next algorithm
    algorithmCtr+= 1

