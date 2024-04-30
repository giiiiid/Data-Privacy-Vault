from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'secret data'

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)


def decrypt(cipher_text, key, nonce):
    cipher = AES.new(key, AES.MODE_EAX, nonce= nonce)
    enc_text, tag2 = cipher.encrypt_and_digest(data.encode("utf-8"))
    data = cipher.decrypt_and_verify(cipher_text, tag2)
    return data.decode("utf-8")

# if __name__ == "__main__":
#     data = decrypt(ciphertext, key, cipher.nonce)
#     # print(data.decode("utf-8"))
#     # print(len(data.decode("utf-8")))

#     user_text = input("Enter text: ")
#     if user_text == data:
#         print("Correct")
#     else:
#         print("Wrong")

print(type(data))