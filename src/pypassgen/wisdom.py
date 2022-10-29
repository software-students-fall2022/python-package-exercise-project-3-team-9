import random
import string
from cryptography.fernet import Fernet
from os import path


def getFile(fileName):
    """Returns the absolute path of a file."""
    return path.join(path.dirname(__file__), fileName)


def generate_password(length=8, num=0, upper=0, lower=0, special=0):
    """Generate a random password based on user input

    Keyword arguments:
        length -- the minimal length of the password to generate (default 8)
        num -- the minimal number of numeric characters required in the password (default 0)
        upper -- the minimal number of uppercase characters required in the password (default 0)
        lower -- the minimal number of lowercase characters required in the password (default 0)
        special -- the minimal number of special characters required in the password (default 0)
        
    Returns:
        A string containing the generated password
    """
    # Catch errors
    if length < 1 or num < 0 or upper < 0 or lower < 0 or special < 0:
        print("Invalid input. Please try again.")

    # all possible characters
    base = string.digits + string.ascii_letters + string.punctuation
    password = ""
    # add the required number of each character type
    if (num != 0):
        password += ''.join(random.choice(string.digits) for _ in range(num))
    if (upper != 0):
        password += ''.join(random.choice(string.ascii_uppercase)
                            for _ in range(upper))
    if (lower != 0):
        password += ''.join(random.choice(string.ascii_lowercase)
                            for _ in range(lower))
    if (special != 0):
        password += ''.join(random.choice(string.punctuation)
                            for _ in range(special))
    # generate the rest of the password if needed
    if (length - len(password) > 0):
        password += ''.join(random.choice(base)
                            for _ in range(length - len(password)))
    # shuffle the password
    password = ''.join(random.sample(password, len(password)))
    return password


def encryption(str):
    """Encrypt a string using Fernet encryption

    Keyword arguments:
        str -- the string to encrypt

    Returns:
        A string containing the encrypted and encoded string
    """
    arr = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z'
    ]
    str_encrypted = ""
    for char in str:
        if (char.isdigit() or char.isalpha()):
            idx = arr.index(char)
            str_encrypted += arr[(idx+5) % len(arr)]
        else:
            str_encrypted += char

    key = open(getFile("key.txt"), "rb").read()
    cipher_suite = Fernet(key)
    encoded_text = cipher_suite.encrypt(str_encrypted.encode('utf-8'))
    
    return encoded_text


def decryption(str):
    """Decrypt a string using Fernet decryption and shifting

    Keyword arguments:
        str -- the string to decrypt

    Returns:
        A string containing the decrypted and decooded string
    """
    #retreiving key from db + decrypting using Fernet
    key = open(getFile("key.txt"), "rb").read()
    cipher_suite = Fernet(key)
    str_decrypted = cipher_suite.decrypt(str.decode('utf-8'))

    arr = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z'
    ]
    #decoding decrypted text by shifting
    decoded_text= ""
    for char in str_decrypted:
        if (char.isdigit() or char.isalpha()):
            idx= arr.index(char)
            decoded_text += arr[(idx-5) % len(arr)]
        else:
            decoded_text += char

    return decoded_text
