import pytest
from library import Library

def test_add_book():
    lib = Library()
    lib.add_book("Python Basics")
    assert lib.total_books() == 1
    assert lib.search_book("Python Basics")

def test_add_duplicate_book():
    lib = Library()
    lib.add_book("Data Science")
    with pytest.raises(ValueError, match="Book already exists"):
        lib.add_book("Data Science")

def test_remove_book():
    lib = Library()
    lib.add_book("AI Fundamentals")
    lib.remove_book("AI Fundamentals")
    assert lib.total_books() == 0

def test_remove_nonexistent_book():
    lib = Library()
    with pytest.raises(ValueError, match="Book not found"):
        lib.remove_book("Machine Learning")

def test_search_book():
    lib = Library()
    lib.add_book("Deep Learning")
    assert lib.search_book("Deep Learning")
    assert not lib.search_book("Blockchain")
