import unittest
from transactions import print_last_transactions
from masked import mask_card_number, mask_account_number

class TestTransactions(unittest.TestCase):
    def test_mask_card_number(self):
        card_number = "1234567890123456"
        masked_card_number = mask_card_number(card_number)
        self.assertEqual(masked_card_number, "1234 XX** **** 3456")

    def test_mask_account_number(self):
        account_number = "12345678"
        masked_account_number = mask_account_number(account_number)
        self.assertEqual(masked_account_number, "**5678")


if __name__ == '__main__':
    unittest.main()
