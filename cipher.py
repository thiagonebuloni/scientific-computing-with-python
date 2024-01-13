text: str = 'mrttaqrhknsw ih puggrur'
custom_key: str = 'python'

def vigenere(message: str, key: str, direction: int = 1) -> str:
    key_index: int = 0
    alphabet: str = 'abcdefghijklmnopqrstuvwxyz'
    final_message: str = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset: int = alphabet.index(key_char)
            index: int = alphabet.find(char)
            new_index: int = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message: str, key: str) -> str:
    return vigenere(message, key)
    
def decrypt(message: str, key: str) -> str:
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption: str = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
