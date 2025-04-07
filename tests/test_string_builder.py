#import relevant class
from lib.string_builder import StringBuilder

# test for empty string on initial instance creation
def test_string_builder_initial_empty():
    builder = StringBuilder()
    result = builder.output()
    assert result == "", 'returns empty string when nothing added to instance'

# test adding single string
def test_add_single_string():
    builder = StringBuilder()
    builder.add("Hello")
    result = builder.output()
    assert result == "Hello", 'returns "Hello" string when "Hello" added to instance'

# test adding multiple string
def test_add_multiple_strings():
    builder = StringBuilder()
    builder.add("Hello")
    builder.add(", World!")
    result = builder.output()
    assert result == "Hello, World!", 'returns "Hello, World!" string when "Hello" then ",World!" added to instance'

# test find length single string
def test_length_single_string():
    builder = StringBuilder()
    builder.add("Hello")
    result = builder.size()
    assert result == 5, 'size returns 5 string when "Hello" added'

# test find length multiple strings
def test_length_multiple_strings():
    builder = StringBuilder()
    builder.add("Hello")
    builder.add(", World!")
    result = builder.size()
    assert result == 13, 'returns size 13 when "Hello" then ",World!" added'