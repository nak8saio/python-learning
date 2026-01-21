# employee profile

emp_name = input("Enter employee name:")
print(f"\nHello, {emp_name}!")

monthly_salary = int (input("Enter your salary:"))
annual_salary = monthly_salary * 12 

if  annual_salary >= 1200000 :
    print(f"High income, {annual_salary}")
elif annual_salary >= 600000 :
    print(f"Good salary, {annual_salary}")
else:
    print("Your salary is need to more improvement")        