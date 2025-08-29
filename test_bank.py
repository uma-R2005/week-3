import pytest
from bank import BankAccount

def test_deposit():
    acc = BankAccount("Alice", 100)
    acc.deposit(50)
    assert acc.balance == 150

def test_withdraw():
    acc = BankAccount("Bob", 200)
    acc.withdraw(100)
    assert acc.balance == 100

def test_withdraw_insufficient_balance():
    acc = BankAccount("Charlie", 50)
    with pytest.raises(ValueError, match="Insufficient balance"):
        acc.withdraw(100)

def test_deposit_negative_amount():
    acc = BankAccount("David", 100)
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        acc.deposit(-20)
