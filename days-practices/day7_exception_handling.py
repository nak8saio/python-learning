
import csv
import os

CSV_FILE = 'employees.csv'

def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12

def salary_category(annual_salary):
    if annual_salary >= 1200000:
        return 'High income'
    elif annual_salary >= 600000:
        return 'Good salary'
    else:
        return 'Need to inmprove skill'

def process_management(count):
    for i in range(count):

        while True:
            try:
                name = input("Enter employee name:")
                monthly_salary = int(input("Enter employee salary:"))
                if monthly_salary < 0:
                    raise ValueError("Salary can't be negative.")
                
                annual_salary = calculate_annual_salary(monthly_salary)
                print(f"Annual salary:{annual_salary}")

                category = salary_category(annual_salary)
                print(f"Category of employees :{category}")

                break
            except ValueError:
                print(f"Invalid input. Please enter positive number only.")

            

def get_employee_count():
    while True:
        try:
            emp_count = int(input("Enter number of employee:"))
            if emp_count < 0:
                raise ValueError
            return emp_count
        except ValueError:
            print("Invalid input")
            

# check file csv

if os.path.exists(CSV_FILE):
    print(f"employees.csv file exist.")
else:
    print(f"employees.csv file does not exist")

try:
    with open(CSV_FILE, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Please save employee data first.")

employee_count = get_employee_count()
process_management(employee_count)   


        