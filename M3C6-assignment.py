# M3C6-assignment.py


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


# Creating an object of the User class
user = User("John Snow", "thenorth123")

print("Username:", user.username)
print("Password:", user.password)
