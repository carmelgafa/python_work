'''
favour composition over inheritance
separate concepts
'''


from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional


class Commission(ABC):
    '''a generic commision class'''
    
    @abstractmethod
    def get_payment(self)->float:
        '''computes commission'''



@dataclass
class ContractCommission(Commission):
    '''commission'''
    commission: float = 100
    contracts_landed: float = 0

    def get_payment(self)-> float:
        '''computes commission'''
        return(
            self.commission * self.contracts_landed
        )


@dataclass
class Contract(ABC):
    '''contract'''
    
    @abstractmethod
    def get_payment(self)-> float:
        ''' calculates contract payment'''



@dataclass
class Employee:
    name: str
    id: int
    contract: Contract
    commission: Optional[Commission] = None
    
    def compute_pay(self)-> float:
        '''compute payment for employee'''
        payout = self.contract.get_payment()
        if self.commission is not None:
            payout += self.commission.get_payment()

        return payout


@dataclass
class HourlyContract(Contract):
    '''contract based on hours'''
    pay_rate: float = 0
    employer_cost : float = 1000
    hours_worked:int  = 0
    
    def get_payment(self)-> float:
        return(
            self.pay_rate * self.hours_worked
            + self.employer_cost
        )
    
@dataclass
class SalariedContract(Contract):
    '''contract based on monthly salary'''
    monthly_salary: float = 0
    percentage : float = 1

    def get_payment(self)-> float:
        return(
            self.monthly_salary * self.percentage
        )


@dataclass
class FreelancerContract(Contract):
    '''freelancer contract'''
    pay_rate: float = 0
    hours_worked:int  = 0
    vat_rate: str = ""


    def compute_pay(self)-> float:
        return(
            self.pay_rate * self.hours_worked
        )
        
def main()->None:
    
    
    henry_contract = HourlyContract(
        pay_rate=50,
        hours_worked=100
    )
    
    henry = Employee(
        "Henry",
        id=123456,
        contract = henry_contract
    )
    print(f'henry worked for {henry.contract.hours_worked} and earned {henry.compute_pay()}')
    
    
    sarah_contract = SalariedContract(
        monthly_salary=5000,
    )
    sarah_commission = ContractCommission(
        contracts_landed=10
        
    )    
    sarah = Employee(
        name='sarah',
        id=789456,
        contract=sarah_contract,
        commission=sarah_commission
    )
    print(f'sarah landed {sarah.commission.contracts_landed} and earned {sarah.compute_pay()}')

if __name__=='__main__':
    main()