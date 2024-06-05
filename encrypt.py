from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    return key

def encrypt_message(key, message):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(message.encode())
    return cipher_text

def main():
    key = generate_key()
    print("Generated Key:", key.decode())

    message = input("Enter a message to encrypt: ")
    cipher_text = encrypt_message(key, message)
    print("Encrypted Message:", cipher_text.decode())

if __name__ == "__main__":
    main()