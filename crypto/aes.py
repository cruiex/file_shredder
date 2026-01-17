import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

KEY_SIZE = 32      # 256-bit
NONCE_SIZE = 12    # GCM standard


def generate_key() -> bytes:
    return os.urandom(KEY_SIZE)


def encrypt_file(input_path: str, output_path: str, key: bytes) -> None:
    aesgcm = AESGCM(key)
    nonce = os.urandom(NONCE_SIZE)

    with open(input_path, "rb") as f:
        plaintext = f.read()

    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    with open(output_path, "wb") as f:
        f.write(nonce + ciphertext)


def decrypt_file(input_path: str, output_path: str, key: bytes) -> None:
    with open(input_path, "rb") as f:
        data = f.read()

    nonce = data[:NONCE_SIZE]
    ciphertext = data[NONCE_SIZE:]

    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)

    with open(output_path, "wb") as f:
        f.write(plaintext)
