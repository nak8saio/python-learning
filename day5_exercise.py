# exercise
# Task:
# Create a function salary_category(annual_salary)
# Return:
    # "High income" if ≥ 12,00,000
    # "Good salary" if ≥ 6,00,000
    # "Needs improvement" otherwise
# Call it inside your loop

def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12

def salary_category(annual_salary):
    if annual_salary >= 1200000 :
        return "High income"
    elif annual_salary >= 600000 :
        return "Good salary"
    else:
        return "Need improvement"    
            
def process_employees(count):
    for i in range(count):
        monthly_salary = int (input("Enter employee monthly salary:"))
        annual_salary = calculate_annual_salary(monthly_salary)
        category = salary_category(annual_salary)

        print(f"Employee {i + 1}- Annual Salary: ₹{annual_salary:,}")
        print(f"Category: {category}")
        print("-" * 30)

count = int (input("Enter number of employees:"))
process_employees(count)