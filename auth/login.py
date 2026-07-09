from datetime import datetime

from database.storage import find_user, update_user
from models.user import User
from security.password_hasher import verify_password

def login(username: str, password: str) -> User:
    user = find_user(username)

    if user is None:
        raise ValueError("Invalid username or password.")

    if not verify_password(password, user.hashed_password):
        raise ValueError("Invalid username or password.")

    user.last_login = datetime.now().isoformat()
    update_user(user)

    return user