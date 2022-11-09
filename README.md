[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9088728&assignment_repo_type=AssignmentRepo)

![Workflow Status](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-9/actions/workflows/python-package.yml/badge.svg?event=push)
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

  - Enter the minimal number of different character types you want to include in your password (default is 1), or enter `0` to exclude them.

  - The generated password will be printed to the terminal.

- **_Verify a password:_**

  - When prompted, enter `2` to start the password verifier.

  - Enter the password you want to verify.

  - The package will print to the terminal whether the password is secure or not and what criteria it fulfills.

- **_Encrypt a string:_**

  - When prompted, enter `3` to start the encryption process.

  - Enter the string you want to encrypt.

  - The encrypted string will be printed to the terminal.

- **_Decrypt an encrypted string:_**

  - When prompted, enter `4` to start the decryption process.

  - Enter the encrypted string you want to decrypt.
  
  - The decrypted string will be printed to the terminal.

## Using the package as a module in a Python project

- Activate the virtual environment after installing the package:

  ```python
  pipenv shell
  ```

- Create a Python program that imports the package and its functions:

  ```python
  from pypassgen import passwordpack
  ```

### Functions

- **_Generate a password:_**

  - Call the `generate_password` function and pass the minimal length and minimal number of different character types as arguments,
  - Pass in `0` if you don't want the password to include specific character types.

    ```python
    # in pypassgen.passwordpack
    generate_password(length=8, num=1, upper=1, lower=1, special=1)
    ```

    For example:

    ```python
    # in your project
    password = passwordpack.generate_password(8, 2, 2, 2, 2)

    print(password)
    # Xq}tT/29
    ```

- **_Verify a password:_**

  - Call the `verify_password` function and pass the password you want to verify as an argument.

    ```python
    # in pypassgen.passwordpack
    verify_pass(password=None)
    verify_type(pass_type=[], length=0):
    ```

    For example:

    ```python
    # in your project
    password = "Xq}tT/29"

    print(passwordpack.verify_type(passwordpack.verify_pass(pass_str), len(pass_str)))
    # Very Strong Password
    # It has at least one uppercase, number, special character, lowercase.
    ```

- **_Encrypt a string:_**

  - Call the `encryption` function and pass the string to be encrypted as argument:

    ```python
    # in pypassgen.passwordpack
    encryption(str)
    ```

    For example:

    ```python
    # in your project
    encoded = passwordpack.encrypted = passwordpack.encryption("hello world!")

    print(encoded)
    # b'gAAAAABjXHQVlraVKy6okfj11o0h0AEqAG8caemLAKEdRCmsrO84_5iG_UatAna5JdWBjZWuJImP8f0K627DmeNkU1a3VlhFvg=='
    ```

- **_Decrypt an encrypted string:_**

  - Call the `decryption` function and pass the encrypted string as argument:

    ```python
    # in pypassgen.passwordpack
    decryption(str)
    ```

    For example:

    ```python
    # in your project
    decoded = passwordpack.decryption(encoded)

    print(decoded)
    # hello world!
    ```

## Contributors

[Darren Le](https://github.com/DarrenLe20)

[Daniel Atlas](https://github.com/Spectraorder)

[Vincent Xu](https://github.com/yx-xyc)

[Elyazya Al Kobaisi](https://github.com/elyazya)

## PyPI link to package
<https://test.pypi.org/project/pypassgenNYU/1.0.0/>
