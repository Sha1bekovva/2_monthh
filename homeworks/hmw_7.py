import sqlite3

connection = sqlite3.connect('''hw.db''')

def create_table(connection,sql): #создание таблицы
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_products(connection,product):#добавление продуктов
    try:
        sql = '''INSERT INTO products
        (products_title,
        price,
        quantity)
        VALUES(?,?,?)'''
        cursor = connection.cursor()
        cursor.execute(sql,product)
        connection.commit()

    except sqlite3.Error as e:
        print(e)

def update_products_quantity(connection,product):# изменение количества продукта по айди
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_products_price(connection,product):# изменение цены продукта по айди
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def delete_products(connection, id): #удаление продукта по айди
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def select_products(connection):# функция вывода в консоль таблицы
    try:
        sql = '''SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_limit(connection,limit): # по лимиту цены
    try:
        sql = '''SELECT * FROM products WHERE price <= ?'''
        cursor = connection.cursor()
        cursor.execute(sql,(limit,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)
def select_products_limit2(connection,limit): #по лимиту количества
    try:
        sql = '''SELECT * FROM products WHERE quantity >= ?'''
        cursor = connection.cursor()
        cursor.execute(sql,(limit,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_limit3(connection):# По названию
    try:
        sql = '''SELECT * FROM products WHERE products_title LIKE 'To%' '''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    products_title VARCHAR(200) NOT NULL,
    price FLOAT(10,2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

connect_to_db = connection
if connect_to_db is not None:
    print('Connection succesfully!')
    # create_table(connect_to_db, sql_to_create_products_table)
    #вся цена тут за кило продукта
    # insert_products(connect_to_db, ('Tomatos_from_Kazakhstan', 90.70, 120))
    # insert_products(connect_to_db, ('Apples', 70, 80))
    # insert_products(connect_to_db, ('Aples"Golden"', 120.90, 20))
    # insert_products(connect_to_db, ('Watermelon_Osh', 20, 10))
    # insert_products(connect_to_db, ('Watermelon_Bishkek', 27.70, 50))
    # insert_products(connect_to_db, ('Potatoes', 40, 100))
    # insert_products(connect_to_db, ('Onion', 60.60, 100)
    # insert_products(connect_to_db, ('Onian_violet', 90, 72))
    # insert_products(connect_to_db, ('Banana', 160.50, 140))
    # insert_products(connect_to_db, ('Dragonfruit', 200, 50))
    # insert_products(connect_to_db, ('Melon', 22, 50))
    # insert_products(connect_to_db, ('Appricots', 100.50, 100))
    # insert_products(connect_to_db, ('Grape', 190.50, 200))
    # insert_products(connect_to_db, ('Grape_Kyrgyzstan', 160.50, 210))

    """проверка функций"""
    # update_products_quantity(connect_to_db,(300,4))
    # update_products_price(connect_to_db, (100, 7))
    # delete_products(connect_to_db,5)
    # select_products(connect_to_db)
    # select_products_limit(connect_to_db,100)
    # select_products_limit2(connect_to_db,5 )
    select_products_limit3(connect_to_db)


    print("all right")
    connect_to_db.close()
