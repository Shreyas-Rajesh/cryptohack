# Description : I've encrypted the flag with my secret key, you'll never be able to guess it.

def xor(a,b):
    result = []
    for i in range(len(a)):
        result.append(a[i] ^ b[i%len(b)])
    return result

ciphertext = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
crib = b"crypto{"

key = [x^y for x,y in zip(ciphertext,crib)]
key_bytes = bytes(key) + b"y" #when printing the key, "myXORke" was shown

plaintext = xor(ciphertext,key_bytes)
print(bytes(plaintext))

