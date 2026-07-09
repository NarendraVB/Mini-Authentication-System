from security.password_hasher import hash_password, verify_password

hashed = hash_password("MyPassword123!")

print(hashed)
print(verify_password("MyPassword123!", hashed))
print(verify_password("WrongPassword", hashed))