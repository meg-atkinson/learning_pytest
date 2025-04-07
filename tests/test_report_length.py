from lib.report_length import report_length

#define test - for strings of varying length
def test_report_string_length(): 
    assert report_length("") == "This string was 0 characters long.", 'returns 0 if string is empty ""'
    assert report_length("Hello") == "This string was 5 characters long.", 'returns 5 if string is "hello"'
    assert report_length("This is amazing!") == "This string was 16 characters long.", 'returns 16 if string is "This is amazing!"'

