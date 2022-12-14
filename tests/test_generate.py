import src.pypassgenNYU.passwordpack as passwordpack
import random


# ------ TEST GENERATE PASSWORD ------
class Tests:
    def test_generate_password_default(self):
        # Test the default case
        password = passwordpack.generate_password()
        assert len(password) >= 8
        assert any(char.isdigit() for char in password)
        assert any(char.isupper() for char in password)
        assert any(char.islower() for char in password)
        assert any(not char.isalnum() for char in password)

    def test_generate_password_num(self):
        # Test the num parameter
        num = random.randint(1, 100)
        length = random.randint(1, 100)
        password = passwordpack.generate_password(length, num, 0, 0, 0)
        count = 0
        for char in password:
            if char.isdigit():
                count += 1
        assert len(password) <= count
        assert any(char.isdigit() for char in password)

    def test_generate_password_lower(self):
        # Test the lower parameter
        lower = random.randint(1, 100)
        length = random.randint(1, 100)
        password = passwordpack.generate_password(length, 0, 0, lower, 0)
        count = 0
        for char in password:
            if char.islower():
                count += 1
        assert len(password) <= count
        assert any(char.islower() for char in password)

    def test_generate_password_upper(self):
        # Test the upper parameter
        upper = random.randint(1, 100)
        length = random.randint(1, 100)
        password = passwordpack.generate_password(length, 0, upper, 0, 0)
        count = 0
        for char in password:
            if char.isupper():
                count += 1
        assert len(password) <= count
        assert any(char.isupper() for char in password)

    def test_generate_password_all_accuracy(self):
        # Test all parameters
        length = random.randint(1, 100)
        num = random.randint(1, 100)
        upper = random.randint(1, 100)
        lower = random.randint(1, 100)
        special = random.randint(1, 100)
        password = passwordpack.generate_password(
            length, num, upper, lower, special)

        assert len(password) >= length
        assert any(char.isdigit() for char in password)
        assert any(char.isupper() for char in password)
        assert any(char.islower() for char in password)
        assert any(not char.isalnum() for char in password)

    def test_generate_password_special(self):
        # Test the special parameter
        special = random.randint(1, 100)
        length = random.randint(1, 100)
        password = passwordpack.generate_password(length, 0, 0, 0, special)
        count = 0
        for char in password:
            if not char.isalnum():
                count += 1
        assert len(password) <= count
        assert any(not char.isalnum() for char in password)

    def test_generate_password_all_accuracy(self):
        # Test all parameters
        length = random.randint(1, 100)
        num = random.randint(1, 100)
        upper = random.randint(1, 100)
        lower = random.randint(1, 100)
        special = random.randint(1, 100)
        password = passwordpack.generate_password(
            length, num, upper, lower, special)

        assert len(password) >= length
        assert any(char.isdigit() for char in password)
        assert any(char.isupper() for char in password)
        assert any(char.islower() for char in password)
        assert any(not char.isalnum() for char in password)

    def test_generate_password_all_count(self):
        # Test all parameters
        length = random.randint(1, 100)
        num = random.randint(1, 100)
        upper = random.randint(1, 100)
        lower = random.randint(1, 100)
        special = random.randint(1, 100)

        password = passwordpack.generate_password(
            length, num, upper, lower, special)

        # Check that the password contains at least the required number of each character type
        count_digit = count_upper = count_lower = count_special = 0
        for char in password:
            if char.isdigit():
                count_digit += 1
            if char.isupper():
                count_upper += 1
            if char.islower():
                count_lower += 1
            if not char.isalnum():
                count_special += 1
        assert count_digit >= num
        assert count_upper >= upper
        assert count_lower >= lower
        assert count_special >= special

    def test_failure(self):
        length = random.randint(1, 100)
        assert passwordpack.generate_password(
            length, 0, 0, 0, 0) == "ERROR: Password generation failed."

    def test_failure_2(self):
        assert passwordpack.generate_password(
            0, -1, -1, -1, -2) == "ERROR: Password generation failed."
