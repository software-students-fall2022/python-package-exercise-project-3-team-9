import random
import string


def generate_password(length=8, num=0, alpha=0, upper=0, lower=0, special=0):
    """Generate a random password based on user input

    Keyword arguments:
        length -- the minimal length of the password to generate (default 8)
        num -- the minimal number of numeric characters required in the password (default 0)
        alpha -- the minimal number of alphabetic characters required in the password (default 0)
        upper -- the minimal number of uppercase characters required in the password (default 0)
        lower -- the minimal number of lowercase characters required in the password (default 0)
        special -- the minimal number of special characters required in the password (default 0)
    Returns:
        A string containing the generated password
    """
    # Catch errors
    if length < 8 or num < 0 or alpha < 0 or upper < 0 or lower < 0 or special < 0:
        print("Invalid input. Please try again.")
    if (upper + lower) > alpha:
        print("Error: The number of uppercase and lowercase characters cannot exceed the number of alphabetic characters")

    # all possible characters
    base = string.digits + string.ascii_letters + string.punctuation
    password = ""
    print(base)


generate_password()
