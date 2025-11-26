from pwn import * # pip install pwntools
import json

from base64 import b64decode
import codecs
from Crypto.Util.number import long_to_bytes
r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(100):

    received = json_recv()   
    
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])
    
    
    def base64_decoded(encoded):
        return b64decode(encoded).decode()
    
    def hex_decoded(encoded):
        return bytes.fromhex(encoded).decode()
    
    def rot13(encoded):
        return codecs.encode(encoded,"rot_13")
    
    def bigint(encoded):
        return bytes.fromhex(encoded[2:]).decode()
    
    def utf_8(encoded):
        return "".join([chr(i) for i in encoded])
    
    if received["type"] == "base64":
        decoded = base64_decoded(received["encoded"])
    elif received["type"] == "hex":
        decoded = hex_decoded(received["encoded"])
    elif received["type"] == "rot13":
        decoded = rot13(received["encoded"])
    elif received["type"] == "bigint":
        decoded = bigint(received["encoded"])
    else:
        decoded = utf_8(received["encoded"])
    
    to_send = {
        "decoded": decoded
    }
    json_send(to_send)
    
json_recv()
    