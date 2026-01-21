# Define salary logic function 

def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12

def salary_category(annual_salary):
    if annual_salary >= 1200000:
        return 'High income'
    elif annual_salary >= 600000:
        return 'Good salary'
    else:
        return 'Need to improve skill'
