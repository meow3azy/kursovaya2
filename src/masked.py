def mask_card_number(card_number):
    return f"{card_number[:17]} {card_number[18:20]}** **** {card_number[-4:]}"


def mask_account_number(account_number):
    return f"**{account_number[-4:]}"
