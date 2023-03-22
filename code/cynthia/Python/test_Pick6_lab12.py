#Lab 12 
#test for Pick6 

from lab03_2 import pick6, num_matches 
import pytest
from unittest.mock import patch



def test_num_matches():
    assert num_matches([1,2,3,4,5,6], [1,2,3,4,5,6]) == 6
    assert num_matches([9,8,7,9,8,7], [1,2,3,4,5,6]) == 0
    assert num_matches([1,2,3,9,8,7], [1,2,3,4,5,6]) == 3

@patch('lab03_2.num_matches', return_value = 2)
def test_pick6(mocked_matches):
    outcome = pick6()
    assert type(outcome) == int
    assert outcome == 500000