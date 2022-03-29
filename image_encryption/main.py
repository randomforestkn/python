# the fernet module generate the private key
from cryptography.fernet import Fernet

# key generation
key = Fernet.generate_key()

# start encryption process
fernet = Fernet(key)

#  store the key in seperate file
with open('key.key', 'wb') as filekey:
    filekey.write(key)

with open('key.key', 'rb') as filekey:
    key = filekey.read()


# open the image file
with open('example.jpeg', 'rb') as file:
    original_audio = file.read()

#  encrypt the image file
encrypted = fernet.encrypt(original_audio)

#  write the encrypted image data in a new file
with open('enc_index.jpeg', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)


# start decryption process
fernet = Fernet(key)

with open('enc_index.jpeg', 'rb') as file:
    audio = file.read()

dec_audio = fernet.decrypt(audio)

with open('dec_index.jpeg', 'wb') as file:
    file.write(dec_audio)
