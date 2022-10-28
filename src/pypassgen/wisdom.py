import random
import string


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
    print(password)


generate_password()
