import src.pypassgen.wisdom as wisdom
from cryptography.fernet import Fernet
import random
import string


# ------ TEST ENCRYPTION ------
def test_empty_input():
    # Test empty input
    key = open(wisdom.getFile("key.txt"), "rb").read()
    cipher_suite = Fernet(key)
    encoded = wisdom.encryption("")
    assert (cipher_suite.decrypt(encoded)).decode("utf-8") == ""


def test_special_input():
    # Test special characters
    key = open(wisdom.getFile("key.txt"), "rb").read()
    cipher_suite = Fernet(key)
    input = "".join(random.sample(string.punctuation, len(string.punctuation)))
    encoded = wisdom.encryption(input)
    assert (cipher_suite.decrypt(encoded)).decode("utf-8") == input


def test_alphanumeric_input():
    # Test random input
    base = string.digits + string.ascii_letters
    arr = list(base)
    input = "".join(
        random.sample(
            string.ascii_letters + string.digits,
            len(string.ascii_letters + string.digits),
        )
    )
    print("Input: " + input)
    str_encrypted = ""
    for char in input:
        idx = arr.index(char)
        str_encrypted += arr[(idx+5) % len(arr)]
    key = open(wisdom.getFile("key.txt"), "rb").read()
    cipher_suite = Fernet(key)
    encoded = wisdom.encryption(input)
    assert (cipher_suite.decrypt(encoded)).decode('utf-8') == str_encrypted


def test_all_input():
  # Test random input
    base = string.digits + string.ascii_letters
    arr = list(base)
    input = "".join(
        random.sample(
            string.ascii_letters + string.digits + string.punctuation,
            len(string.ascii_letters + string.digits + string.punctuation),
        )
    )
    print("Input: " + input)
    str_encrypted = ""
    for char in input:
        if (char.isdigit() or char.isalpha()):
            idx = arr.index(char)
            str_encrypted += arr[(idx+5) % len(arr)]
        else:
            str_encrypted += char
    key = open(wisdom.getFile("key.txt"), "rb").read()
    cipher_suite = Fernet(key)
    encoded = wisdom.encryption(input)
    assert (cipher_suite.decrypt(encoded)).decode('utf-8') == str_encrypted
