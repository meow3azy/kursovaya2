import pytest
from src.transactions import print_last_transactions

def test_print_last_transactions(capsys):
    print_last_transactions()
    captured = capsys.readouterr()
    assert "Перевод организации" in captured.out
