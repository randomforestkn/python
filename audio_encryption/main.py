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

# open the audio file
with open('example.mp3', 'rb') as file:
    original_audio = file.read()

#  encrypt the audio file
encrypted = fernet.encrypt(original_audio)

#  write the encrypted audio data in a new file
with open('voice_encryption.mp3', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)


# start decryption process
fernet = Fernet(key)

with open('voice_encryption.mp3', 'rb') as file:
    audio = file.read()

dec_audio = fernet.decrypt(audio)

with open('voice_decryption.mp3', 'wb') as file:
    file.write(dec_audio)

