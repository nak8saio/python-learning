from database import get_connection

def insert_employee(emp):
    conn = get_connection()
    cusor = conn.cursor()

    cusor.execute("INSERT INTO employees('name','monthly_salary','annual_salary','category') VALUES (?,?,?,?)",
                  (emp.name,emp.monthly_salary,emp.annual_salary(),emp.category())
                  )
    conn.commit()
    conn.close()

def fetch_employees():
    conn = get_connection()
    cusor = conn.cursor()

    cusor.execute("SELECT * FROM employees")
    rows = cusor.fetchall()
    conn.close
    return rows

