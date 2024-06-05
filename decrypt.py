from cryptography.fernet import Fernet

def decrypt_message(key, cipher_text):
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text)
    return plain_text

def main():
    key = input("Enter the key: ").encode()
    cipher_text = input("Enter the encrypted message: ").encode()

    plain_text = decrypt_message(key, cipher_text)
    print("Decrypted Message:", plain_text.decode())

if __name__ == "__main__":
    main()