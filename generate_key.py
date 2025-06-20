from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("key.key", "wb") as key_file:
    key_file.write(key)

print("✅ Fernet key generated and saved to 'key.key'")
