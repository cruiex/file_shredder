import secrets
from typing import List, Tuple

PRIME = 2**521 - 1


def _eval_poly(coeffs, x):
    result = 0
    for c in reversed(coeffs):
        result = (result * x + c) % PRIME
    return result


def split_secret(secret: bytes, k: int, n: int) -> List[Tuple[int, int]]:
    if k > n:
        raise ValueError("k cannot be greater than n")

    secret_int = int.from_bytes(secret, "big")
    coeffs = [secret_int] + [secrets.randbelow(PRIME) for _ in range(k - 1)]

    shares = []
    for x in range(1, n + 1):
        y = _eval_poly(coeffs, x)
        shares.append((x, y))

    return shares


def reconstruct_secret(shares: List[Tuple[int, int]]) -> bytes:
    secret = 0

    for j, (xj, yj) in enumerate(shares):
        num = 1
        den = 1
        for m, (xm, _) in enumerate(shares):
            if m != j:
                num = (num * (-xm)) % PRIME
                den = (den * (xj - xm)) % PRIME
        lagrange = num * pow(den, -1, PRIME)
        secret = (secret + yj * lagrange) % PRIME

    size = (secret.bit_length() + 7) // 8
    return secret.to_bytes(size, "big")
