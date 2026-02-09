# Использование конструктора __init__
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        print(f"User {self.username} created.")

new_user = User("john_doe", "john@example.com")
