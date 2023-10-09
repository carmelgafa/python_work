'''
implements inheritance
notice explosion of subclasses for every type
'''


from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Employee(ABC):
    name: str
    id: int
    
    @abstractmethod
    def compute_pay(self)-> float:
        '''compute payment for employee'''


@dataclass
class HourlyEmployee(Employee):
    '''employee paid based in hours'''
    commission: float = 100
    contracts_landed: float = 0
    pay_rate: float = 0
    employer_cost : float = 1000
    hours_worked:int  = 0
    
    
    def compute_pay(self)-> float:
        return(
            self.pay_rate * self.hours_worked
            + self.employer_cost
            + self.commission * self.contracts_landed
        )
    
@dataclass
class SalariedEmployee(Employee):
    '''employee paid based on monthly salary'''

    monthly_salary: float = 0
    percentage : float = 1

    def compute_pay(self)-> float:
        return(
            self.monthly_salary * self.percentage
        )


@dataclass
class SalariedEmployeeWithCommission(SalariedEmployee):
    '''employee paid based on monthly salary with commission'''
    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self)-> float:
        return(
            super().compute_pay()
            + self.commission * self.contracts_landed
        )


@dataclass
class Freelancer(Employee):
    '''freelancer employee'''
    pay_rate: float = 0
    hours_worked:int  = 0
    vat_rate: str = ""    


    def compute_pay(self)-> float:
        return(
            self.pay_rate * self.hours_worked
        )



@dataclass
class FreelancerWithCommission(Freelancer):
    '''freelancer employee'''
    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self)-> float:
        return(
            super().compute_pay()
            + self.commission * self.contracts_landed
        )


        
def main()->None:
    
    henry = HourlyEmployee(
        "Henry",
        id=123456,
        pay_rate=50,
        hours_worked=100)
    print(f'henry worked for {henry.hours_worked} and earned {henry.compute_pay()}')
    
    sarah = SalariedEmployeeWithCommission(
        name='sarah',
        id=789456,
        monthly_salary=5000,
        contracts_landed=10
    )
    print(f'sarah landed {sarah.contracts_landed} and earned {sarah.compute_pay()}')

if __name__=='__main__':
    main()