from factorial import factorial

# Assertion to test if factorial(0) returns 1
def test_factorial_zero():
    assert factorial(0) == 1

# Assertion to test if factorial(1) returns 1
def test_factorial_one():
    assert factorial(1) == 1

# Assertion to test if factorial(5) returns 120
def test_factorial_five():
    assert factorial(5) == 120

# Assertion to test if factorial(10) returns 3628800
def test_factorial_ten():
    assert factorial(10) == 3628800

#negative case
def test_factorial

# Assertion to test if attempting to calculate factorial of a negative number raises a ValueError
try:
    factorial(-1)
except ValueError as e:
    assert str(e) == "Factorial is undefined for negative numbers."

print("All assertions passed!")