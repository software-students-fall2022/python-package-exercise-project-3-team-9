""" ------ TEST DECRYPTION ------ """
import random
import string
from cryptography.fernet import Fernet
from src.pypassgen import passwordpack


class Tests:
    # ------ TEST DECRYPTION ------
    def test_encrypted_empty_input(self):
        """
        Test encrypted empty input
        """
        key = open(passwordpack.get_file("key.txt"), "rb").read()
        cipher_suite = Fernet(key)
        encoded_str = cipher_suite.encrypt("".encode('utf-8')).decode('utf-8')
        decoded_str = passwordpack.decryption(encoded_str)
        assert decoded_str == ""

    def test_encrypted_lower_input(self):
        """
        Test encrypted lower case input
        """
        base = string.digits + string.ascii_letters
        arr = list(base)
        key = open(passwordpack.get_file("key.txt"), "rb").read()
        cipher_suite = Fernet(key)
        input_str = "".join(random.sample(
            string.ascii_lowercase, len(string.ascii_lowercase)))
        str_encrypted = ""
        for char in input_str:
            idx = arr.index(char)
            str_encrypted += arr[(idx+5) % len(arr)]
        encoded_str = cipher_suite.encrypt(
            str_encrypted.encode('utf-8')).decode('utf-8')
        decoded_str = passwordpack.decryption(encoded_str)
        assert decoded_str == input_str

    def test_encrypted_upper_input(self):
        """
        Test encrypted upper case input
        """
        base = string.digits + string.ascii_letters
        arr = list(base)
        key = open(passwordpack.get_file("key.txt"), "rb").read()
        cipher_suite = Fernet(key)
        input_str = "".join(random.sample(
            string.ascii_uppercase, len(string.ascii_uppercase)))
        str_encrypted = ""
        for char in input_str:
            idx = arr.index(char)
            str_encrypted += arr[(idx+5) % len(arr)]
        encoded_str = cipher_suite.encrypt(
            str_encrypted.encode('utf-8')).decode('utf-8')
        decoded_str = passwordpack.decryption(encoded_str)
        assert decoded_str == input_str

    def test_encrypted_num_input(self):
        """
        Test encrypted num input
        """
        base = string.digits + string.ascii_letters
        arr = list(base)
        key = open(passwordpack.get_file("key.txt"), "rb").read()
        cipher_suite = Fernet(key)
        input_str = "".join(random.sample(
            string.digits, len(string.digits)))
        str_encrypted = ""
        for char in input_str:
            idx = arr.index(char)
            str_encrypted += arr[(idx+5) % len(arr)]
        encoded_str = cipher_suite.encrypt(
            str_encrypted.encode('utf-8')).decode('utf-8')
        decoded_str = passwordpack.decryption(encoded_str)
        assert decoded_str == input_str

    def test_encrypted_special_input(self):
        """
        Test encrypted special characters
        """
        key = open(passwordpack.get_file("key.txt"), "rb").read()
        cipher_suite = Fernet(key)
        input_str = "".join(random.sample(
            string.punctuation, len(string.punctuation)))
        encoded_str = cipher_suite.encrypt(
            input_str.encode('utf-8')).decode('utf-8')
        decoded_str = passwordpack.decryption(encoded_str)
        assert decoded_str == input_str

    def test_encrypted_alphanumeric_input(self):
        """
        Test encrypted alphanumeric input
        """
        base = string.digits + string.ascii_letters
        arr = list(base)
        input_str = "".join(
            random.sample(
                string.ascii_letters + string.digits,
                len(string.ascii_letters + string.digits),
            )
        )
        # print("Input: " + input_str)
        str_encrypted = ""
        for char in input_str:
            idx = arr.index(char)
            str_encrypted += arr[(idx+5) % len(arr)]
        key = open(passwordpack.get_file("key.txt"), "rb").read()
        cipher_suite = Fernet(key)
        encoded_str = cipher_suite.encrypt(
            str_encrypted.encode('utf-8')).decode('utf-8')
        decoded_str = passwordpack.decryption(encoded_str)
        assert decoded_str == input_str

    def test_all_input(self):
        """
        Test encrypted random input
        """
        base = string.digits + string.ascii_letters
        arr = list(base)
        input_str = "".join(
            random.sample(
                string.ascii_letters + string.digits + string.punctuation,
                len(string.ascii_letters + string.digits + string.punctuation),
            )
        )
        # print("Input: " + input_str)
        str_encrypted = ""
        for char in input_str:
            if (char.isdigit() or char.isalpha()):
                idx = arr.index(char)
                str_encrypted += arr[(idx+5) % len(arr)]
            else:
                str_encrypted += char
        key = open(passwordpack.get_file("key.txt"), "rb").read()
        cipher_suite = Fernet(key)
        encoded_str = cipher_suite.encrypt(
            str_encrypted.encode('utf-8')).decode('utf-8')
        decoded_str = passwordpack.decryption(encoded_str)
        assert decoded_str == input_str

    def test_unencrypted_input(self):
        """
        Test unencrypted input
        """
        input_str = "".join(
            random.sample(
                string.ascii_letters + string.digits + string.punctuation,
                len(string.ascii_letters + string.digits + string.punctuation),
            )
        )
        assert passwordpack.decryption(
            input_str) == "ERROR: The entered phrase was not encrypted with pypassgen."
