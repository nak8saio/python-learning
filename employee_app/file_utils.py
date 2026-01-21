import csv
import os

CSV_FILE = "employees.csv"

def file_exists():
    return os.path.exists(CSV_FILE)

def write_csv_file(employees):
    if not file_exists():
        return 'file not found!'
    else:
        with open(CSV_FILE, 'w', newline='') as file:
            writer =  csv.writer(file)
            writer.writerow(['Name','Monthly Salary','Annual Salary','Category'])

            for emp in employees:
                writer.writerow(emp)

def read_file():
    if not file_exists():
        return 'File not found!'
    else:
        with open(CSV_FILE, 'r') as file:
            return file.read()    
    