import functools
import time

def authenticate(func):
    @functools.wraps(func)
    def wrapper(user, *args):
        if not user.get("authenticated", False):
            return "User not authenticated"
        return func(user, *args)
    return wrapper

def rate_limit(calls_per_minute):
    interval = 60 / calls_per_minute
    def decorator(func):
        last_called = {}
        @functools.wraps(func)
        def wrapper(user, *args):
            now = time.time()
            user_id = user.get("id")
            last_time = last_called.get(user_id, 0)
            if now - last_time < interval:
                return "Rate limit exceeded"
            last_called[user_id] = now
            return func(user, *args)
        return wrapper
    return decorator

@authenticate
@rate_limit(2)  # max 2 posts per minute
def post_message(user, message):
    return f"{user['name']} posted: {message}"

# Usage example
user = {"id": 1, "name": "Alice", "authenticated": True}
print(post_message(user, "Hello world!"))
