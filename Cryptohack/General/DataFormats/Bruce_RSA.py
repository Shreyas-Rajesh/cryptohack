from Crypto.PublicKey import RSA

with open("General/DataFormats/Bruce_RSA.pub", "r") as f:
    object = RSA.import_key(f.read())

print(dir(object))
print(object.__ne__)
