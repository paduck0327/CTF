import base64

def gen(i):
	return i - 0xB * (((i * 0x5D1745D1745D1746) >> 0x40) >> 2)

for i in range(0x20):
	print(gen(i))

key = b"FlareOn2024"
flag = base64.b64decode('cQoFRQErX1YAVw1zVQdFUSxfAQNRBXUNAxBSe15QCVRVJ1pQEwd/WFBUAlElCFBFUnlaB1ULByRdBEFdfVtWVA==')
for i in range(len(flag)):
	print(chr(flag[i] ^ key[i % len(key)]),end='')
