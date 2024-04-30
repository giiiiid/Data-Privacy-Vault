from db.databaseConnect import sessionLocal
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


'''Initializing db'''
def get_db():
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()


'''Key to be used for encryption'''
key = get_random_bytes(16)


'''Cipher to encrypt'''
cipher = AES.new(key, AES.MODE_EAX)


'''Encryption function'''
def encrypt_data(data: str):
    cipher_text, tag = cipher.encrypt_and_digest(data.encode("utf-8"))
    return cipher_text, tag


'''Decryption function'''
def decrypt_data(cypher_text, tag):
    decrypt_cipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
    # enc_text, tag = cipher.encrypt_and_digest(data.encode("utf-8"))
    data = decrypt_cipher.decrypt(cypher_text, tag)
    return data.decode("utf-8")


# if __name__ == "__main__":
#     data = 
