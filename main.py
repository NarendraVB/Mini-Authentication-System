from auth.login import login
from auth.register import register
from getpass import getpass

def register_menu():
    username = input("Enter username: ")
    password = getpass("Enter password: ")

    try:
        user = register(username, password)
        print(f"User '{user.username}' registered successfully.")
    except ValueError as e:
        print(f"Error: {e}")


def login_menu():
    username = input("Enter username: ")
    password = getpass("Enter password: ")

    try:
        user = login(username, password)
        print(f"User '{user.username}' logged in successfully.")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    while True:
        print("\n===== Mini Authentication System =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register_menu()
        elif choice == "2":
            login_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()