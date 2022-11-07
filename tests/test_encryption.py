""" ------ TEST ENCRYPTION ------ """
import random
import string
from cryptography.fernet import Fernet
from src.pypassgen import wisdom


class Tests:
  # ------ TEST ENCRYPTION ------
    def test_empty_input(self):
        """
        Test empty input
        """
        key = open(wisdom.get_file("key.txt"), "rb").read()
        cipher_suite = Fernet(key)
        encoded_str = wisdom.encryption("")
        assert (cipher_suite.decrypt(
            encoded_str.encode("utf-8"))).decode("utf-8") == ""

    def test_special_input(self):
        """
        Test special characters
        """
        key = open(wisdom.get_file("key.txt"), "rb").read()
        cipher_suite = Fernet(key)
        input_str = "".join(random.sample(
            string.punctuation, len(string.punctuation)))
        encoded_str = wisdom.encryption(input_str)
        assert (cipher_suite.decrypt(encoded_str.encode("utf-8"))
                ).decode("utf-8") == input_str

    def test_alphanumeric_input(self):
        """
        Test random input
        """
        base = string.digits + string.ascii_letters
        arr = list(base)
        input_str = "".join(
            random.sample(
                string.ascii_letters + string.digits,
                len(string.ascii_letters + string.digits),
            )
        )
        print("Input: " + input_str)
        str_encrypted = ""
        for char in input_str:
            idx = arr.index(char)
            str_encrypted += arr[(idx+5) % len(arr)]
        key = open(wisdom.get_file("key.txt"), "rb").read()
        cipher_suite = Fernet(key)
        encoded_str = wisdom.encryption(input_str)
        assert (cipher_suite.decrypt(encoded_str.encode("utf-8"))
                ).decode("utf-8") == str_encrypted

    def test_all_input(self):
        """
        Test random input
        """
        base = string.digits + string.ascii_letters
        arr = list(base)
        input_str = "".join(
            random.sample(
                string.ascii_letters + string.digits + string.punctuation,
                len(string.ascii_letters + string.digits + string.punctuation),
            )
        )
        print("Input: " + input_str)
        str_encrypted = ""
        for char in input_str:
            if (char.isdigit() or char.isalpha()):
                idx = arr.index(char)
                str_encrypted += arr[(idx+5) % len(arr)]
            else:
                str_encrypted += char
        key = open(wisdom.get_file("key.txt"), "rb").read()
        cipher_suite = Fernet(key)
        encoded_str = wisdom.encryption(input_str)
        assert (cipher_suite.decrypt(encoded_str.encode("utf-8"))
                ).decode("utf-8") == str_encrypted

    def test_lower_input(self):
        """
        Test encrypted lower case input
        """
        base = string.digits + string.ascii_letters
        arr = list(base)
        input_str = "".join(random.sample(
            string.ascii_lowercase), len(string.ascii_lowercase))
        str_encrypted = ""
        for char in input_str:
            idx = arr.index(char)
            str_encrypted += arr[(idx+5) % len(arr)]
        key = open(wisdom.get_file("key.txt"), "rb").read()
        cipher_suite = Fernet(key)
        encoded_str = wisdom.encryption(input_str)
        assert (cipher_suite.decrypt(encoded_str.encode('utf-8'))).decode('utf-8') == str_encrypted
     
    def test_upper_input(self):
        """
        Test encrypted upper case input
        """
        base = string.digits + string.ascii_letters
        arr = list(base)
        input_str = "".join(random.sample(
            string.ascii_uppercase), len(string.ascii_uppercase))
        str_encrypted = ""
        for char in input_str:
            idx = arr.index(char)
            str_encrypted += arr[(idx+5) % len(arr)]
        key = open(wisdom.get_file("key.txt"), "rb").read()
        cipher_suite = Fernet(key)
        encoded_str = wisdom.encryption(input_str)
        assert (cipher_suite.decrypt(encoded_str.encode('utf-8'))
                ).decode('utf-8') == str_encrypted

    def test_num_input(self):
        """
        Test encrypted num input
        """
        base = string.digits + string.ascii_letters
        arr = list(base)
        input_str = "".join(random.sample(
            string.digits), len(string.digits))
        str_encrypted = ""
        for char in input_str:
            idx = arr.index(char)
            str_encrypted += arr[(idx+5) % len(arr)]
        key = open(wisdom.get_file("key.txt"), "rb").read()
        cipher_suite = Fernet(key)
        encoded_str = wisdom.encryption(input_str)
        assert (cipher_suite.decrypt(encoded_str.encode('utf-8'))
                ).decode('utf-8') == str_encrypted
