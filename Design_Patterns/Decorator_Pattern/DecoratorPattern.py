import abc
from functools import wraps

def Logging(func):
    @wraps(wrapped=func)
    def wrapper(*args, **kwargs):
        print(wrapper.__name__,"Called with",kwargs)
        print(wrapper.__code__.co_freevars)
        print (wrapper.__code__.co_varnames)
        # print(kwargs)
        return func(*args, **kwargs)
    return wrapper

class EmployeeInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr (subclass, 'Employee_Salary') and
                callable (subclass.Employee_Salary) and
                hasattr (subclass, 'Employee_Benefits') and
                callable (subclass.Employee_Benefits) or
                NotImplemented)

    @abc.abstractmethod
    def Employee_Salary(self, base: float , bonus_percent: float):
        """Define Employee Salary"""
        raise NotImplementedError

    @abc.abstractmethod
    def Employee_Benefits(self, retirement_plan: str):
        """Define Employee Benefits"""
        raise NotImplementedError

class FullTimeEmployee(EmployeeInterface):

    def Employee_Salary(self, base: float , bonus_percent: int):
        self.base = base
        self.bonus_percent = bonus_percent
        self.annual_total = base + (bonus_percent/100)
        return self.annual_total


    def Employee_Benefits(self, retirement_plan: str):
        self.retirement_plan = retirement_plan if retirement_plan.__contains__("401k") else "None"
        return self.retirement_plan

class ContractEmployee(EmployeeInterface):

    @Logging
    def Employee_Salary(self, base: float , bonus_percent: int):
        self.base = base
        self.bonus_percent = float((bonus_percent * self.base/100))
        annual_total = base + self.bonus_percent
        self.annual_total = annual_total
        # print(annual_total)
        return self.annual_total

    def Employee_Benefits(self, retirement_plan: str):
        self.retirement_plan = retirement_plan if retirement_plan.__contains__("401k") else "None"
        return self.retirement_plan



print(callable(ContractEmployee.Employee_Salary))

CT1 = ContractEmployee()
print(id(ContractEmployee), id(CT1))
print(vars(CT1))

print(CT1.Employee_Salary(base=80000.00,bonus_percent=20))
print(vars(CT1))

print(CT1.annual_total)
print(issubclass(ContractEmployee,EmployeeInterface))