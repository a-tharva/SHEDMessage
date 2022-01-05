from cryptography.fernet import Fernet

key = input('Input key: ').encode()
#key = Fernet.generate_key()
print(type(key))
text = input('Input text: ').encode()
enc = Fernet(key)
encode_text = enc.encrypt(f'{text}')
print(encode_text)