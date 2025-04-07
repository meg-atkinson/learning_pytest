#import function to test
from lib.greet import greet

#create test example (must start with "test_" so pytest can find)
def test_greet_sarah():
    #running greet() with arg "Sarah" returns "Hello, Sarah!"
    result = greet("Sarah")
    assert result == "Hello, Sarah!"