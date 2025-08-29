import pytest
from cart import Cart

def test_add_item():
    cart = Cart()
    cart.add_item("Book", 200)
    assert cart.item_count() == 1
    assert cart.total() == 200

def test_multiple_items():
    cart = Cart()
    cart.add_item("Book", 200)
    cart.add_item("Pen", 20)
    assert cart.item_count() == 2
    assert cart.total() == 220
