# Task:
# 1.Ask how many employees
# 2.For each employee:
#     Ask name
#     Ask monthly salary
#     Store in a dictionary
# 3.Store all employees in a list
# 4.Loop through the list and print:
#     Name
#     Annual salary
#     Salary category (reuse your function!)

def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12

def salary_category(annual_salary):
    if annual_salary >= 1200000:
        return 'High income'
    elif annual_salary >= 60000:
        return 'Good salary'
    else:
        return 'Need to improve your skill'

employees = []

count = int(input("Enter number of employees:"))

for x in range(count):
    name = input("Enter the name of employee:")
    monthly_salary = int (input("Enter the monthly salary of employee {x+1}:"))

    emp = {"name":name, "monthly_salary":monthly_salary}

    employees.append(emp)


# employee detail

for emp_detail in employees:
    annual_salary = calculate_annual_salary(emp_detail["monthly_salary"])
    category = salary_category(annual_salary)

    print(f"Name of employee:{emp_detail['name']}")
    print(f"Annual salary of employee:{annual_salary}")
    print(f"The employee category:{category}")

    print("-"*40)

