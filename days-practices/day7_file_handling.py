# Save employee data using file handlling

employees = []

def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12


def salary_category(annaul_salary):
    if annaul_salary >=1200000:
        return 'High income'
    elif annaul_salary >= 60000:
        return 'Good salary'
    else:
        return 'Need to improve your skill.'
    

def proccess_management(count):
    for emp_count in range(count):
        name = input("Enter the name of employee:")
        monthly_salary = int(input("Enter the monthly salary of employee: "))

        emp_dict = {'name': name, 'monthly_salary': monthly_salary}
        employees.append(emp_dict)
        

count = int(input("Enter the number of employees:"))
proccess_management(count)

with open("employee.txt", "w") as file:
    for emp in employees:
        annual_salary = calculate_annual_salary(emp['monthly_salary'])
        category = salary_category(annual_salary)

        # write employees details into employee text file.
        file.write(f"Name of employee:{emp['name']}\n")
        file.write(f"Salary of employee:{annual_salary}\n")
        file.write(f"Category of employee:{category}\n")
        file.write("-" * 30 + "\n")

print(f"Employee data saved to employee.txt")        

