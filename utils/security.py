from cryptography.fernet import Fernet
from config import FERNET_KEY

fernet = Fernet(FERNET_KEY)

def encrypt_password(password: str) -> str:
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(password: str) -> str:
    return fernet.decrypt(password.encode()).decode()