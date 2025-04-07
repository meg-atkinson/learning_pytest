#import class and pytest
import pytest
from lib.present import Present

#define tests

#test for output if add contents to wrap
def test_add_contents_to_wrap():
    present = Present()
    present.wrap("book")
    assert present.contents == "book"

#test for output if add contents and unwrap
def test_contents_not_none_unwrapped():
    present = Present()
    present.wrap("book")
    present.unwrap()
    assert present.contents == "book"

#test for error output if already contents wrapped
def test_error_contents_already_wrapped():
    present = Present()
    present.wrap("book")
    with pytest.raises(Exception) as e:
        present.wrap("necklace")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

#test for that if try to wrap again where there is already wrapped present, that contents is not overwritten  
def test_existing_contents_not_replaced():
    present = Present()
    present.wrap("book")
    with pytest.raises(Exception) as e:
        present.wrap("necklace")
    assert present.unwrap() == "book"

#test for output if no contents to unwrap
def test_error_no_contents_to_unwrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."