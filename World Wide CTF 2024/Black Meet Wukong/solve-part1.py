from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from cryptography.fernet import Fernet
import os

key_fernet = [b'zTskoYGm68VrSiOM6J9W0PqyKTfSyraM0NydVmJvM_k=', b'pcD23bRQTL1MqLS84NdPsiPdYJlwbTaal6JmulzTq4k=', b'9EBQNDjmy0rGXCbVgVnrgFFsAHk4Ye1M8y1GSIx9CPY=', b'663RnK5l0MQzewfpAQfYhJbL3p7ZRoR-j7I3DkXiUIk=', b'I5Arxkgfo2E56VBVctFjJ-pFkeBbQg6QXMuG-gNgqq4=', b'eXP1sKfkTE9PNkWR8rA9jzJqun80yMYPrzMMi65JQpw=', b'56S9Sv7zUPL71w6N2OTSwxvFl_a-5zvsN6rxQI97UWU=', b'gZcRMaVftMg_F9E4tNQ_etAR7_PKT_vVfWwWkMSxDQc=', b'-XmaKL4uo4p0gM5ARQZtxjZ_5ecK1w53AEkWuiWDIzQ=', b'ikNfBtrrX-9EBI3iKzWnBJW5wNNvi8rM4oT9BLqDJNw=', b'uEikHaHAX1B20aB_bcQwUA0aO21Ai-rgYAqGfKxHKJA=', b'deoHTwNvwTOuQjoy5oh9jN_ZQlLbVCvwI47D3sQt8UA=', b'xuaD7BqwreniKZAvBO38MO250oO40HXboxhU8--6YQ0=', b'X5GfY_zukIDPKxyzmMYFkps-Av8Ao2TQDPmckrjb3ZQ=', b'CAOD7XSW4e-ON33uz5_8h6RZhorDlKg798e1RcEYSlo=', b'dMphwlwO6Qh_FCdbMzseoZsWkQWPFtGx8VSiFAN2SSo=', b'q4NfcRieLIKnyBwFEhUxZcR_8A3BFS_n_cIE8sFX8a4=', b'hLfAPR06xuo545qJlzlYko5f9KKuXOBrCBNgzruTV14=']
key_xori = 'y0u_l00k_l1k3_X1sh1_&_b3_my_l4dy'

def god_bless_aes(data, key):
    key = key.encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(data, AES.block_size)
    cipher_text = cipher.encrypt(padded_text)
    return cipher_text

def decrypt_aes(data, key):
	key = key.encode('utf-8')
	cipher = AES.new(key, AES.MODE_ECB)
	padded_text = cipher.decrypt(data)
	plain_text = unpad(padded_text, AES.block_size)
	return plain_text

def xor(data, key):
	return bytearray([b ^ key[i % len(key)] for i, b in enumerate(data)])

f = open("wukong.png.odin", "rb")
data = f.read()
enc = data
dec = decrypt_aes(enc, key_xori)
xor_dec = bytes(xor(dec, key_fernet[0]))
for key in key_fernet[::-1]:
	fernet = Fernet(key)
	xor_dec = fernet.decrypt(xor_dec)
f2 = open("wukong.png", "wb")
f2.write(xor_dec)
