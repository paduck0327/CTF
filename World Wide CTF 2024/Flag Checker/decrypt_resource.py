data = open("resource", "rb").read()
xor_key = bytes.fromhex("0F4D0DB3668DD58CABB9EB409657EAA8") # md5("FLAG")
codes = b''

for i in range(0, len(data)):
    v1 = data[i]
    v2 = xor_key[i % len(xor_key)]
    x1 =  v1 ^ v2
    codes += bytes( [ x1 ] )

with open("resource_decrypt.bin", "wb") as f:
    f.write(codes)
