def mask_card_number(card_number):
    card_name = card_number.split(' ')[0]
    card_number = ''.join(filter(str.isdigit, card_number))[:6]
    visible_part = f"{card_name} {' '.join([card_number[:4], 'XX**', '****', card_number[-4:]])}"
    return visible_part




def mask_account_number(account_number):
    masked_number = '**' + account_number[-4:]
    return masked_number
