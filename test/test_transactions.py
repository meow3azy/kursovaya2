import os
import json
import pytest


@pytest.fixture
def transactions_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file = os.path.join(current_dir, '../data/operation.json')

    if not os.path.exists(json_file):
        pytest.skip(f"File '{json_file}' not found. Skipping test.")

    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def test_print_last_transactions(transactions_data):
    operations = transactions_data.get('operations', [])

    assert len(operations) > 0


def test_operations_count(transactions_data):
    operations = transactions_data.get('operations', [])

    assert len(operations) == 3


def test_operations_dates(transactions_data):
    operations = transactions_data.get('operations', [])

    for operation in operations:
        assert 'date' in operation
        assert operation['date'][:4] == '2019'


def test_operations_currency(transactions_data):
    operations = transactions_data.get('operations', [])

    for operation in operations:
        amount = operation.get('operationAmount', {}).get('currency', {}).get('code', '')
        assert amount in ['USD', 'RUB']


def test_operations_descriptions(transactions_data):
    operations = transactions_data.get('operations', [])

    for operation in operations:
        description = operation.get('description', '')
        assert len(description) > 0


if __name__ == '__main__':
    pytest.main()
