import os
import secrets


def secure_delete(path: str, passes: int = 3) -> None:
    if not os.path.isfile(path):
        raise FileNotFoundError(path)

    length = os.path.getsize(path)

    with open(path, "r+b", buffering=0) as f:
        for _ in range(passes):
            f.seek(0)
            f.write(secrets.token_bytes(length))
            f.flush()
            os.fsync(f.fileno())

    os.remove(path)
