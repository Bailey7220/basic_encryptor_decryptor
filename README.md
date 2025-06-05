# Basic Encryption/Decryption Tool

## Description

- This tool allows users to securely encrypt and decrypt files with a password. It uses AES (Advanced Encryption Standard) with strong password-based key derivation (PBKDF2), ensuring that only those with the correct password can access the protected data.
---

## Features

- Encrypts and decrypts files using AES (CBC mode)
- Password-based key derivation (PBKDF2) for strong security
- Handles errors and incorrect passwords gracefully
- Simple command-line interface

---

## Installation

1. Ensure Python 3 is installed.
2. Install the required library:

pip install pycryptodome

3. Download or clone this repository.

---

## Usage

**Encrypt a file:**

python basic_encryptor.py

- Choose "E" for encrypt.
- Enter the filename and a password.

**Decrypt a file:**

python basic_encryptor.py

- Choose "D" for decrypt.
- Enter the encrypted filename (ends with `.enc`) and the password.


---

## Security Concepts Demonstrated

- Symmetric encryption (AES)
- Password-based key derivation (PBKDF2)
- Secure file handling
- Access control and data confidentiality

---

## Improvement Ideas

- Add a GUI for easier use
- Support for multiple files or folders
- Integrate file integrity checking
- Allow choice of encryption algorithms

---

## What I Learned

- How to implement AES encryption in Python
- The importance of strong passwords and key derivation
- Secure handling of sensitive files

---

## References

- [PyCryptodome Documentation](https://pycryptodome.readthedocs.io/en/latest/)
- [AES (Wikipedia)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- [Password-Based Key Derivation Function (PBKDF2)](https://en.wikipedia.org/wiki/PBKDF2)

---

**For educational use only. Do not use for protecting highly sensitive or production data.**
