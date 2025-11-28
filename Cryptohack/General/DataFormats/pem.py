from Crypto.PublicKey import RSA
rsa_key = RSA.importKey(open('General/DataFormats/PEM.pem', "rb").read())
#Since rsa_key is a object
print(dir(rsa_key)) 
print(rsa_key._d)