import json
import os
from masked import mask_card_number, mask_account_number


def print_last_transactions():
    with open('../data/operations.json', 'r', encoding='utf-8') as file:
        operations = json.load(file)

    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    last_executed_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)[:5]

    for op in last_executed_operations:
        date = op['date']
        description = op['description']
        from_account = op.get('from', '')
        to_account = op.get('to', '')
        operation_amount = op.get('operationAmount', '')
        if isinstance(operation_amount, str):
            amount, currency = operation_amount.split(' ')
        else:
            amount = currency = ''
        masked_from_account = mask_card_number(from_account)
        masked_to_account = mask_account_number(to_account)

        print(f"{date} {description}")
        print(f"{masked_from_account} -> {masked_to_account}")
        print(f"{amount} {currency}")
        print()


print("Current directory:", os.getcwd())
