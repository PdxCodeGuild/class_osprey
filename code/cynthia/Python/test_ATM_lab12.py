#Automated Tests
#using Pick 6 and ATM

from lab08_2 import ATM
import pytest

def test_ATM_creation():
    atm = ATM(0)
    assert atm.balance == 0
    atm = ATM(-5)
    assert atm.balance == -5
    atm = ATM(.1)
    assert atm.interest_rate == .1

def test_check_balance():
    atm = ATM(0)
    assert atm.check_balance() == 0

def test_deposit():
    atm = 