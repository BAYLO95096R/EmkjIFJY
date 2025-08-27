# 代码生成时间: 2025-08-27 13:30:56
import hashlib
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from getpass import getpass


class PasswordEncryptionDecryption:
    """
    A class for encrypting and decrypting passwords using symmetric key cryptography.
    """

    def __init__(self, key=None):
        """
        Initialize the encryption/decryption tool.
        If a key is not provided, a random key will be generated.
        """
        self.key = key or self.generate_key()
        self.cipher = Fernet(self.key)

    @staticmethod
    def generate_key():
        """
        Generate a random key using Fernet's key generation method.
        """
        return Fernet.generate_key()

    def encrypt_password(self, password):
        """
        Encrypt a password using the symmetric key.
        :param password: The password to be encrypted.
        :return: The encrypted password.
        """
        try:
            if not password:
                raise ValueError("Password cannot be empty")
            encrypted_password = self.cipher.encrypt(password.encode())
            return encrypted_password.decode()
        except Exception as e:
            print(f"An error occurred during encryption: {e}")
            return None

    def decrypt_password(self, encrypted_password):
        """
        Decrypt an encrypted password using the symmetric key.
        :param encrypted_password: The encrypted password to be decrypted.
        :return: The decrypted password.
        """
        try:
            if not encrypted_password:
                raise ValueError("Encrypted password cannot be empty")
            decrypted_password = self.cipher.decrypt(encrypted_password.encode())
            return decrypted_password.decode()
        except Exception as e:
            print(f"An error occurred during decryption: {e}")
            return None

    @staticmethod
    def derive_key(password, salt):
        """
        Derive a key from a password using PBKDF2 HMAC algorithm.
        :param password: The password to derive the key from.
        :param salt: A random salt to use during key derivation.
        :return: The derived key.
        """
        backend = default_backend()
        salt_bytes = salt.encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt_bytes,
            iterations=100000,
            backend=backend
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key.decode()

# Example usage:
if __name__ == "__main__":
    password_tool = PasswordEncryptionDecryption()
    password = getpass("Enter password to encrypt: ")
    encrypted = password_tool.encrypt_password(password)
    print(f"Encrypted password: {encrypted}")
    
    decrypted = password_tool.decrypt_password(encrypted)
    print(f"Decrypted password: {decrypted}")
