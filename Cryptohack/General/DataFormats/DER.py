from Crypto.PublicKey import RSA
rsa_key = RSA.importKey(open('General/DataFormats/DER.der', "rb").read())
print(dir(rsa_key))
print(rsa_key.__ne__)