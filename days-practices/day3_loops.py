# Task 1:

# Ask how many employees
count = int (input ("Enter number of employees:"))

# Loop and take salary input
for i in range(count):
    salary = int (input("Enter salary:"))
    annual_salary = salary * 12
    # Print annual salary for each
    print(f"{i+1}-employee annual salary is:{annual_salary}")

    