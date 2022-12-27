from Crypto.PublicKey import RSA 
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from base64 import b64encode


# open all files
plainkeyFile = open("sender/keys.txt", "r")
cipherkeyFile = open("encryptedKey.txt" , "wb")

receiverPublicKeyFile = open("receiverPublicKey.txt", "rb")

recipientKey = RSA.import_key(receiverPublicKeyFile.read())

# sessionKey = get_random_bytes(16)

# # sessionKey = b64encode(sessionKey).decode("UTF-8")

# # Encrypt the session key with the public RSA key
# cipher_rsa = PKCS1_OAEP.new(recipientKey)
# enc_session_key = cipher_rsa.encrypt(sessionKey)

# # Encrypt the data with the AES session key
# cipher_aes = AES.new(sessionKey, AES.MODE_EAX)
# data = plainkeyFile.read()
# ciphertext = cipher_aes.encrypt(data.encode('UTF-8'))

# cipherkeyFile.write(ciphertext)

