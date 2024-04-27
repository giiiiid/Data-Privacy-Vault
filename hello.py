from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


salt = b'K\xb1\x19\xf6\xcd\x8a\xfdn\xeb\xbc\xe4\x08(\xf3y\x1e\xea\xe0\xbff\xb0\xd9Qa\t\xea\x0c\xc4^\x91\xb2D'
password = "mypassword"

'''Encrypting'''
key = PBKDF2(password, salt, dkLen=32)

message = "Hello world"

cipher = AES.new(key, AES.MODE_CBC)

ciphered_message = cipher.encrypt(pad(message.encode("utf-8"), AES.block_size))
# print(ciphered_message)


''''Decrypting'''
iv = b'\xb7\x84\xbc\x96\x00({\x99\x10\x02\xd6_\x12Z\x10\x8a'
decrpyt_data = b'\xb7\x84\xbc\x96\x00({\x99\x10\x02\xd6_\x12Z\x10\x8a'

cipher = AES.new(key, AES.MODE_CBC, iv=cipher.iv)

original = unpad(cipher.decrypt(decrpyt_data), AES.block_size)
print(original)
# print(iv.encode("utf-8"))
