from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import re
import codecs


salt = b'K\xb1\x19\xf6\xcd\x8a\xfdn\xeb\xbc\xe4\x08(\xf3y\x1e\xea\xe0\xbff\xb0\xd9Qa\t\xea\x0c\xc4^\x91\xb2D'
password = "mypassword"

# '''Encrypting'''
key = PBKDF2(password, salt, dkLen=16)

plain_text = "Gideon701!nobbs7!"
print(len(plain_text))
    

def encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    enc_text = cipher.encrypt(pad(plain_text.encode("utf-8"), AES.block_size))
    return cipher.iv, enc_text


def decrypt(enc_text, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    dec_text = cipher.decrypt(enc_text).decode("utf-8")
    return dec_text.strip("")


if __name__ == "__main__":
    iv, enc_text = encrypt(plain_text, key)
    dec_text = decrypt(enc_text, iv)
    print(len(dec_text))
    print(dec_text)

    user_text = input("Enter text: ")
    # if codecs.encode(user_text, "base64") == dec_text:
    if user_text == dec_text:
        print("Correct")
    else: 
        print("Wrong")
    