from Crypto.PublicKey import RSA 


receiverPrivateKeyFile = open("receiverPrivateKey.txt", "wb")
receiverPublicKeyFile = open("receiverPublicKey.txt", "wb")

key = RSA.generate(2048)
privateKey = key.export_key()
receiverPrivateKeyFile.write(privateKey)

publicKey = key.publickey().export_key()
receiverPublicKeyFile.write(publicKey)
receiverPublicKeyFile.close()