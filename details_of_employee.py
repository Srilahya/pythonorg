class insertexception(Exception):
    def __str__(self):
        return "projent name not in list of the projects"
class id_exception(Exception):
    def __str__(self):
        return "id already exist enter new id for employee"
class bonus_ex(Exception):
    def __str__(self):
        return "bonus is very high enter with in range"
class schema:
    # To initialize connection string to connect database
    # To create cursor object to execute sql commands
    def __init__(self):
        # In this connection string server,database,user Id and password is included.
        # for connnecting database to perform operations on Database table.
        self.cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=HCL-02-NEW-12\SQLEXPRESS04;DATABASE=lahyasri;UID=capstone;PWD=Capstone@123')
        self.cursor = self.cnxn.cursor()
    def create_table(self):
        query=''' CREATE TABLE employee_table (emp_id int NOT NULL,
                    NameOfEmployee varchar(50),
                    Salary int,
                    Project varchar(50),
                    PRIMARY KEY(emp_id)); '''
        self.cursor.execute(query)
        self.cnxn.commit()
import pyodbc
class EMPLOYEE:
    def __init__(self):
        #In this connection string server,database,user Id and password is included.
        # for connnecting database to perform operations on Database table.
        self.cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=HCL-02-NEW-12\SQLEXPRESS04;DATABASE=lahyasri;UID=capstone;PWD=Capstone@123')
        self.cursor = self.cnxn.cursor()
        self.project=['c','java','python']
    def add_employee_details(self,id,name,salary,project):
        query_for_search_id=''' select emp_id from lahyasri_table '''
        format_query_for_search_id= query_for_search_id.format(id)
        value_of_query_for_search_id=self.cursor.execute(format_query_for_search_id)
        f=False
        for i in value_of_query_for_search_id:
            if i.emp_id == id:
                f=True
                break
        if f:
            try:
                raise id_exception
            except id_exception as id_ex:
                print(id_ex)
        else:
            query = ''' INSERT INTO lahyasri_table (emp_id,NameOfEmployee, Salary,Project) values ({0},'{1}',{2},'{3}') '''
            insertquery = query.format(id, name, salary, project)
            if project in self.project:
                self.cursor.execute(insertquery)
                self.cnxn.commit()
                print("details insert successfully in db")
            else:
                try:
                    raise insertexception
                except insertexception as ex:
                    print(ex)
    def update_details(self,id,project=' ',salary=0):
        if salary !=0:
            query_for_salary_uptate= ''' UPDATE lahyasri_table SET salary = {0} where emp_id = {1} '''
            insertquery_for_salary_update=query_for_salary_uptate.format(salary,id)
            self.cursor.execute(insertquery_for_salary_update)
            self.cnxn.commit()
            print("updated succsesfully")
        if project:
            quairy_for_project= ''' UPDATE lahyasri_table SET project = '{0}' where emp_id = {1} '''
            inertquairy_for_project_update = quairy_for_project.format(project, id)
            self.cursor.execute(inertquairy_for_project_update)
            self.cnxn.commit()
            print("update successfully")
    def display_employee_details(self):
        query_for_display_details='''select * from employee_table '''
        values=self.cursor.execute(query_for_display_details)
        for i in values:
            print("employee id ",i.emp_id," employee name ",i.name," salary ",i.salary," project ",i.project)
    def delet_employee_details(self,id):
        query=''' DELETE from employee_table where emp_id = {0} '''.format(id)
        self.cursor.execute(query)
        self.cnxn.commit()
        print("deleted successfully")
    def add_bonus(self,id,bonus):
        if bonus > 0 and bonus <= 2:
            query = ''' select salary from lahyasri_table where emp_id = {}'''.format(id)
            value = self.cursor.execute(query)
            for i in value:
                salary = i.salary
            bonus_and_bonus = salary + salary * bonus
            query_for_update_bonus = ''' UPDATE lahyasri_table SET salary = {0} where emp_id = {1} '''.format(
                bonus_and_bonus, id)
            self.cursor.execute(query_for_update_bonus)
            self.cnxn.commit()
            print("bouns updated successfully")
        else:
            try:
                raise bonus_ex
            except bonus_ex as ex:
                print(ex)
obj=EMPLOYEE()
obj.add_employee_details(5,'sri',15,'java')
obj.update_details(5,project='python')
obj.display_employee_details()

