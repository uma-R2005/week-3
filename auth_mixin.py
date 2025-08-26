class AuthMixin:
    def login(self, username, password):
        # Simple hardcoded check for demo purposes
        if username == "admin" and password == "secret":
            self.logged_in = True
            return "Login successful!"
        else:
            self.logged_in = False
            return "Login failed!"

    def check_permission(self, permission):
        # Hardcoded permissions for demo
        if not getattr(self, 'logged_in', False):
            return "Access denied: User not logged in."
        permissions = {
            "admin": ["read", "write", "delete"],
            "user": ["read"]
        }
        user_role = getattr(self, "role", "user")
        if permission in permissions.get(user_role, []):
            return f"Permission '{permission}' granted."
        else:
            return f"Permission '{permission}' denied."

class User(AuthMixin):
    def __init__(self, role="user"):
        self.role = role
        self.logged_in = False

# Usage:
username = input("Username: ")
password = input("Password: ")

user = User(role="admin" if username=="admin" else "user")
print(user.login(username, password))

perm = input("Enter permission to check (read/write/delete): ")
print(user.check_permission(perm))
