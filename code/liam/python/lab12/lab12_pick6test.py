from lab03_v2 import pick6, num_matches, match_to_win
import pytest

#Test functions for Pick 6 lab
def test_pick6():
    assert type(pick6()) == list
    assert len(pick6()) == 6
    for i in pick6():
        assert i >= 1 and i <= 99

def test_num_matches():
    assert num_matches([43, 31, 2, 99, 10, 11], [43, 31, 2, 99, 10, 11]) == 6
    assert num_matches([43, 31, 2, 99, 4, 11], [43, 31, 2, 99, 10, 11]) == 5
    assert num_matches([11, 31, 2, 99, 10, 43], [43, 31, 2, 99, 10, 11]) == 4
    assert num_matches([43, 31, 2, 99, 4, 11], [2, 99, 4, 11, 43, 31]) == 0

def test_match_to_win():
    assert match_to_win(6) == 25000000
    assert match_to_win(2) == 7

def test_errors():
    with pytest.raises(KeyError):
        match_to_win('a')
    with pytest.raises(KeyError):
        match_to_win(1.4)
