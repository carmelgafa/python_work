import unittest
from unittest.mock import patch

from dependency_injection import Authorizer_SMS, Order, PaymentProcessor

class Order_TestCase(unittest.TestCase):
    
    def test_init(self):
        order = Order()
        self.assertEqual(order.status, 'open')
        
    def test_set_status(self):
        order = Order()
        order.set_status("paid")
        self.assertEqual(order.status, "paid")
        
class Authorizer_SMS_TestCase(unittest.TestCase):
    
    def test_init_authorized(self):
        auth = Authorizer_SMS()
        self.assertFalse(auth.is_authorized())
        
    def test_code_decima(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        self.assertTrue(auth.code.isdecimal())
    
    def test_authorize_success(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        with patch('builtins.input', return_value=auth.code):
            auth.authorize()
            self.assertTrue(auth.is_authorized)

    @patch('builtins.input', return_value="1234567")
    def test_authorize_fail(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        auth.authorize()
        self.assertFalse(auth.is_authorized())

class PaymentProcessor_TestCase(unittest.TestCase):
    
    def test_payment_success(self):
        self.assertTrue(True)
        
    def test_payment_fail(self):
        self.assertTrue(True)
        

if __name__=="__main__":
    unittest.main()