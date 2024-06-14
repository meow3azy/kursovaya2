def mask_card_number(card_number):
    card_name, card_number = card_number.rsplit(' ', 1)
    masked_number = f"{card_number[:4]} {card_number[4:6]}XX **** {card_number[-4:]}"
    return f"{card_name} {masked_number}"

def mask_account_number(account_number):
    return f"**{account_number[-4:]}"
