# How to create a funtion to avoid task repetation

# calculate salary
def calculate_annulal_salary(monthly_salary):
    return monthly_salary *12

# employee process 

def process_employees(count):
    for i in range(count):
        monthly_salary = int (input("Enter monthly salary:"))
        annual_salary = calculate_annulal_salary(monthly_salary)
        print(f"{i+1}- annual salary of employee is :{annual_salary}")

count = int (input("Enter number of employees:"))
process_employees(count)