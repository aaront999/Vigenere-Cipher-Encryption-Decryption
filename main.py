# Vigenère cipher Encryption/Decryption Project 


text = input("Enter a message to encrypt: ")
secret_key = input("Enter your secret key: ")


def VigenereCypher(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for char in message:
        if not char.isalpha():                           # Append any non-letter character to the message
            result += char
        else:
            is_upper = char.isupper()                    # Determine if character is uppercase or lowercase
            while not key[key_index % len(key)].isalpha(): # While the character is not a letter, continue iterating
                key_index +=1
            key_char = key[key_index % len(key)].lower() # Find the right key character to encode/decode
            key_index += 1 
            index = alphabet.find(char.lower())
            offset = alphabet.index(key_char)            # Define the offset and the encrypted/decrypted letter
            new_index = (index + offset * direction) % len(alphabet)
            encrypt_char = alphabet[new_index]
            if is_upper:
                encrypt_char = encrypt_char.upper()      # Preserve original case if there is a capital letter
            result += encrypt_char

    return result


# Defining encrypt/decrypt function for better readability
def encrypt(message, key):
    return VigenereCypher(message, key)

def decrypt(message, key):
    return VigenereCypher(message, key, -1)


# test cases
# output results for ENCRYPTION
print(f'\nDecrypted text: {text}')
print(f'(Secret Key: {secret_key})')
print('_________________________')
encryption = encrypt(text, secret_key)
print(f'YOUR ENCRYPTED TEXT: {encryption}\n')


print('////////////////////////////')


# output results for DECRYPTION
print(f'\nEncrypted text: {encryption}')
print(f'(Secret Key: {secret_key})')
decryption = decrypt(encryption, secret_key)
print('_________________________')
print(f'SUCCESS! decrypted text: {decryption}')
