import json
from datetime import datetime
from src.masked import mask_card_number, mask_account_number

def load_operations(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            operations = json.load(f)
        return operations
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

def print_transaction(operation):
    date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    description = operation.get('description', 'Нет описания')
    from_account = mask_card_number(operation.get('from', 'Нет данных'))
    to_account = mask_account_number(operation.get('to', 'Нет данных'))
    amount = operation.get('operationAmount', {}).get('amount', 'Нет данных')
    currency = operation.get('operationAmount', {}).get('currency', {}).get('name', 'Нет данных')

    print(f"{date} {description}")
    print(f"{from_account} -> Счет {to_account}")
    print(f"{amount} {currency}\n")

def print_last_transactions(file_path):
    operations = load_operations(file_path)
    if not operations:
        return

    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    sorted_operations = sorted(executed_operations, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    last_5_operations = sorted_operations[:5]

    for operation in last_5_operations:
        print_transaction(operation)
