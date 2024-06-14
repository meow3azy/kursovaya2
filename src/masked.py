def mask_card_number(card_number):
    if len(card_number) > 10:
        visible_part = f"{card_number[:6]} XX** **** {card_number[-4:]}"
    else:
        visible_part = f"{card_number[:6]} XX** **** {card_number[-4:]}"
    return visible_part

def mask_account_number(account_number):
    return f"**{account_number[-4:]}"
