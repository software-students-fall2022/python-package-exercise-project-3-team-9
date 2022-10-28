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
        choice = input("Enter your choice (1 - 5): ")
        if (choice == "1"):
            print("Your password is: " + wisdom.generate_password() + "\n")
        # elif (choice == "2"):
        # elif (choice == "3"):
        # elif (choice == "4"):
        elif (choice == "5"):
            print("Goodbye!\n")
        else:
            print("Invalid choice. Please try again or enter 5 to exit.\n")


if __name__ == '__main__':
    main()
