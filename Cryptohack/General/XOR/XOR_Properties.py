# KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

def xor(a,b):
    return [x^y for x,y in zip(a,b)]

key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key2 = bytes(xor(bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"),key1))
key3 = bytes(xor(bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"),key2))
key1_xor_key2 = bytes(xor(key1,key2))
key12_xor_key3 = bytes(xor(key1_xor_key2,key3))
flag = bytes(xor(bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"),key12_xor_key3))
print(flag)