from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import unpad
from base64 import b64decode
import codecs

# from Crypto.Cipher import 
def decryption(ctext):
    # open all files
    plaintextFile = open("receiver/decipheredText.txt", "w")
    keysFile = open("receiver/decryptedKeys.txt", "rb+")
    ciphertextFile = open("ciphertext.txt", "rb")

    keyAES =  b64decode(keysFile.readline().replace(b'\r\n', b''))
    keyDES =  b64decode(keysFile.readline().replace(b'\r\n', b''))
    keyBlowFish =  b64decode(keysFile.readline().replace(b'\r\n', b''))

    blockSize = 16
    algorithmCtr = 0

    while True:
        # generate ciphertext
        nonce, ciphertextBlock = [ciphertextFile.read(x) for x in (blockSize, -1)]
        #keys = b64decode(keysFile.readline().replace(b'\r\n', b''))

        if len(ciphertextBlock) == 0:
            break

        elif (algorithmCtr%3 == 0):
            # update size to be read
            blockSize = 8

            # implement AES
            cipher = AES.new(keyAES, AES.MODE_EAX, nonce)

            # decrypt and write to file
            plaintext = cipher.decrypt(ciphertextBlock)

            # check if unpadding is needed
            # try:
            #     unpaddedText = unpad(plaintext, 16)
            #     break
            # except ValueError:
            #     unpaddedText = plaintext

        elif (algorithmCtr%3 == 1):
            # update size to be read
            blockSize = 8
            
            # implement DES
            cipher = DES.new(keyDES, DES.MODE_EAX, nonce)

            # decrypt and write to file
            plaintext = cipher.decrypt(ciphertextBlock)

            # check if unpadding is needed
            # try:
            #     unpaddedText = unpad(plaintext, 8)
            #     break
            # except ValueError:
            #     unpaddedText = plaintext

        else :  
            # update size to be read
            blockSize = 16

            # implement blowfish
            cipher = Blowfish.new(keyBlowFish, Blowfish.MODE_EAX, nonce)

            # decrypt and write to file
            plaintext = cipher.decrypt(ciphertextBlock)

            # check if unpadding is needed
            # try:
            #     unpaddedText = unpad(plaintext, 8)
            #     break
            # except ValueError:
            #     unpaddedText = plaintext
        


        p = (plaintext)
        print(p)  
        plaintextFile.write(plaintext.decode())

        # increment to next algorithm
        algorithmCtr+= 1


    plaintextFile.close()
    keysFile.close()
    ciphertextFile.close()