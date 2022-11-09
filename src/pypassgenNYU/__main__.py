"""Main program page"""
from pypassgenNYU import passwordpack


def menu():
    """Prompt user menus """
    print("Welcome to pypassgen - your simple and lightweight password generator!")
    print("1. Generate a password")
    print("2. Verify a password")
    print("3. Encrypt a phrase")
    print("4. Decrypt an encrypted phrase")
    print("5. Exit")


def main():
    """The main program"""
    choice = ""
    while choice != "5":
        menu()
        # Prompt user to pick which function to use
        choice = input("Enter your choice (1 - 5): ")
        if choice == "1":
            default_length = 8
            default_digit = default_special = default_upper = default_lower = 1
            length = input(
                "Enter the minimal length of the password (default: 8): ")
            digit = input(
                "Enter the minimal number of numeric values needed (default: 1): ")
            upper = input(
                "Enter the minimal number of uppercase letters needed (default: 1): ")
            lower = input(
                "Enter the minimal number of lowercase letters needed (default: 1): ")
            special = input(
                "Enter the minimal number of special characters needed (default: 1): ")
            if length == "":
                length = default_length
            if digit == "":
                digit = default_digit
            if upper == "":
                upper = default_upper
            if lower == "":
                lower = default_lower
            if special == "":
                special = default_special
            print("Your password is: " + passwordpack.generate_password(int(length),
                  int(digit), int(upper), int(lower), int(special)) + "\n")
        elif choice == "2":
            pass_str = input("Enter your password: ")
            print(passwordpack.verify_type(passwordpack.verify_pass(pass_str), len(pass_str)))
            print()
        elif choice == "3":
            phrase = input("Enter the phrase to encrypt: ")
            print("Your encrypted phrase is: ",
                  passwordpack.encryption(phrase) + "\n")
        elif choice == "4":
            phrase = input("Enter the phrase to decrypt: ")
            print("Your decrypted phrase is: " +
                  passwordpack.decryption(phrase) + "\n")
        elif choice == "5":
            print("Goodbye!\n")
        else:
            print("Invalid choice. Please try again or enter 5 to exit.\n")


if __name__ == '__main__':
    main()
