def mask_card_number(card_number):
    if card_number:
        return f"{card_number[:17]} {'X' * 4}"
    else:
        return None

def mask_account_number(account_number):
    if account_number:
        return account_number[-4:]
    else:
        return None
