def mask_card_number(card_number):
    card_parts = card_number.split()
    card_name = ' '.join(card_parts[:-1])
    card_digits = card_parts[-1]

    masked_digits = f"{card_digits[:4]} XX** **** {card_digits[-4:]}"
    return f"{card_name} {masked_digits}"
def mask_card_number(card_number):
    if len(card_number) > 16:
        visible_part = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        visible_part = f"{card_number[:4]} XX** **** {card_number[-4:]}"
    return visible_part

def mask_account_number(account_number):
    return f"**{account_number[-4:]}"
