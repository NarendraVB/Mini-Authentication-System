import pytest
from auth.register import register
from database.storage import clear_user

def test_successful_registration():
    clear_user()
    user = register("alice", "Password123!")

    assert user.username == "alice"
    assert user.last_login is None
    assert user.hashed_password != "Password123!"