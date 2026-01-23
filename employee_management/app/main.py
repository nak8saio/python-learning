from database import create_table
from curd import insert_employee,fetch_employees
from models import Employee

create_table()

count = int(input("Enter number of employees:"))
for i in range(count):
    name = input("Enter employee name:")
    salary = int(input("Enter employee monthly salary:"))
    if salary < 0:
        print(f"salary must be positive")
        continue

    emp = Employee(name,salary)
    insert_employee(emp)

print("\nStored Employees")
print("-" * 40)

for emp in fetch_employees():
    print(emp)
