# Write your test here
from challenge02  import *
import pytest

def test_repeated_word_1():
    hashtabel1= HashTabel()
    actual=hashtabel1.find_repeated('ASAC is a department at LTUC. ASAC teaches programming in LTUC.')
    expected = 'ASAC'
    assert actual == expected

def test_repeated_word_2():
    hashtabel1= HashTabel()
    actual=hashtabel1.find_repeated('I am learning programming at ASAC.')
    expected = 'No Repetition'
    assert actual == expected
