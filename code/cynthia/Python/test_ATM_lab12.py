#Automated Tests
#using using ATM 

from lab08_2 import ATM
import pytest

def test_ATM_creation():
    atm = ATM(0)
    assert atm.balance == 0
    atm = ATM(-5)
    assert atm.balance == -5
    assert atm.interest_rate == .1

def test_check_balance():
    atm = ATM(0)
    assert atm.check_balance() == 0
    atm = ATM(10)
    assert atm.check_balance() == 10
    

def test_deposit():
    atm = ATM(50)
    assert atm.deposit(10) == 60
    assert atm.deposit(30)  == 90

def test_check_withdrawal():
    atm = ATM(10)
    assert atm.check_withdrawal(5) == True
    atm = ATM(5)
    assert atm.check_withdrawal(0) == True
   

def test_withdraw():
    atm = ATM(50)
    assert atm.withdraw(10) == 40
    assert atm.withdraw(5) == 35

def test_calc_interest():
    atm = ATM(50)
    assert atm.calc_interest() == 5
    atm = ATM(10000)
    assert atm.calc_interest() == 1000
