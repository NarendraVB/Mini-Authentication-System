from auth.login import login


user = login("Narendra", "Password123!")
print(user.last_login)