from base64 import b64decode




keysFile = open("receiver/decryptedKeys.txt", "rb+")

keys1 = (keysFile.readline().replace(b'\r\n', b''))
keys2 = b64decode(keysFile.readline().replace(b'\r\n', b''))
keys3 = b64decode(keysFile.readline().replace(b'\r\n', b''))



print(keys1.decode('utf-8'))
print(keys2)
print(keys3)

