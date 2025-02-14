# File Shredder Using Shamir's Secret Sharing

## Team Members
- Saahil Mishra (22BCS105)
- Rohit (22BCS100)
- Shriya Udupa (22BCS121)
- Laxmi (22BCS059)

## About the Project
The **File Shredder using Shamir's Secret Sharing** project aims to create a secure tool for file encryption, shredding, and key distribution using Shamir’s Secret Sharing Scheme (SSS). This tool provides an additional layer of security by encrypting files using AES encryption and splitting the AES key into multiple shares using SSS. Only a specific number of shares are required to reconstruct the key, providing both confidentiality and resilience.

### Type of Security Measures We Implement
Our project uses a combination of **AES encryption** to secure the file contents and **Shamir’s Secret Sharing Scheme** to protect the AES key. Furthermore, the **file shredding mechanism** overwrites and securely deletes the original files to prevent unauthorized recovery.

## What are we trying to do? (Target of our Project)
### Objective
To develop a robust file security tool that:
- Encrypts sensitive files using AES encryption.
- Splits the AES encryption key into multiple shares using Shamir’s Secret Sharing Scheme.
- Allows secure key reconstruction with a predefined threshold of shares.
- Implements secure file shredding to prevent unauthorized recovery.

### Features
1. **File Encryption with AES**
   - Encrypt files using the AES algorithm to protect the data from unauthorized access.
2. **Shamir’s Secret Sharing Scheme**
   - Split the AES encryption key into multiple shares.
   - Define a threshold (`k`) to reconstruct the key, requiring only `k` out of `n` shares.
3. **File Shredding**
   - Securely overwrite and delete the original file to prevent data recovery.
4. **Key Reconstruction**
   - Reconstruct the AES key from the gathered shares and decrypt the encrypted file.

## Implementation Details
- **Front-End (Optional)**: A graphical interface using `tkinter` or `PyQt5` to provide a user-friendly experience for uploading, encrypting, shredding, and decrypting files.
- **Back-End**: Python libraries for encryption, secret sharing, and file operations.
  - **AES Encryption**: The `pycryptodome` library provides AES encryption and decryption tools.
  - **Shamir's Secret Sharing**: The `secretsharing` library (or `cryptography` library) offers Shamir’s scheme for splitting and reconstructing secrets.
  - **File Shredding**: Python’s `os` and `shutil` modules enable overwriting and deleting files securely.

### Progress
We have implemented the core functionality, including:
- File encryption using AES.
- Splitting the AES key into shares using Shamir’s Secret Sharing Scheme.
- Secure file shredding by overwriting data.
- A basic reconstruction and decryption process using the shares.

### Future Enhancements
- Improve the graphical interface for better user interaction.
- Explore additional overwriting patterns for enhanced file shredding security.
- Add a distributed storage option for securely storing the key shares.

## Conclusion
This project enhances file security by combining AES encryption, Shamir’s Secret Sharing Scheme, and secure file shredding. It not only ensures data confidentiality but also prevents unauthorized recovery of shredded files. By requiring a specific threshold of shares for key reconstruction, we provide both security and redundancy, making the tool suitable for secure file storage and deletion scenarios.
