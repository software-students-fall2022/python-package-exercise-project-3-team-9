from ast import Num
import src.pypassgen.wisdom as wisdom
import random


# ------ TEST GENERATE PASSWORD ------
def test_generate_password_default():
    # Test the default case
    assert len(wisdom.generate_password()) == 8


def test_generate_password_length():
    # Test the length parameter
    length = random.randint(1, 100)
    assert len(wisdom.generate_password(length, 1, 1, 1, 1)) == length


def test_generate_password_num():
    # Test the num parameter
    num = random.randint(1, 100)
    length = random.randint(1, 100)
    password = wisdom.generate_password(length, num, 0, 0, 0)
    assert len(password) >= num
    assert any(char.isdigit() for char in password)


def test_generate_password_upper():
    # Test the upper parameter
    upper = random.randint(1, 100)
    length = random.randint(1, 100)
    password = wisdom.generate_password(length, 0, upper, 0, 0)
    assert len(password) >= upper
    assert any(char.isupper() for char in password)


def test_generate_password_lower():
    # Test the lower parameter
    lower = random.randint(1, 100)
    length = random.randint(1, 100)
    password = wisdom.generate_password(length, 0, 0, lower, 0)
    assert len(password) >= lower
    assert any(char.islower() for char in password)


def test_generate_password_special():
    # Test the special parameter
    special = random.randint(1, 100)
    length = random.randint(1, 100)
    password = wisdom.generate_password(length, 0, 0, 0, special)
    assert len(password) >= special
    assert any(not char.isalnum() for char in password)


def test_generate_password_all_accuracy():
    # Test all parameters
    length = random.randint(1, 100)
    num = random.randint(1, 100)
    upper = random.randint(1, 100)
    lower = random.randint(1, 100)
    special = random.randint(1, 100)
    password = wisdom.generate_password(length, num, upper, lower, special)
    assert len(password) >= length
    assert any(char.isdigit() for char in password)
    assert any(char.isupper() for char in password)
    assert any(char.islower() for char in password)
    assert any(not char.isalnum() for char in password)


def test_generate_password_all_count():
    # Test all parameters
    length = random.randint(1, 100)
    num = random.randint(1, 100)
    upper = random.randint(1, 100)
    lower = random.randint(1, 100)
    special = random.randint(1, 100)
    password = wisdom.generate_password(length, num, upper, lower, special)
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
