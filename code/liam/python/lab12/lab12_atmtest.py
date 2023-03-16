from lab08_v2 import ATM
import pytest

#Test functions for ATM lab

def test_check_balance():
    atm = ATM()
    assert atm.check_balance() == 0.0
    atm = ATM(300.0)
    assert atm.check_balance() == 300.0

def test_deposit():
    amount = 30.35
    atm = ATM(0.0)
    assert atm.deposit(amount) == 30.35
    atm = ATM(30.35)
    assert atm.deposit(amount) == 60.7
    assert atm.deposit(amount) == 91.05

def test_check_withdrawal():
    amount = 20.50
    atm = ATM(0)
    assert atm.check_withdrawal(amount) == False
    atm = ATM(20.50)
    assert atm.check_withdrawal(amount) == True
    atm = ATM(2000.50)
    assert atm.check_withdrawal(amount) == True

def test_withdraw():
    amount = 50
    atm = ATM(500)
    assert atm.withdraw(amount) == 450.0
    amount = 12.85
    assert atm.withdraw(amount) == 437.15
    amount = 437.15
    assert atm.withdraw(amount) == 0.0

def test_calc_interest():
    atm = ATM(210.0)
    assert atm.calc_interest() == 21.0
    atm = ATM(231.10)
    assert atm.calc_interest() == 23.11
    atm = ATM(45.21)
    assert atm.calc_interest() == 4.52

def test_print_transactions():
    atm = ATM()
    assert type(atm.print_transactions()) == str

def test_errors():
    atm = ATM()
    with pytest.raises(TypeError):
        atm.withdraw('banana')
    with pytest.raises(TypeError):
        atm.withdraw([1])
    with pytest.raises(TypeError):
        atm.deposit((5, 1))
    with pytest.raises(TypeError):
        atm.check_withdrawal({'money': 40})