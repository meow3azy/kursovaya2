import os
from masked import mask_card_number, mask_account_number
import json
from datetime import datetime


def print_last_transactions():
    """
    Выводит на экран последние 5 выполненных операций.

    Операции разделяются пустой строкой.
    Дата перевода представлена в формате ДД.ММ.ГГГГ.
    Номер карты замаскирован и не отображается целиком.
    Номер счета замаскирован и не отображается целиком.
    """
    # Определение пути к файлу operations.json
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Получаем текущую директорию
    file_path = os.path.join(current_directory, '..', 'data', 'operations.json')  # Объединяем путь к файлу

    # Открытие файла с данными операций
    with open(file_path, 'r', encoding='utf-8') as file:
        operations = json.load(file)

    # Фильтрация и сортировка выполненных операций по дате (от новых к старым)
    executed_operations = sorted(
        (op for op in operations if op.get('state') == 'EXECUTED'),
        key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'),
        reverse=True
    )

    # Получение последних 5 выполненных операций (самые новые)
    last_executed_operations = executed_operations[:5]

    # Вывод информации о количестве операций
    print("Сверху списка находятся самые последние операции (по дате):")

    for operation in last_executed_operations:
        print_transaction(operation)


def print_transaction(operation):
    date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    description = operation['description']
    from_account = operation.get('from', '')
    to_account = operation['to']
    operation_amount = operation['operationAmount']
    amount = operation_amount['amount']
    currency = operation_amount['currency']['name']

    # Маскируем номер карты
    masked_from_account = mask_card_number(from_account) if from_account else "Нет данных"

    # Маскируем номер счета
    masked_to_account = mask_account_number(to_account) if to_account else "Нет данных"

    if masked_from_account:
        masked_from_account = ' '.join([masked_from_account[:17], 'XX**', '****'])

    if masked_to_account:
        masked_to_account = 'Счет **' + masked_to_account[-4:]

    # Выводим операцию
    print(f"{date} {description}")
    print(f"{masked_from_account} -> {masked_to_account}")
    print(f"{amount} {currency}")
    print()
