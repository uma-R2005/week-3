# Week 3 - Day 5 Projects: Unit Testing with pytest

This set of projects is designed to demonstrate **practical applications of Python unit testing** using the `pytest` framework.  
Each project represents a real-world inspired system with its own functionality, along with a dedicated test file that ensures correctness, error handling, and edge case coverage.

The goal of these exercises is to build confidence in writing clean, testable code and understanding the importance of automated testing in software development.

---

## Projects demonstrating pytest concepts:

### 🛒 `cart.py`
A shopping cart system that allows adding items and calculating totals.

- Add items to the cart with price.
- Compute the total price of items.
- Count the number of items in the cart.

**Test cases (`test_cart.py`)**:
- Verify adding a single item.
- Verify adding multiple items updates total correctly.
- Edge case: Adding item with zero/negative price (raises error).

---

### 🏦 `bank.py`
A bank account system for deposit and withdrawal operations.

- Deposit funds into an account.
- Withdraw funds if sufficient balance exists.
- Prevent invalid transactions (negative deposit/overdraw).

**Test cases (`test_bank.py`)**:
- Deposit increases balance.
- Withdraw decreases balance.
- Withdrawing more than available balance raises error.
- Depositing negative amount raises error.

---

### 🎓 `grades.py`
A grading system that manages students and their marks.

- Add marks for students.
- Calculate average marks.
- Assign grade (A, B, C, F) based on score.

**Test cases (`test_grades.py`)**:
- Add marks correctly.
- Compute average of multiple marks.
- Correctly assign grades based on marks.
- Handle case when no marks are added.

---

### 📚 `library.py`
A library system that manages books.

- Add books to the library.
- Remove books.
- Search for books by title.

**Test cases (`test_library.py`)**:
- Adding a duplicate book raises error.
- Removing a book decreases total count.
- Removing non-existent book raises error.
- Searching for a book returns correct result.

---

## Key Concepts Practiced
- Writing unit tests with `pytest`.
- Using `assert` statements to validate results.
- Testing for exceptions with `pytest.raises`.
- Structuring projects with separate `test_*.py` files.
- Automating test execution for multiple modules.

---

## How to Run

1. Install pytest:
   ```bash
   pip install pytest
