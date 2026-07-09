import pytest
from auth.register import register
from database.storage import clear_user
from auth.login import login

def test_successful_registration():
    clear_user()
    user = register("alice", "Password123!")

    assert user.username == "alice"
    assert user.last_login is None
    assert user.hashed_password != "Password123!"

def test_duplicate_username():
    clear_user()

    register("alice", "Password123!")

    with pytest.raises(ValueError, match="Username already exists."):
        register("alice", "AnotherPassword123!")


def test_invalid_username():
    clear_user()

    with pytest.raises(ValueError):
        register("alice","123")

def test_invalid_password():
    clear_user()

    with pytest.raises(ValueError):
        register("alice","123")

def test_successful_login():
    clear_user()

    register("alice", "Password123!")

    user = login("alice", "Password123!")

    assert user.username == "alice"
    assert user.last_login is not None



def test_wrong_password():
    clear_user()

    register("alice", "Password123!")

    with pytest.raises(ValueError, match="Invalid username or password."):
        login("alice", "WrongPassword123!")

def test_unknown_user():
    clear_user()

    with pytest.raises(ValueError, match="Invalid username or password."):
        login("bob", "Password123!")