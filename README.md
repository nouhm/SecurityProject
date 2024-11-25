# Secure-Shared-File-Storage-Using-Hybrid-Cryptography and FTP


Our goal is to achieve a secure shared file access using Hybrid Cryptography and FTP.
The purpose of this project is to build a secure platform of file sharing using FTP and multiple ciphers encryption. The requirements are that a file owner can upload an encrypted file to an FTP server. Other users can download the file from the server and then request the encryption keys of the file using their public keys, hence only the users granted this key can decrypt the downloaded file.
FTP is an old Internet protocol where files can be shared via upload/download mechanism.


## Encryptions algorithms used: 

## AES
Advanced Encryption Standard,
### The main idea of the algorithm:
• AES is a block cipher.
• The key size can be 128/192/256 bits.
• Encrypts data in blocks of 128 bits each.
* That means it takes 128 bits as input and outputs 128 bits of encrypted cipher text as output. AES relies on substitution-permutation network principle which means it is performed using a series of linked operations which involves replacing and shuffling of the input data.
When working on ciphersàAES performs operations on bytes of data rather than in bits. Since the block size is 128 bits, the cipher processes 128 bits (or 16 bytes) of the input data at a time.

## DES
Data encryption standard,
### The main idea of the algorithm:
• DES is a block cipher.
• The key size is 56 bits.
• Encrypts data in blocks of 64 bits each. 
* DES is based on the two fundamental attributes of cryptography: substitution (also called confusion) and transposition (also called diffusion). DES consists of 16 steps, each of which is called a round. Each round performs the steps of substitution and transposition. Let us now discuss the broad-level steps in DES.
When working on ciphersàsince DES is a block cipher and encrypts data in blocks of size of 64 bits each, which means 64 bits of plain text go as the input to DES, which produces 64 bits of ciphertext. The same algorithm and key are used for encryption and decryption, with minor differences.


## BlowFish
It is designed to be as an alternative to DES Encryption Technique. It is significantly faster than DES and provides a good encryption rate with no effective cryptanalysis technique found to date
### Characteristics:
• blockSize: 64-bits
• keySize: 32-bits to 448-bits variable size
• number of subkeys: 18
• number of rounds: 16
• number of substitution boxes: 4 (each having 512 entries of 32-bits
each)
### The main idea of the algorithm:
The encryption function consists of two parts: (1) rounds: The encryption consists of 16 rounds with each round (Ri) taking inputs the plaintext from previous round and corresponding subkey (Pi). (2) post-processing: The output after the 16 rounds is processed. While The decryption process is similar to that of encryption and the subkeys are used in reverse (P[17] – P[0]).
