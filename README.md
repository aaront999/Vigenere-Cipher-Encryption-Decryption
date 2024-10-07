## Vigenère cipher Encryption/Decryption Project

### Description:

The Vigenère cipher is a polyalphabetic encryption algorithm invented by the French cryptologist Blaise de Vigenère in the 16th century. It is based on a shift cipher to which is added the use of a keyword that changes the shift at each step.

### How it works: 

In order to cipher a text, take the first letter of the message and the first letter of the key, and add their value together (letters have a value depending on their rank in the alphabet, starting with 0). 

Example: To encrypt "CAR", and the key being "KEY" and the alphabet is ABCDEFGHIJKLMNOPQRSTUVWXYZ.

Example: Take the first letters of the plaintext C (value = 2) and of the key K (value = 10) and add them together (2+10=12), the letter with value 12 is M.

Continue with the next letter of the plaintext, and the next letter of the key. When arrived at the end of the key, go back to the first letter of the key.

### Decryption method: 

Please refer: https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Base.html

#
### Pro:

The Vigenère cipher is a polyalphabetic substitution cipher that rotates through different shifts, so the same plaintext letter will not always be encrypted to the same ciphertext letter. It is also more complex and secure than the Caesar cipher.

### Con:

The primary weakness of the Vigenère cipher is the repeating nature of its key. 
