from salary_utils import calculate_annual_salary,salary_category
from file_utils import file_exists,read_file,write_csv_file

employees = []

def get_employee_count():
    while True:
        try:
            count = int(input("Enter the number of employee:"))
            if count < 0:
                raise ValueError
            return count
        except ValueError:
            print(f"Invalid input.Enter only positive number.")

def proccess_management(count):
    for i in range(count):
        while True:
            try:
                name = input("Enter name of employee:")
                monthly_salary = int(input("Enter employee monthly_salary:"))

                if monthly_salary < 0:
                    raise ValueError
                
                annual_salary = calculate_annual_salary(monthly_salary)
                category = salary_category(annual_salary)
                # emp = {'name': name, 'monthly_salary': monthly_salary,'category':category}
                employees.append([name,monthly_salary,annual_salary,category])
                print(f"Employee annual salary :{annual_salary}")
                print(f"Employee category:{category}")
                break
            except ValueError:
                print(f"salary cannot be negative.Enter positive number")

# if file_exists():
#     print(f"file exists")
#     print(read_file())
# else:
#     print("file does not exist")  

employee_count = get_employee_count()
proccess_management(employee_count)
write_csv_file(employees)
