# Encrypt-Decrypt-Text
Demonstrate Encryption and Decryption using the Fernet symmetric Encryption algorithm

**Here's a step-by-step explanation of the code: Encrypt Program**
Step 1: Importing the Fernet class
The code starts by importing the Fernet class from the cryptography.fernet module. The Fernet class is a symmetric encryption algorithm that provides secure encryption and decryption of data.

Step 2: Defining the generate_key function
The generate_key function is defined to generate a new Fernet key. This key will be used for encryption and decryption. The Fernet.generate_key() method generates a new key, which is then returned by the function.

Step 3: Defining the encrypt_message function
The encrypt_message function is defined to encrypt a message using a given key. It takes two arguments: key and message. Here's what the function does:
It creates a Fernet object using the provided key.
It encodes the message to bytes using the encode() method.
It encrypts the encoded message using the encrypt() method of the Fernet object.
It returns the encrypted ciphertext.

Step 4: Defining the main function
The main function is the entry point of the script. Here's what it does:
It generates a new Fernet key using the generate_key() function and prints it to the console.
It prompts the user to enter a message to encrypt using the input() function.
It encrypts the message using the encrypt_message() function and prints the encrypted ciphertext to the console.

Step 5: Running the script
The script uses the if __name__ == "__main__": guard to ensure that the main() function is only executed when the script is run directly (i.e., not when it's imported as a module by another script).

When you run this script, it will:
Generate a new Fernet key and print it to the console.
Prompt you to enter a message to encrypt.
Encrypt the message using the generated key and print the encrypted ciphertext to the console.

The encrypted ciphertext is a URL-safe base64-encoded string, which can be safely stored or transmitted. To decrypt the ciphertext, you would need to use the same Fernet key and the decrypt() method of the Fernet object.



**Here's a step-by-step explanation of the code: Decrypt Program**
Step 1: Importing the Fernet class
The code starts by importing the Fernet class from the cryptography.fernet module. The Fernet class is a symmetric encryption algorithm that provides secure encryption and decryption of data.

Step 2: Defining the decrypt_message function
The decrypt_message function is defined to decrypt a ciphertext using a given key. It takes two arguments: key and cipher_text. Here's what the function does:
It creates a Fernet object using the provided key.
It decrypts the cipher_text using the decrypt() method of the Fernet object.
It returns the decrypted plaintext.

Step 3: Defining the main function
The main function is the entry point of the script. Here's what it does:
It prompts the user to enter the Fernet key using the input() function and encodes it to bytes using the encode() method.
It prompts the user to enter the encrypted message (ciphertext) using the input() function and encodes it to bytes using the encode() method.
It decrypts the ciphertext using the decrypt_message() function and prints the decrypted plaintext to the console.
Step 4: Running the script

The script uses the if __name__ == "__main__": guard to ensure that the main() function is only executed when the script is run directly (i.e., not when it's imported as a module by another script).

When you run this script, it will:
Prompt you to enter the Fernet key.
Prompt you to enter the encrypted message (ciphertext).
Decrypt the ciphertext using the provided key and print the decrypted plaintext to the console.

Note that the decrypt_message() function will raise an InvalidToken exception if the provided key is invalid or if the ciphertext is tampered with. You may want to add error handling to handle such cases.
