ciphertext = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for key in range(256):
    key_byte = key.to_bytes(1,"big")
    plaintext = []

    for j in range(len(ciphertext)):
        plaintext.append(ciphertext[j] ^ key)

    plaintext_bytes = bytes(plaintext)

    if b"crypto" in plaintext_bytes:
        print("Key:",key)
        print("Plaintext:",plaintext_bytes)
