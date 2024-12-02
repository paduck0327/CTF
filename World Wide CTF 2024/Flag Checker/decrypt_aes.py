from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def aes_cbc_decrypt(key, iv, encrypted_data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)
    decrypted_data = unpad(decrypted_data, AES.block_size)
    return decrypted_data

if __name__ == "__main__":
    key = bytes.fromhex("5245564552534520454e47494e454552")  # AES Key (16 bytes)
    iv = bytes.fromhex("5245564552534520454e47494e454552")  # IV (16 bytes)

    encrypted_data =b'\xb7\xa86\x83\xa3c[p\x8d\xef\xa8\xb7\xa5X\x9a\x18V\xaco\x1f\xe3_\xe3\x0e\x98\xd9\xa7\x85Q\x90\x1e,\xd3HC\xb8\xe2\x02\xb8HLRU\x8a\x16.\xbd\xdb\x10*u\xeb\x1a\xa6U\x90\xf0\x12\xa8\xed\xd1\xd8p\xab'
    decrypted_data = aes_cbc_decrypt(key, iv, encrypted_data)
    print("flag: ",decrypted_data.decode('utf-8'))
