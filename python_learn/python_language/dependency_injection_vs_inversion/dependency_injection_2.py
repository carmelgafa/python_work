import random
import string
from abc import ABC, abstractmethod

class Order:

    def __init__(self):
        self.id = ''.join(random.choices(string.ascii_lowercase, k=6))
        self.status = 'open'
    
    def set_status(self, status):
        self.status = status

class Authorizer(ABC):
    
    @abstractmethod
    def authorize(self):
        '''pass'''
    
    @abstractmethod
    def is_authorized(self) -> bool:
        pass

class Authorizer_SMS(Authorizer):
    
    def __init__(self):
        self.authorized = False
        self.code = None
    
    def generate_sms_code(self):
        self.code = ''.join(random.choices(string.digits, k=6))

    def authorize(self):
        code = input('Enter SMS code: ')
        self.authorized = code == self.code
        
    def is_authorized(self) -> bool:
        return self.authorized
    
class PaymentProcessor:
    
    def __init__(self, auth:Authorizer):
        self.authorizer = auth
        
    def pay(self, order):
        self.authorizer.authorize()
        if not self.authorizer.is_authorized():
            raise Exception('Not Authorized')
        print(f'Processing payment for order with id: {order.id}')
        order.set_status('paid')
        