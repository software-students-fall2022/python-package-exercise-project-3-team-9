""" ------ TEST DECRYPTION ------ """
import random
import string
from cryptography.fernet import Fernet
from src.pypassgen import wisdom


class Tests:
    # ------ TEST DECRYPTION ------
    def test_encrypted_lower_input(self):
        """
        Test encrypted lower case input
        """
        base = string.digits + string.ascii_letters
        arr = list(base)
        key = open(wisdom.get_file("key.txt"), "rb").read()
        cipher_suite = Fernet(key)
        input_str = "".join(random.sample(
            string.ascii_lowercase, len(string.ascii_lowercase)))
        str_encrypted = ""
        for char in input_str:
            idx = arr.index(char)
            str_encrypted += arr[(idx+5) % len(arr)]
        encoded_str = cipher_suite.encrypt(
            str_encrypted.encode('utf-8')).decode('utf-8')
        decoded_str = wisdom.decryption(encoded_str)
        assert decoded_str == input_str


    def test_encrypted_upper_input(self):
        """
        Test encrypted upper case input
        """
        base = string.digits + string.ascii_letters
        arr = list(base)
        key = open(wisdom.get_file("key.txt"), "rb").read()
        cipher_suite = Fernet(key)
        input_str = "".join(random.sample(
            string.ascii_uppercase, len(string.ascii_uppercase)))
        str_encrypted = ""
        for char in input_str:
            idx = arr.index(char)
            str_encrypted += arr[(idx+5) % len(arr)]
        encoded_str = cipher_suite.encrypt(
            str_encrypted.encode('utf-8')).decode('utf-8')
        decoded_str = wisdom.decryption(encoded_str)
        assert decoded_str == input_str

    def test_encrypted_num_input(self):
        """
        Test encrypted num input
        """
        base = string.digits + string.ascii_letters
        arr = list(base)
        key = open(wisdom.get_file("key.txt"), "rb").read()
        cipher_suite = Fernet(key)
        input_str = "".join(random.sample(
            string.digits, len(string.digits)))
        str_encrypted = ""
        for char in input_str:
            idx = arr.index(char)
            str_encrypted += arr[(idx+5) % len(arr)]
        encoded_str = cipher_suite.encrypt(
            str_encrypted.encode('utf-8')).decode('utf-8')
        decoded_str = wisdom.decryption(encoded_str)
        assert decoded_str == input_str