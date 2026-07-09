import json
from dataclasses import asdict
from pathlib import Path

from models.user import User

DATA_FILE = Path(__file__).parent / "users.json"

def load_users() -> list[User]:
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as file:
        data = json.load(file)

    return [User(**user) for user in data]


def save_users(users: list[User]) -> None:
    with open(DATA_FILE, "w") as file:
        json.dump([asdict(user) for user in users], file, indent=4)


def find_user(username: str) -> User | None:
    users = load_users()
    for user in users:
        if user.username == username:
            return user
    return None

def add_user(user: User) -> None:
    users = load_users()
    users.append(user)
    save_users(users)

def update_user(updated_user: User) -> None:
    users = load_users()
    for i, user in enumerate(users):
        if user.username == updated_user.username:
            users[i] = updated_user
            break
    save_users(users)