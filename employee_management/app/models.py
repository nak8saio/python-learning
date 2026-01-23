# Base class

class Employee:
    def __init__(self,name,monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary *12    
    
    def category(self):
        annual = self.annual_salary()

        if annual >= 12_00_000:
            return 'High income'
        elif annual >= 600_000:
            return 'Good salary'
        else:
            return 'Need improvement'