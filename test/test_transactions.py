import os
import pytest
from transactions import print_last_transactions, mask_card_number, load_operations

@pytest.fixture
def json_file():
    current_dir = os.path.dirname(__file__)
    json_file = os.path.join(current_dir, '..', 'data', 'operations.json')
    return json_file

def test_mask_card_number():
    assert mask_card_number("Visa Platinum 7000 7900 1234 6361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_card_number("Maestro 7810846596785568") == "Maestro 7810 84** **** 5568"

def test_load_operations(json_file):
    operations = load_operations(json_file)
    assert isinstance(operations, list)
    assert len(operations) > 0

def test_print_last_transactions(json_file, capsys):
    print_last_transactions(json_file)
    captured = capsys.readouterr()

    assert "08.12.2019 Открытие вклада" in captured.out
    assert "Нет данных -> Счет **5907" in captured.out
    assert "41096.24 USD" in captured.out

    assert "07.12.2019 Перевод организации" in captured.out
    assert "Visa Classic 2842 78** **** 9012 -> Счет **3655" in captured.out
    assert "48150.39 USD" in captured.out

    assert "19.11.2019 Перевод организации" in captured.out
    assert "MasterCard 143544 16** **** 8409 -> Счет **2869" in captured.out
    assert "30153.72 руб." in captured.out

    assert "13.11.2019 Перевод со счета на счет" in captured.out
    assert "Счет 386114395228 56** **** 9794 -> Счет **8125" in captured.out
    assert "62814.53 руб." in captured.out

    assert "05.11.2019 Открытие вклада" in captured.out
    assert "Нет данных -> Счет **8381" in captured.out
    assert "21344.35 руб." in captured.out
