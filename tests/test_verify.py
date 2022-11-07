import src.pypassgen.passwordpack as passwordpack
import random

# ------ TEST VERIFICATION ------


class Tests:
    def test_verify_very_strong(self):
        length = random.randint(8, 100)
        num = random.randint(1, 100)
        upper = random.randint(1, 100)
        lower = random.randint(1, 100)
        special = random.randint(1, 100)
        password = wisdom.generate_password(length, num, upper, lower, special)
        assert wisdom.verify_type(wisdom.verify_pass(password), len(password))

    def test_verify_strong_withoutnum(self):
        length = random.randint(6, 7)
        upper = random.randint(1, 100)
        lower = random.randint(1, 100)
        special = random.randint(1, 100)
        password = wisdom.generate_password(length, 0, upper, lower, special)
        assert wisdom.verify_type(wisdom.verify_pass(password), len(password))

    def test_verify_strong_withoutupper(self):
        length = random.randint(6, 7)
        num = random.randint(1, 100)
        lower = random.randint(1, 100)
        special = random.randint(1, 100)
        password = wisdom.generate_password(length, num, 0, lower, special)
        assert wisdom.verify_type(wisdom.verify_pass(password), len(password))

    def test_verify_strong_withoutlower(self):
        length = random.randint(6, 7)
        num = random.randint(1, 100)
        upper = random.randint(1, 100)
        special = random.randint(1, 100)
        password = wisdom.generate_password(length, num, upper, 0, special)
        assert wisdom.verify_type(wisdom.verify_pass(password), len(password))

    def test_verify_strong_withoutspecial(self):
        length = random.randint(6, 7)
        num = random.randint(1, 100)
        upper = random.randint(1, 100)
        lower = random.randint(1, 100)
        password = wisdom.generate_password(length, num, upper, lower, 0)
        assert wisdom.verify_type(wisdom.verify_pass(password), len(password))

    def test_verify_weak(self):
        length = random.randint(1, 5)
        num = random.randint(1, 100)
        upper = random.randint(1, 100)
        lower = random.randint(1, 100)
        special = random.randint(1, 100)
        password = wisdom.generate_password(length, num, upper, lower, special)
        assert wisdom.verify_type(wisdom.verify_pass(password), len(password))
