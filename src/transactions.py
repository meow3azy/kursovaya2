import os
import json
from datetime import datetime
from masked import mask_card_number, mask_account_number


def print_transaction(operation):
    date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    description = operation['description']
    from_account = operation.get('from', 'Нет данных') or 'Нет данных'
    to_account = operation['to']
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    if 'from' in operation:
        from_account = mask_card_number(from_account) if from_account.startswith('Maestro') or from_account.startswith(
            'Visa') else mask_account_number(from_account)

    to_account = mask_account_number(to_account)

    print(f"{date} {description}")
    print(f"{from_account} -> Счет {to_account}")
    print(f"{amount} {currency}\n")


def print_last_transactions():
    file_path = "C:\\Users\\killr\\PycharmProjects\\kursach_2\\data\\operations.json"
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        operations = json.load(file)
    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    sorted_operations = sorted(executed_operations, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'),
                               reverse=True)
    last_5_operations = sorted_operations[:5]

    print("Сверху списка находятся самые последние операции (по дате):")
    for operation in last_5_operations:
        print_transaction(operation)
