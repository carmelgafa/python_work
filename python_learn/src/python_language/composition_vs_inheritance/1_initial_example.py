from dataclasses import dataclass

@dataclass
class HourlyEmployee:
    '''employee paid based in hours'''
    name: str
    id: int
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
class SalariedEmployee:
    '''employee paid based on monthly salary'''
    name: str
    id: int
    commission: float = 100
    contracts_landed: float = 0
    monthly_salary: float = 0
    percentage : float = 1

    def compute_pay(self)-> float:
        return(
            self.monthly_salary * self.percentage
            + self.commission * self.contracts_landed
        )

@dataclass
class Freelancer:
    '''freelancer employee'''
    name: str
    id: int
    commission: float = 100
    contracts_landed: float = 0
    pay_rate: float = 0
    hours_worked:int  = 0
    vat_rate: str = ""    


    def compute_pay(self)-> float:
        return(
            self.pay_rate * self.hours_worked
            + self.commission * self.contracts_landed
        )
        
def main()->None:
    
    henry = HourlyEmployee(
        "Henry",
        id=123456,
        pay_rate=50,
        hours_worked=100)
    print(f'henry worked for {henry.hours_worked} and earned {henry.compute_pay()}')
    
    sarah = SalariedEmployee(
        name='sarah',
        id=789456,
        monthly_salary=5000,
        contracts_landed=10
    )
    print(f'sarah landed {sarah.contracts_landed} and earned {sarah.compute_pay()}')


if __name__=='__main__':
    main()