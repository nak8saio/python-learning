# combine list+dict+loop+fucntion

employees = []

def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12

def salary_category(annual_salary):
    if annual_salary >= 1200000:
        return 'High income'
    elif annual_salary >= 60000:
        return 'Good salary'
    else:
        return 'Need to improve your skill.'
    
count = int(input("Enter number of employees:"))    
for i in range(count):
    name = input("Enter the name of employee:")
    monthly_salary = int(input("Eneter employee monthly salary:"))

    employee = {'name': name,'monthly_salary': monthly_salary}
    employees.append(employee)
    

for emp in employees:
    annual_salary = calculate_annual_salary(emp['monthly_salary'])
    category = salary_category(annual_salary)

    print(f"Name of the employee: {emp['name']}")
    print(f"The annual salary of employee:{annual_salary}")
    print(f"The employee category:{category}")

    print("-"*40)  
    