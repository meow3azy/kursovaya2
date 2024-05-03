def mask_card_number(card_number):
    if card_number:
        return f"{card_number[:4]} XX** **** {card_number[-4:]}"
    else:
        return ''


def mask_account_number(account_number):
    if account_number:
        return f"**{account_number[-4:]}"
    else:
        return ''
