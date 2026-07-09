import re


def validate_username(username: str) -> None:
    if not username:
        raise ValueError("Username cannot be empty.")

    if len(username) < 3:
        raise ValueError("Username must be at least 3 characters long.")

    if len(username) > 15:
        raise ValueError("Username cannot exceed 15 characters.")

    if not re.match(r"^[a-zA-Z0-9_]+$", username):
        raise ValueError(
            "Username can only contain letters, numbers, and underscores."
        )
    
    

def validate_password(password: str) -> None:
    if not password:
        raise ValueError("Password cannot be empty.")

    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters long.")

    if len(password) > 20:
        raise ValueError("Password cannot exceed 20 characters.")

    if not re.search(r"[A-Z]", password):
        raise ValueError("Password must contain at least one uppercase letter.")

    if not re.search(r"[a-z]", password):
        raise ValueError("Password must contain at least one lowercase letter.")

    if not re.search(r"[0-9]", password):
        raise ValueError("Password must contain at least one digit.")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise ValueError(
            "Password must contain at least one special character (!@#$%^&*(),.?\":{}|<>)."
        )
    
    