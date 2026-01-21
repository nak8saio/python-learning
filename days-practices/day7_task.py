# write employee data into csv file.
# Task:
# Save employee data in CSV format
# Each line:
#         name,monthly_salary,annual_salary,category
import csv
import os
csvfile_path = 'employees.csv'

def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12

def salary_category(annual_salary):
    if annual_salary >= 1200000:
        return 'High income'
    elif annual_salary >= 60000:
        return 'Good salary'
    else:
        return 'Need to improve skill'

employees = []

def process_management(count):
    for i in range(count):
        name = input("Enter the name of employee:")
        monthly_salary = int(input("Enter the employee monthly salary:"))

    # define the dictinoary
        emp = {'name': name, 'monthly_salary': monthly_salary}
    # add dictionary into list
        employees.append(emp)

emp_count = int(input("Enter number of empolyees:"))
process_management(emp_count)

# check file csv

if os.path.exists(csvfile_path):
    print(f"employees.csv file exist.")
else:
    print(f"employees.csv file does not exist")

# write data as csv
with open("employees.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Add Header
    writer.writerow(['Name','Monthly Salary','Annual Salary','Category'])
    for emp in employees:
        annual_salary = calculate_annual_salary(emp['monthly_salary'])
        category = salary_category(annual_salary)

        # write file in csv file
        writer.writerow([emp['name'],emp['monthly_salary'],annual_salary,category])
                                
print(f"Employees data save into employees.csv file.")       