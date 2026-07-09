from datetime import datetime

from auth.validator import validate_username, validate_password
from database.storage import find_user, add_user
from models.user import User
from security.password_hasher import hash_password

def register(username: str, password: str) -> User:
    validate_username(username)
    validate_password(password)

    if find_user(username):
        raise ValueError("Username already exists.")

    hashed_password = hash_password(password)

    user = User(
        username=username,
        hashed_password=hashed_password,
        created_at=datetime.now().isoformat(),
        last_login=None,
    )

    add_user(user)

    return user