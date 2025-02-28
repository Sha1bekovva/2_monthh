import sqlite3


def connect_to_db():
    return sqlite3.connect('shop.db')


def get_stores():
    connection = connect_to_db()
    cursor = connection.cursor()

    # Получаем список магазинов
    cursor.execute("SELECT store_id, title FROM stores")
    stores = cursor.fetchall()

    connection.close()
    return stores


def display_products_by_store(store_id):
    connection = connect_to_db()
    cursor = connection.cursor()

    query = """
    SELECT p.title AS product_title, c.title AS category_title, p.unit_price, p.stock_quantity
    FROM products p
    JOIN categories c ON p.category_code = c.code
    WHERE p.store_id = ?
    """
    cursor.execute(query, (store_id,))
    products = cursor.fetchall()

    connection.close()

    if not products:
        print("Продукты не найдены для выбранного магазина.")
    else:
        print("\nСписок продуктов:")
        for product in products:
            print(f"Название продукта: {product[0]}")
            print(f"Категория: {product[1]}")
            print(f"Цена: {product[2]}")
            print(f"Количество на складе: {product[3]}")
            print("-" * 30)


def main():
    while True:
        print("Вы можете отобразить список продуктов по выбранному id магазина из")
        print("перечня магазинов ниже, для выхода из программы введите цифру 0:")

        stores = get_stores()

        for i, store in enumerate(stores, start=1):
            print(f"{i}. {store[1]}")  # store[1] это название магазина

        choice = input("Введите id магазина для просмотра продуктов: ")

        if choice == '0':
            print("Выход из программы...")
            break

        try:
            store_id = int(choice)
            if store_id < 1 or store_id > len(stores):
                print("Неверный id магазина. Попробуйте снова.")
            else:
                display_products_by_store(store_id)
        except ValueError:
            print("Пожалуйста, введите число.")


if __name__ == "__main__":
    main()


sql_to_create_categories_table = '''
CREATE TABLE categories (
    code VARCHAR(2) PRIMARY KEY,  
    title VARCHAR(150) NOT NULL   
)
'''

sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY,               
    title VARCHAR(250) NOT NULL,           
    category_code VARCHAR(2),             
    unit_price FLOAT,                      
    stock_quantity INTEGER,               
    store_id INTEGER,                      
    FOREIGN KEY (category_code) REFERENCES categories(code), 
    FOREIGN KEY (store_id) REFERENCES stores(store_id)         
)
'''

sql_to_create_stores_table = '''
CREATE TABLE stores (
    store_id INTEGER PRIMARY KEY,          
    title VARCHAR(100) NOT NULL             
)
'''


