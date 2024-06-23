def mask_card_number(card_info):
    """
    Маскировка номера карты, отображающая полное название карты, первые 6 цифр, затем '** ****', затем последние 4 цифры.
    Обеспечивает правильное форматирование.
    """
    if not card_info or card_info == "Нет данных":
        return "Нет данных"

    parts = card_info.split()
    card_name = " ".join(parts[:-1])
    card_number = parts[-1]

    first_six = card_number[:6]
    last_four = card_number[-4:]

    masked_card_number = f"{card_name} {first_six[:4]} {first_six[4:6]}** **** {last_four}"

    return masked_card_number


def mask_account_number(account_info):
    """
    Маскировка номера счета, отображающая только последние 4 цифры с префиксом '**'.
    """
    if not account_info or account_info == "Нет данных":
        return "Нет данных"

    parts = account_info.split()
    account_name = " ".join(parts[:-1])
    account_number = parts[-1]

    last_four = account_number[-4:]

    masked_account_number = f"{account_name} **{last_four}"

    return masked_account_number
