import os
from typing import List
from crypto.aes import decrypt_file
from crypto.shamir import reconstruct_secret


def decrypt_pipeline(encrypted_file: str, share_files: List[str], output_file: str):
    if not os.path.isfile(encrypted_file):
        raise FileNotFoundError(encrypted_file)

    shares = []
    for sf in share_files:
        with open(sf, "r") as f:
            x, y = f.read().strip().split(",")
            shares.append((int(x), int(y)))

    key = reconstruct_secret(shares)
    decrypt_file(encrypted_file, output_file, key)
    del key
