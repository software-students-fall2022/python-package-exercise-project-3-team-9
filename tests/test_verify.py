import src.pypassgen.passwordpack as passwordpack
import random

# ------ TEST VERIFICATION ------
def test_verify_very_strong():
    length = random.randint(8, 100)
    num = random.randint(1, 100)
    upper = random.randint(1, 100)
    lower = random.randint(1, 100)
    special = random.randint(1, 100)
    password = passwordpack.generate_password(length, num, upper, lower, special)
    assert passwordpack.verify_type(passwordpack.verify_pass(password), len(password))


def test_verify_strong_withoutnum():
    length = random.randint(6, 7)
    upper = random.randint(1, 100)
    lower = random.randint(1, 100)
    special = random.randint(1, 100)
    password = passwordpack.generate_password(length, 0, upper, lower, special)
    assert passwordpack.verify_type(passwordpack.verify_pass(password), len(password))


def test_verify_strong_withoutupper():
    length = random.randint(6, 7)
    num = random.randint(1, 100)
    lower = random.randint(1, 100)
    special = random.randint(1, 100)
    password = passwordpack.generate_password(length, num, 0, lower, special)
    assert passwordpack.verify_type(passwordpack.verify_pass(password), len(password))


def test_verify_strong_withoutlower():
    length = random.randint(6, 7)
    num = random.randint(1, 100)
    upper = random.randint(1, 100)
    special = random.randint(1, 100)
    password = passwordpack.generate_password(length, num, upper, 0, special)
    assert passwordpack.verify_type(passwordpack.verify_pass(password), len(password))


def test_verify_strong_withoutspecial():
    length = random.randint(6, 7)
    num = random.randint(1, 100)
    upper = random.randint(1, 100)
    lower = random.randint(1, 100)
    password = passwordpack.generate_password(length, num, upper, lower, 0)
    assert passwordpack.verify_type(passwordpack.verify_pass(password), len(password))


def test_verify_weak():
    length = random.randint(1, 5)
    num = random.randint(1, 100)
    upper = random.randint(1, 100)
    lower = random.randint(1, 100)
    special = random.randint(1, 100)
    password = passwordpack.generate_password(length, num, upper, lower, special)
    assert passwordpack.verify_type(passwordpack.verify_pass(password), len(password))
