from cryptography.fernet import Fernet

def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())
