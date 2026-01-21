# # Create class

# class Employee:
#     def __init__(self,name,monthly_salary):
#         self.name = name
#         self.monthly_salary = monthly_salary

#     def calculate_annual_salary(self):
#         return self.monthly_salary *12

#     def salary_category(self):
#         annual_salary = self.calculate_annual_salary()
#         if annual_salary >= 1200000:
#             return 'High income'
#         elif annual_salary >= 600000:
#             return 'Good salary'
#         else:
#             return 'Need to improve skill'    

# employees = []

# count = int(input("Enter number of employee:"))
# for i in range(count):
#     name = input("Enter name of employee:")
#     salary = int(input("Enter monthly salary of employee:"))

#     if salary < 0:
#         print(f"Salary must be positive.")
#         continue

#     # emp = Employee(name,salary)
#     employees.append(Employee(name,salary)
# )

# for emp in employees:
#     print(f"Name of the employee:{emp.name}")
#     print(f"Annual salary of the employee:{emp.calculate_annual_salary()}")
#     print(f"Category of the employee:{emp.salary_category()}") 
#     print("-" * 30)   




class Employee:
    def __init__(self,name,monthly_salary):
        self.name = name
        self._monthly_salary = monthly_salary

    def annual_salary(self):
        return self._monthly_salary * 12
    
    def salary_category(self):
        salary = self.annual_salary()
        if salary >= 120000:
            return 'High income'
        elif salary >= 60000:
            return 'Good salary'
        else:
            return 'Need to improve skill'
        
class Manager(Employee):
    def __init__(self, name, monthly_salary,bonus):
        super().__init__(name, monthly_salary)
        self.bonus = bonus

    def annual_salary(self):
        return super().annual_salary() + self.bonus           
        
employees = []
count = int(input("Enter number of employee:"))
for i in range(count):
    role = input("Enter role (employee/manager): ").lower()
    name = input("Enter name of employee:")
    salary = int(input("Enter monthly salary of employee:"))
    if salary < 0:
        print(f"Salary must be positive only.")
        continue
    if role =='manager':
        bonus = int(input("Enter bouns amount:"))
        employees.append(Manager(name,salary,bonus))
    else:
        employees.append(Employee(name,salary))

print("\nEmployee Details")
print("-" * 30)

for emp in employees:
    print(f"Name of employee:{emp.name}")
    print(f"Annual salary of employee:{emp.annual_salary()}")
    print(f"Category of employees:{emp.salary_category()}")
    print("-" * 30)
