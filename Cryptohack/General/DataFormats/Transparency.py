from Crypto.PublicKey import RSA
from hashlib import sha256

with open("General/DataFormats/Transparency.pem", "r") as f:
    object = RSA.import_key(f.read())

der = object.export_key(format="DER")
sha = sha256(der).hexdigest()
print(sha)
# 29ab37df0a4e4d252f0cf12ad854bede59038fdd9cd652cbc5c222edd26d77d2
#https://thetransparencyflagishere.cryptohack.org/