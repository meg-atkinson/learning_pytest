#import function to test
from lib.check_codeword import check_codeword

#define test - for correct code word
def test_with_correct_codeword(): 
    result = check_codeword("horse")
    assert result == "Correct! Come in.", 'returns "Correct! Come in." if word is "horse"'

#define test - for close code word 
def test_with_close_codeword(): 
    result = check_codeword("house")
    assert result == "Close, but nope.", 'returns "Close, but nope." if word is "herse"'

#define test - for wrong code word 
def test_with_wrong_codeword(): 
    result = check_codeword("help")
    assert result == "WRONG!", 'returns "WRONG!" if word is "help"'