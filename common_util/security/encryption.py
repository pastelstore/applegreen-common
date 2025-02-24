import logging
import os

from cryptography.fernet import Fernet
from common_util.constant.constant import SECRET_KEY_PATH

# secret key를 최초 구동 시 로딩
SECRET_KEY_CACHE: bytes


def generate_key():
    if not os.path.exists(SECRET_KEY_PATH):
        key = Fernet.generate_key()
        with open(SECRET_KEY_PATH, "wb") as key_file:
            key_file.write(key)

        logging.info("Secret key created successfully.")


def load_key():
    global SECRET_KEY_CACHE

    if not os.path.exists(SECRET_KEY_PATH):
        raise FileNotFoundError("Secret key not found.")

    with open(SECRET_KEY_PATH, "rb") as key_file:
        SECRET_KEY_CACHE = key_file.read()

    logging.info("Secret key loaded.")


def encrypt_data(plain_text: str) -> str:
    if SECRET_KEY_CACHE is None:
        raise RuntimeError("Secret key NOT loaded.")

    cipher = Fernet(SECRET_KEY_CACHE)
    encrypted_text = cipher.encrypt(plain_text.encode())
    return encrypted_text.decode()


def decrypt_data(encrypted_text: str) -> str:
    if SECRET_KEY_CACHE is None:
        raise RuntimeError("Secret key NOT loaded.")

    cipher = Fernet(SECRET_KEY_CACHE)
    decrypted_text = cipher.decrypt(encrypted_text.encode())
    return decrypted_text.decode()


# 최초 실행 시 암호화 키 생성
if __name__ == "__main__":
    generate_key()
