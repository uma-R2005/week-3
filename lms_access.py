import functools

def requires_role(role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args):
            if user.get("role") != role:
                return f"Access denied: Requires {role}"
            return func(user, *args)
        return wrapper
    return decorator

def log_action(func):
    @functools.wraps(func)
    def wrapper(user, *args):
        print(f"User {user['name']} ({user.get('role')}) called {func.__name__}")
        return func(user, *args)
    return wrapper

@requires_role("teacher")
@log_action
def grade_quiz(user, student_name, score):
    return f"Graded {student_name}'s quiz with score {score}"

@requires_role("student")
@log_action
def submit_quiz(user, quiz_id):
    return f"{user['name']} submitted quiz {quiz_id}"

# Usage examples
teacher = {"name": "Mr. Smith", "role": "teacher"}
student = {"name": "Jane", "role": "student"}

print(grade_quiz(teacher, "Jane", 90))  # Allowed
print(submit_quiz(student, 101))        # Allowed
print(grade_quiz(student, "Jane", 90))  # Access denied
