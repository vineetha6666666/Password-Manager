from cryptography.fernet import Fernet
import json
import os

KEY_FILE = 'key.key'
DATA_FILE = 'passwords.json'

def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)

def load_key():
    with open(KEY_FILE, 'rb') as f:
        return f.read()

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def add_password(site, username, password, fernet):
    data = load_data()
    encrypted_pw = fernet.encrypt(password.encode()).decode()
    data[site] = {"username": username, "password": encrypted_pw}
    save_data(data)
    print("✅ Password added successfully.")

def get_password(site, fernet):
    data = load_data()
    if site in data:
        decrypted_pw = fernet.decrypt(data[site]['password'].encode()).decode()
        print(f"🔓 Site: {site}\n👤 Username: {data[site]['username']}\n🔑 Password: {decrypted_pw}")
    else:
        print("❌ Site not found.")

def main():
    generate_key()
    fernet = Fernet(load_key())

    while True:
        print("\nPassword Manager")
        print("1. Add new password")
        print("2. Get existing password")
        print("3. Exit")
        choice = input("Select option (1/2/3): ")

        if choice == '1':
            site = input("Site: ")
            username = input("Username: ")
            password = input("Password: ")
            add_password(site, username, password, fernet)
        elif choice == '2':
            site = input("Enter site to retrieve: ")
            get_password(site, fernet)
        elif choice == '3':
            break
        else:
            print("⚠️ Invalid option.")

if __name__ == '__main__':
    main()
  
