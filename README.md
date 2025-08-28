# Week 3 - Day 4 Projects: Decorators and functools Demonstrations

This set of projects is designed to showcase practical applications of Python decorators and the `functools` module in real-world inspired systems. Each script demonstrates how decorators can be used to enforce role-based access control, logging, authentication, rate limiting, error handling, caching, and more.

---

## Projects demonstrating decorators and functools concepts:

### `bank_system.py`

A banking system simulating core financial operations enhanced by decorators to:

- Log all function calls with input parameters and results for transparency.
- Restrict sensitive operations like loan approvals to users with the "manager" role.
- Gracefully handle errors during loan approval with informative messages.
- Demonstrates combining multiple decorators on class methods.
- Implements an interactive terminal interface for user and manager roles.

Key concepts:
- Decorating class methods, managing `self`.
- Layered decorators for logging, access control, and error handling.
- Use of `functools.wraps` to maintain function metadata.

---

### `ecommerce_platform.py`

Simulates a role-based e-commerce platform with:

- Role enforcement via decorators to restrict price updates to admins and order placement to customers.
- Action logging for every operation performed by users.
- Input validation for prices and order quantities.
- Menu-driven CLI interface adapting to user roles.

Key concepts:
- Stacking decorators to enforce roles and log actions.
- Handling variable function arguments in decorators.
- Real-time role checks and informative access denial.

---

### `lms_access.py`

A learning management system access control simulation featuring:

- Role-based restrictions for grading quizzes (teachers only) and quiz submissions (students only).
- Logging of actions to track user activity.
- Simple user role dictionaries to simulate authentication contexts.

Key concepts:
- Clean separation of roles using decorators.
- Dynamic enforcement of permissions at runtime.
- Use of `functools.wraps` for proper decorator implementation.

---

### `social_media.py`

Simulates core social media features with focus on:

- User authentication checks before allowing posts.
- Rate limiting posts to prevent spamming, using decorators with parameters.
- Combining authentication and rate limiting decorators.
- Tracking user post timestamps to enforce limits.

Key concepts:
- Creating parameterized decorators.
- Managing state inside decorators for rate limiting.
- Combining multiple decorators for robust access control.

---

## Core functools utilities used across projects:

- `functools.wraps`: Ensures wrapped functions retain original metadata like name and docstring.
- `functools.lru_cache` (mentioned conceptually): Used for caching to optimize repeated calls (demonstrated or expandable).
- Closures and higher-order functions for creating decorators with parameters.
- Managing decorator stacking and argument passing smoothly.

---

## Running the projects

Each project can be run independently from the command line:

```bash
python bank_system.py
python ecommerce_platform.py
python lms_access.py
python social_media.py
