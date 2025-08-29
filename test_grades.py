import pytest
from grades import Student

def test_add_valid_marks():
    s = Student("John")
    s.add_mark(85)
    s.add_mark(90)
    assert s.marks == [85, 90]

def test_add_invalid_marks():
    s = Student("John")
    with pytest.raises(ValueError, match="Mark must be between 0 and 100"):
        s.add_mark(120)

def test_average():
    s = Student("Alice")
    s.add_mark(80)
    s.add_mark(100)
    assert s.average() == 90

def test_grade_A():
    s = Student("Bob")
    s.add_mark(95)
    s.add_mark(92)
    assert s.grade() == "A"

def test_grade_F():
    s = Student("Charlie")
    s.add_mark(30)
    s.add_mark(40)
    assert s.grade() == "F"
