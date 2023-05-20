import random
import cowsay
import pytest
from project import validate_name
from project import value
from project import simulate_answer

def main():
    test_validate_name()
    test_value()
    test_simulate_answer()

def test_validate_name():
    assert validate_name("Taylor Twift") == ("Taylor", "Twift")
    assert validate_name("Jenny Kenny") == ("Jenny", "Kenny")

def test_value():
    assert value("hello") == 100
    assert value("hi") == 50
    assert value("no, thank you. ") == 0

def test_simulate_answer():
    assert simulate_answer("wolfsbane") == False
    assert simulate_answer("I don't know") == False
    assert simulate_answer("dragon's blood") == True

if __name__ == "__main__":
    main()