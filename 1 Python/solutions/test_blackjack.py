from blackjack import handle_card, advise
from unittest.mock import patch
import pytest


def test_advise_blackjack():
    assert advise([21]) == ('BLACKJACK!', 21)
    assert advise([2, 10, 21]) == ('BLACKJACK!', 21)
    assert advise([21, 30]) == ('BLACKJACK!', 21)


def test_advise_bust():
    assert advise([30]) == ('BUSTED', 30)
    assert advise([22, 23]) == ('BUSTED', 22)


def test_advise_stay():
    assert advise([20]) == ('stay', 20)
    assert advise([17]) == ('stay', 17)
    assert advise([4, 18, 30]) == ('stay', 18)


def test_advise_hit():
    assert advise([16]) == ('hit', 16)
    assert advise([12]) == ('hit', 12)
    assert advise([4, 13, 30]) == ('hit', 13)


def test_advise_errors():
    with pytest.raises(TypeError):
        advise('hello :)')

    with pytest.raises(TypeError):
        print(advise(1))


@patch('builtins.input')
def test_handle_card(mock_input):
    mock_input.return_value = 'k'
    assert handle_card('test', [0]) == [10]
    assert handle_card('test', [5]) == [15]
    assert handle_card('test', [5, 15]) == [15, 25]
    assert handle_card('test', [1, 11]) == [11, 21]

    mock_input.return_value = '3'
    assert handle_card('test', [0]) == [3]
    assert handle_card('test', [5]) == [8]
    assert handle_card('test', [5, 15]) == [8, 18]
    assert handle_card('test', [1, 11]) == [4, 14]

    mock_input.return_value = 'a'
    assert handle_card('test', [0]) == [1, 11]
    assert handle_card('test', [10]) == [11, 21]
    assert handle_card('test', [2, 14]) == [3, 15, 13, 25]

    with pytest.raises(RecursionError):
        mock_input.return_value = ':)'
        handle_card('test', [0])

    with pytest.raises(TypeError):
        mock_input.return_value = 'k'
        handle_card('test', ':)')

    with pytest.raises(TypeError):
        mock_input.return_value = 'k'
        handle_card('test', 1)
