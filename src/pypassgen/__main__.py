import wisdom as wisdom


def menu():
    print("Welcome to pypassgen - your simple and lightweight password generator!")
    # Prompt user to enter a pick which function to use
    print("1. Generate a password")
    print("2. Verify a password")
    print("3. Encrypt a phrase")
    print("4. Decrypt an encrypted phrase")
    print("5. Exit")


def main():
    choice = ""
    while choice != "5":
        menu()
        choice = input("Enter your choice: ")
        if (choice == "1"):
            print("Your password is: " + wisdom.generate_password() + "\n")


if __name__ == '__main__':
    main()
