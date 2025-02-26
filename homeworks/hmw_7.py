import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(connection, create_table_sql):
    try:
        cursor= connection.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

db_name = '''hw.db'''

sql_to_create_employees_table = '''
CREATE TABLE employees (
    id INTEGER  PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT  NOT NULL DEFAULT 0.0,
    quantity INT NOT NULL DEFAULT 0,
    
)

'''
my_connection = create_connection(db_name)
if my_connection is not None:
    print('Connection established')
    create_table(my_connection, sql_to_create_employees_table)
    my_connection.close()