# import class needed
from lib.counter import *

#define test for single add
def test_counter_add_single_number():
    new_counter = Counter()
    new_counter.add(10)
    result = new_counter.report()
    assert result == "Counted to 10 so far.", 'returns "Counted to 10 so far." if add 10 and report'

#define test for adding multiple numbers
def test_counter_add_multiple_numbers():
    new_counter = Counter()
    new_counter.add(15)
    new_counter.add(3)
    new_counter.add(10)
    result = new_counter.report() 
    assert result == "Counted to 28 so far.", 'returns "Counted to 28 so far." if add 15, then 3, then 10'

#define test for adding negative numbers
def test_counter_add_negative_num():
    new_counter = Counter()
    new_counter.add(-5)
    result = new_counter.report() 
    assert result == "Counted to -5 so far.", 'returns "Counted to -5 so far." if add 15, then 3, then 10'

def test_counter_add_and_report_in_stages():
    new_counter = Counter()
    new_counter.add(15)
    result = new_counter.report() 
    assert result == "Counted to 15 so far.", 'returns "Counted to 15 so far." if add 15 and report'
    new_counter.add(3)
    result = new_counter.report() 
    assert result == "Counted to 18 so far.", 'returns "Counted to 18 so far." if add further 3 and rereport'
    new_counter.add(10)
    result = new_counter.report() 
    assert result == "Counted to 28 so far.", 'returns "Counted to 28 so far." if if add further 10 and rereport'
