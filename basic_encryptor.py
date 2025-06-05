import os
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

def pad(data):
    pad_len = 16 - (len(data) % 16)
    return data + (chr(pad_len) * pad_len).encode()

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

def encrypt_file(filename, password):
    with open(filename, 'rb') as f:
        plaintext = f.read()
    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32, count=100000)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext))
    with open(filename + '.enc', 'wb') as f:
        f.write(salt + cipher.iv + ct_bytes)
    print(f"File encrypted as {filename}.enc")

def decrypt_file(enc_filename, password):
    with open(enc_filename, 'rb') as f:
        data = f.read()
    salt = data[:16]
    iv = data[16:32]
    ct = data[32:]
    key = PBKDF2(password, salt, dkLen=32, count=100000)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct))
    out_filename = enc_filename.replace('.enc', '.dec')
    with open(out_filename, 'wb') as f:
        f.write(pt)
    print(f"File decrypted as {out_filename}")

def main():
    print("Basic AES File Encryptor/Decryptor")
    choice = input("Choose (E)ncrypt or (D)ecrypt: ").strip().lower()
    if choice == 'e':
        filename = input("Enter the filename to encrypt: ").strip()
        password = input("Enter password: ").encode()
        encrypt_file(filename, password)
    elif choice == 'd':
        filename = input("Enter the filename to decrypt: ").strip()
        password = input("Enter password: ").encode()
        decrypt_file(filename, password)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
