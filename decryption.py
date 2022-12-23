from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import unpad
from base64 import b64decode

# from Crypto.Cipher import 

# open all files
plaintextFile = open("decipheredText.txt", "w")
keysFile = open("keys.txt", "rb+")
ciphertextFile = open("ciphertext.txt", "rb")

blockSize = 16
algorithmCtr = 0

while True:
    # generate ciphertext
    ciphertextBlock = ciphertextFile.read(blockSize)

    if ciphertextBlock == '':
        break

    elif (algorithmCtr%3 == 0):
        # update size to be read
        blockSize = 8

        # generate random key 
        key =  b64decode(keysFile.readline().replace(b'\r\n', b'')) # key size = 16 bytes

        # implement AES
        cipher = AES.new(key, AES.MODE_ECB)

        # decrypt and write to file
        plaintext = cipher.decrypt(ciphertextBlock)

        # check if unpadding is needed
        try:
            unpaddedText = unpad(plaintext, 16)
            break
        except ValueError:
            unpaddedText = plaintext

    elif (algorithmCtr%3 == 1):
        # update size to be read
        blockSize = 8

        # generate random key 
        key =  b64decode(keysFile.readline().replace(b'\r\n', b'')) # key size = 8 bytes

        # implement DES
        cipher = DES.new(key, DES.MODE_ECB)

        # decrypt and write to file
        plaintext = cipher.decrypt(ciphertextBlock)

        # check if unpadding is needed
        try:
            unpaddedText = unpad(plaintext, 8)
            break
        except ValueError:
            unpaddedText = plaintext

    else :  
        # update size to be read
        blockSize = 16

        # generate random key 
        key =  b64decode(keysFile.readline().replace(b'\r\n', b'')) # key size = 8 bytes

        # implement blowfish
        cipher = Blowfish.new(key, Blowfish.MODE_ECB)

        # decrypt and write to file
        plaintext = cipher.decrypt(ciphertextBlock)

        # check if unpadding is needed
        try:
            unpaddedText = unpad(plaintext, 8)
            break
        except ValueError:
            unpaddedText = plaintext
    


    p = (unpaddedText).decode('UTF-8')
    plaintextFile.write(p)

    # increment to next algorithm
    algorithmCtr+= 1

