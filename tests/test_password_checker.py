import pytest
from lib.password_checker import *

#def test password valid (8 or more characters)
def test_password_is_valid():
    checker = PasswordChecker()
    assert checker.check("password") == True 

#def test error when password less than 8 characters
def test_error_password_invalid_length():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check("hello") 
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
