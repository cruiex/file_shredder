#  Secure File Protection Tool  
**AES Encryption · Shamir’s Secret Sharing · Secure Shredding**

## Overview
This project implements a secure file protection system that combines strong symmetric encryption, threshold-based key management, and secure data deletion. Files are encrypted using **AES-256-GCM**, encryption keys are split using **Shamir’s Secret Sharing** for *k-of-n* recovery, and plaintext files are securely shredded to reduce the risk of forensic recovery.

---

## Features
- **AES-256-GCM** authenticated file encryption  
- **Shamir’s Secret Sharing (k-of-n)** for distributed key management  
- Threshold-based recovery requiring a minimum number of key shares  
- Secure overwrite-and-delete of plaintext files  
- Command-line interface (CLI) only  
- Cross-platform support: **Windows, Linux, macOS, WSL**

---

##  Project Structure
    file_shredder/
    ├── crypto/
    │   ├── aes.py          # AES-256-GCM encryption & decryption
    │   ├── shamir.py       # Shamir’s Secret Sharing implementation
    │   └── shredder.py     # Secure overwrite & delete logic
    │
    ├── core/
    │   ├── encrypt.py      # Encryption pipeline
    │   └── decrypt.py      # Recovery pipeline
    │
    ├── cli.py              # Command-line interface
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    │
    └── storage/            # Created automatically at runtime (gitignored)
        ├── encrypted/
        └── shares/

**Note:**  
The `storage/` directory is intentionally excluded from version control. It is created at runtime and stores sensitive artifacts such as encrypted files and key shares.

---

##  Requirements
- Python **3.10+**
- `pip`
- Virtual environment support (`venv`)
- External dependency: **cryptography**

---

##  Setup (All Operating Systems)

### Step 1: Clone the repository
    git clone https://github.com/cruiex/file_shredder.git
    cd file_shredder

### Step 2: Create and activate a virtual environment

### **Windows (PowerShell):**
    python -m venv venv
    venv\Scripts\Activate.ps1

### **Linux / macOS / WSL:**
    python3 -m venv venv
    source venv/bin/activate

### Step 3: Install dependencies
    pip install -r requirements.txt

---

##  Usage

### Encrypt a file
    python cli.py encrypt secret.txt --k 3 --n 5

**Syntax**

 python cli.py encrypt FILE_to_ENCRYPT --k RECOVERY_SHARES --n SPILITTING_SHARES


This operation:
- Encrypts `secret.txt` using **AES-256-GCM**
- Splits the encryption key into **5 shares**
- Requires **any 3 shares** for recovery
- Securely shreds the original plaintext file

Artifacts created:
- Encrypted file → `storage/encrypted/`
- Key shares → `storage/shares/secret.txt/`

---

### Decrypt a file (Threshold Recovery)

    python cli.py decrypt storage/encrypted/secret.txt.enc \
        --shares \
        storage/shares/secret.txt/share_1.txt \
        storage/shares/secret.txt/share_2.txt \
        storage/shares/secret.txt/share_3.txt \
        --out recovered.txt


**Syntax**

 python cli.py decrypt ENCRYPTED_FILE --shares SHARE_1 SHARE_2 SHARE_K --out recovered.txt
    

Decryption succeeds **only** if at least `k` valid key shares are provided.  
Using fewer than `k` shares fails cryptographically.
