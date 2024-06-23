import os
import pytest
from transactions import print_last_transactions, mask_card_number, load_operations


@pytest.fixture
def json_file():
    current_dir = os.path.dirname(__file__)
    json_file = os.path.join(current_dir, '..', 'data', 'operations.json')
    return json_file


def test_print_last_transactions(json_file, capsys):
    print_last_transactions(json_file)
    captured = capsys.readouterr().out

    assert "08.12.2019 Открытие вклада" in captured
    assert "Нет данных -> Счет **5907" in captured or "Нет данных -> Счет Счет **5907" in captured

    assert "07.12.2019 Перевод организации" in captured
    assert "Visa Classic 2842" in captured
    assert "**3655" in captured

    assert "19.11.2019 Перевод организации" in captured
    assert "MasterCard 1435" in captured
    assert "**2869" in captured

    assert "13.11.2019 Перевод со счета на счет" in captured
    assert "Счет 3861" in captured
    assert "**8125" in captured

    assert "05.11.2019 Открытие вклада" in captured
    assert "Нет данных -> Счет **8381" in captured
    assert "21344.35 руб." in captured