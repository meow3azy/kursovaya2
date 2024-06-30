import pytest
import os
from src.transactions import print_last_transactions, load_operations, print_transaction
from src.masked import mask_card_number
@pytest.fixture
def operations():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    ]

def test_mask_card_number():
    assert mask_card_number("Visa Classic 28428790129012") == "Visa Classic 2842 87** **** 9012"
    assert mask_card_number("MasterCard 1435441678908409") == "MasterCard 1435 44** **** 8409"
    assert mask_card_number("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"

def test_print_transaction(capsys, operations):
    print_transaction(operations[0])
    captured = capsys.readouterr()
    assert "26.08.2019 Перевод организации" in captured.out
    assert "Maestro 1596 83** **** 5199 -> Счет **9589" in captured.out
    assert "31957.58 руб." in captured.out

def test_print_last_transactions(capsys, operations, monkeypatch):
    def mock_load_operations(file_path):
        return operations

    monkeypatch.setattr('src.transactions.load_operations', mock_load_operations)

    current_dir = os.path.dirname(__file__)
    json_file = os.path.join(current_dir, '..', 'data', 'operations.json')
    print_last_transactions(json_file)
    captured = capsys.readouterr()
    assert "Сверху списка находятся самые последние операции (по дате):" in captured.out

    assert "26.08.2019 Перевод организации" in captured.out
    assert "Maestro 1596 83** **** 5199 -> Счет **9589" in captured.out
    assert "31957.58 руб." in captured.out

    assert "03.07.2019 Перевод организации" in captured.out
    assert "MasterCard 7158 30** **** 6758 -> Счет **5560" in captured.out
    assert "8221.37 USD" in captured.out

    assert "30.06.2018 Перевод организации" in captured.out
    assert "Счет 7510 68** **** 6952 -> Счет **6702" in captured.out
    assert "9824.07 USD" in captured.out

def test_load_operations():
    current_dir = os.path.dirname(__file__)
    json_file = os.path.join(current_dir, '..', 'data', 'operations.json')
    data = load_operations(json_file)
    assert data is not None
    assert type(data) == list
    assert load_operations("error_file") == []
