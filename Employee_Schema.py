import pyodbc

# Hardcoded Global variables used connect to DB
server = 'HCL-02-NEW-12\SQLEXPRESS04'
database = 'lahyasri'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class TableCreationError(Exception):
    def __str__(self):
        return "table created"
class employee_schema():
    def create_table(self):
        try:
            query='''
                    create table lahyasri_table
                    (
                    emp_id int NOT NULL,
                    NameOfEmployee varchar(50),
                    Salary int,
                    Project varchar(50),
                    PRIMARY KEY(emp_id)
                     )
                '''
            cursor.execute(query)
            cnxn.commit()
        except TableCreationError as h:
            print(h)
obj=employee_schema()
obj.create_table()