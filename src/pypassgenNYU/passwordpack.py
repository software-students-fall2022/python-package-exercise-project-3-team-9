"""Function Page"""
import random
import string
from os import path
import cryptography as crypto
from cryptography.fernet import Fernet


def get_file(file_name):
    """Returns the absolute path of a file."""
    return path.join(path.dirname(__file__), file_name)


def generate_password(length=8, num=1, upper=1, lower=1, special=1):
    """Generate a random password based on user input

    Keyword arguments:
        length -- the minimal length of the password to generate (default 8)
        num -- the minimal number of numeric characters required in the password (default 1)
        upper -- the minimal number of uppercase characters required in the password (default 1)
        lower -- the minimal number of lowercase characters required in the password (default 1)
        special -- the minimal number of special characters required in the password (default 1)

    Returns:
        A string containing the generated password
    """
    # Catch errors
    if length < 1 or num < 0 or upper < 0 or lower < 0 or special < 0:
        print("ERROR: Invalid input. Please try again.")
        return "ERROR: Password generation failed."
    elif num == 0 and upper == 0 and lower == 0 and special == 0:
        print("ERROR: Password must contain at least 1 type of character.")
        return "ERROR: Password generation failed."
    else:
        base = ""
        password = ""
        # add the required number of each character type
        if num != 0:
            base += string.digits
            password += ''.join(random.choice(string.digits)
                                for _ in range(num))
        if upper != 0:
            base += string.ascii_uppercase
            password += ''.join(random.choice(string.ascii_uppercase)
                                for _ in range(upper))
        if lower != 0:
            base += string.ascii_lowercase
            password += ''.join(random.choice(string.ascii_lowercase)
                                for _ in range(lower))
        if special != 0:
            base += string.punctuation
            password += ''.join(random.choice(string.punctuation)
                                for _ in range(special))
        # generate the rest of the password if needed
        if length - len(password) > 0:
            password += ''.join(random.choice(base)
                                for _ in range(length - len(password)))
        # shuffle the password
        password = ''.join(random.sample(password, len(password)))
        return password


def verify_pass(password=None):
    """Verify and determine what type of password the user is inputting

    Keyword arguments:
        password -- the string for password

    Returns:
        None if the input is invalid
        A list with codes:
        1 contains lowercase
        2 contains uppercase
        3 contains numbers
        4 contains special characters
    """
    if password is None:
        print("Invalid input. Please try again.")
        return None
    output = []
    for cur in password:
        if string.ascii_lowercase.__contains__(cur):
            try:
                pos = output.index(1)
            except:
                output.append(1)
        if string.ascii_uppercase.__contains__(cur):
            try:
                pos = output.index(2)
            except:
                output.append(2)
        if string.digits.__contains__(cur):
            try:
                pos = output.index(3)
            except:
                output.append(3)
        if string.punctuation.__contains__(cur):
            try:
                pos = output.index(4)
            except:
                output.append(4)
    return output


def verify_type(pass_type=[], length=0):
    """Verify and determine what type of password the user is inputting

    Keyword arguments:
        pass_type -- the type list for password

    Returns:
        pass_str -- the string for properties of password
    """
    if length == 0:
        print("Invalid input. Please try again.")
        return ''
    if len(pass_type) == 4 and length >= 8:
        print("Very Strong Password")
    elif len(pass_type) >= 2 and length >= 6:
        print("Strong Password")
    else:
        print("Weak Password")
    pass_str = 'It has at least one '
    for cur in pass_type:
        if cur == 1:
            pass_str += 'lowercase'
        if cur == 2:
            pass_str += 'uppercase'
        if cur == 3:
            pass_str += 'number'
        if cur == 4:
            pass_str += 'special character'
        if cur == pass_type[len(pass_type)-1]:
            pass_str += '.'
        else:
            pass_str += ', '
    return pass_str


def encryption(origin_password):
    """Encrypt a string using Fernet encryption

    Keyword arguments:
        str -- the string to encrypt

    Returns:
        A string containing the encrypted and encoded string
    """
    base = string.digits + string.ascii_letters
    arr = list(base)
    str_encrypted = ""
    for char in origin_password:
        if (char.isdigit() or char.isalpha()):
            idx = arr.index(char)
            str_encrypted += arr[(idx+5) % len(arr)]
        else:
            str_encrypted += char

    # key = open(get_file("key.txt"), "rb").read()
    key = "9JLx_ipNCkFmSsSNrb4YdFbZuaQqOJbWMIk0ONnI7rU="
    cipher_suite = Fernet(key)
    encoded_text = cipher_suite.encrypt(
        str_encrypted.encode('utf-8')).decode('utf-8')

    return encoded_text


def decryption(decrypted_password):
    """Decrypt a string using Fernet decryption and shifting

    Keyword arguments:
        str -- the string to decrypt

    Returns:
        A string containing the decrypted and decooded string
    """
    # retrieving key from db + decrypting using Fernet
    # key = open(get_file("key.txt"), "rb").read()
    key = "9JLx_ipNCkFmSsSNrb4YdFbZuaQqOJbWMIk0ONnI7rU="
    cipher_suite = Fernet(key)
    try:
        str_decrypted = (cipher_suite.decrypt(decrypted_password.encode('utf-8'))).decode('utf-8')
    except (crypto.fernet.InvalidToken, TypeError):
        return "ERROR: The entered phrase was not encrypted with pypassgen."
    base = string.digits + string.ascii_letters
    arr = list(base)
    # decoding decrypted text by shifting
    decoded_text = ""
    for char in str_decrypted:
        if (char.isdigit() or char.isalpha()):
            idx = arr.index(char)
            decoded_text += arr[(idx-5) % len(arr)]
        else:
            decoded_text += char
    return decoded_text
