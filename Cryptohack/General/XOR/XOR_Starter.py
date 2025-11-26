def xor(a,b):
    result = []
    for i in range(len(a)):
        result.append(a[i] ^ b[i%len(b)])
    return result

key = 13
key_bytes = key.to_bytes(1,"big")
ciphertext = b"label"

plaintext = xor(ciphertext,key_bytes)
print(bytes(plaintext))
#  print([chr(i) for i in plaintext])