from random import randint
from unittest.mock import patch

TICKET_COST = 2
PAYOUTS = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50_000,
    5: 1_000_000,
    6: 25_000_000
}
ITERATIONS = 100_000


def make_ticket() -> list:
    '''returns a ticket with 6 numbers between 1 and 99'''
    return [randint(1, 99) for _ in range(6)]


def count_matches(player_ticket: list, winning_ticket: list) -> int:
    '''returns number of indices with matching values for two tickets'''
    matches = 0
    for i in range(len(player_ticket)):
        if player_ticket[i] == winning_ticket[i]:
            matches += 1
    return matches


def play():
    '''returns the earnings and expenses for a batch of lottery tickets'''
    winner = make_ticket()
    earnings = 0
    for _ in range(ITERATIONS):
        matches = count_matches(winner, make_ticket())
        earnings += PAYOUTS[matches]
    expenses = TICKET_COST * ITERATIONS
    return earnings, expenses


if __name__ == '__main__':
    earnings, expenses = play()
    print(f'''
you spent: ${expenses}
you won: ${earnings}
your balance: ${earnings - expenses}
your ROI: {(earnings - expenses)/expenses}
''')


@patch('pick6.count_matches', return_value=3)
def test_play(mocked_count):
    outcome = play()
    assert type(outcome) == tuple
    assert len(outcome) == 2
    assert type(outcome[0]) == int
    assert type(outcome[1]) == int
    assert outcome[1] == ITERATIONS * TICKET_COST
    assert outcome[0] == PAYOUTS[mocked_count.return_value] * ITERATIONS
