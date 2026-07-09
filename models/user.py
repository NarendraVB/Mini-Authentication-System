from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    username: str
    hashed_password: str
    created_at: str
    last_login: Optional[str] = None