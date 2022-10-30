[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9088728&assignment_repo_type=AssignmentRepo)

# Python Package Exercise

A little exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

## Pypassgen - A simple password generator

Pypassgen has 4 functions that assist the user in creating their passwords:

1. Generating a random password based on the user's input criteria (e.g., all numeric, all alphabetic, uppercase, etc.)

2. Verify if a user's entered password is secure.

3. Encrypt the user's input string into a secured password based on the package's specific encryption rules.

4. Decrypt the user's encrypted password back to its original form provided that the password was orginally encrypted by pypassgen.

## Installation

- Create a `pipenv`-managed environment.

- Run the following command to install the lastest version of the package:

  ```bash
  pipenv install -i https://test.pypi.org/simple/ pypassgen==1.0.0
  ```

## Running package directly from the command line

- **_Initializing the package:_**

  - Run the following command in the terminal:

    ```python
    python -m pypassgen
    ```

  - This will initialize the package and prompt the user to choose their desired function.
    ```bash
    Welcome to pypassgen - your simple and lightweight password generator!
    1. Generate a password
    2. Verify a password
    3. Encrypt a phrase
    4. Decrypt an encrypted phrase
    5. Exit
    Enter your choice (1 - 5):
    ```

- **_Generate a password:_**

  - When prompted, enter `1` to start the password generator.

  - Enter the minimal length of the password you want to generate. (default is 8)

  - Enter the minimal number of different character types you want to include in your password.

- **_Verify a password:_**

  - When prompted, enter `2` to start the password verifier.

  - Enter the password you want to verify.

- **_Encrypt a string:_**

  - When prompted, enter `3` to start the encryption process.

  - Enter the string you want to encrypt.

- **_Decrypt an encrypted string:_**

  - When prompted, enter `4` to start the decryption process.

  - Enter the encrypted string you want to decrypt.

## Using the package as a module in a Python project

- Activate the virtual environment after installing the package:

  ```python
  pipenv shell
  ```

- Create a Python program that imports the package and its functions:

  ```python
  from pypassgen import wisdom
  ```

### Functions

- **_Generate a password:_**

  - Call the `generate_password` function and pass the minimal length and minimal number of different character types as arguments:

    ```python
    # in pypassgen.wisdom
    generate_password(length=8, num=0, upper=0, lower=0, special=0)
    ```

    For example:

    ```python
    # in your project
    password = wisdom.generate_password(length=8, num=2, upper=2, lower=2, special=2)

    print(password)
    # C0?8yOa)
    ```

- **_Verify a password:_**

- **_Encrypt a string:_**

  - Call the `encryption` function and pass the string to be encrypted as argument:

    ```python
    # in pypassgen.wisdom
    encryption(str)
    ```

    For example:

    ```python
    # in your project
    encoded = wisdom.encrypted = wisdom.encryption("hello world!")

    print(encoded)
    # b'gAAAAABjXHQVlraVKy6okfj11o0h0AEqAG8caemLAKEdRCmsrO84_5iG_UatAna5JdWBjZWuJImP8f0K627DmeNkU1a3VlhFvg=='
    ```

- **_Decrypt an encrypted string:_**

## Contributors

[Darren Le](https://github.com/DarrenLe20)

[Daniel Atlas](https://github.com/Spectraorder)

[Vincent Xu](https://github.com/yx-xyc)

[Elyazya Al Kobaisi](https://github.com/elyazya)

## PyPI link to package
