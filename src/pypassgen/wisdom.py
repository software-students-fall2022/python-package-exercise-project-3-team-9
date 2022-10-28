import random


def generate_password(length=8, num=0, alpha=0, upper=0, lower=0):
    """Generate a random password based on user input

    Keyword arguments:
    length -- the minimal length of the password to generate (default 8)
    num -- the minimal number of numeric characters to be included in the password (default 0)
    alpha -- the minimal number of alphabetic characters to be included in the password (default 0)
    upper -- the minimal number of uppercase characters to be included in the password (default 0)
    lower -- the minimal number of lowercase characters to be included in the password (default 0)
    """
    # Catch errors
    if length < 8 or num < 0 or alpha < 0:
        print("Invalid input")
    if (upper + lower) > alpha:
        print("Error: The number of uppercase and lowercase characters cannot exceed the number of alphabetic characters")
