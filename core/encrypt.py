import os
from crypto.aes import generate_key, encrypt_file
from crypto.shamir import split_secret
from crypto.shredder import secure_delete


def encrypt_pipeline(input_file: str, k: int, n: int):
    if not os.path.isfile(input_file):
        raise FileNotFoundError(input_file)

    encrypted_dir = "storage/encrypted"
    shares_dir = "storage/shares"

    os.makedirs(encrypted_dir, exist_ok=True)
    os.makedirs(shares_dir, exist_ok=True)

    key = generate_key()

    encrypted_path = os.path.join(
        encrypted_dir, os.path.basename(input_file) + ".enc"
    )
    encrypt_file(input_file, encrypted_path, key)

    shares = split_secret(key, k, n)

    base = os.path.basename(input_file)
    file_share_dir = os.path.join(shares_dir, base)
    os.makedirs(file_share_dir, exist_ok=True)

    for idx, (x, y) in enumerate(shares, start=1):
        with open(os.path.join(file_share_dir, f"share_{idx}.txt"), "w") as f:
            f.write(f"{x},{y}")

    secure_delete(input_file)
    del key

    return encrypted_path, file_share_dir
