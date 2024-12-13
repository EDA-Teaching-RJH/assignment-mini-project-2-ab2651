import pytest
from BankAccount import BankAccount

def account():
    return BankAccount("John", 200)

def test_invalid_deposit():
    with pytest.raises(ValueError):
        account.deposit(-300)
    
