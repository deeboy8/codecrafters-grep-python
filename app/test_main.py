import pytest

from main import match_pattern 

def test_digit():
    pattern = '\\d'
    input_line_pass = '123'
    input_line_fail = 'abc'

    test_pass = match_pattern(input_line_pass, pattern)
    test_fail = match_pattern(input_line_fail, pattern)
    
    assert(test_pass)
    assert(test_fail)

def test_negative_character_classes():
    pattern = "[^abc]"
    input_line = 'def'

    test_pass = match_pattern(input_line, pattern)

    assert(test_pass)

def test_negative_character_class():
    pattern = "[^abc]"
    input_line = 'abc'

    test_pass = match_pattern(input_line, pattern)

    assert(not test_pass)