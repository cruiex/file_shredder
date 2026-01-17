import argparse
from core.encrypt import encrypt_pipeline
from core.decrypt import decrypt_pipeline


def main():
    parser = argparse.ArgumentParser(
        description="Secure File Protection Tool (AES + Shamir + Shredding)"
    )

    sub = parser.add_subparsers(dest="cmd", required=True)

    enc = sub.add_parser("encrypt")
    enc.add_argument("file")
    enc.add_argument("--k", type=int, required=True)
    enc.add_argument("--n", type=int, required=True)

    dec = sub.add_parser("decrypt")
    dec.add_argument("encrypted")
    dec.add_argument("--shares", nargs="+", required=True)
    dec.add_argument("--out", required=True)

    args = parser.parse_args()

    if args.cmd == "encrypt":
        enc_file, share_dir = encrypt_pipeline(args.file, args.k, args.n)
        print(f"[+] Encrypted file: {enc_file}")
        print(f"[+] Shares stored in: {share_dir}")

    elif args.cmd == "decrypt":
        decrypt_pipeline(args.encrypted, args.shares, args.out)
        print(f"[+] Decrypted output: {args.out}")


if __name__ == "__main__":
    main()
