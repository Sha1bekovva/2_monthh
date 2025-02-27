import hmw_8 as db_main
connect_to_db = db_main.create_connection('''homework.db''')
db_main.city_print(connect_to_db)
while True:
    add = int(input("""Вы можете отобразить список учеников по выбранному id 
    города из перечня городов выще, для выхода из программы введите 0:"""))
    if add == 0:
        print("ВЫХОД")
        break
    else:
        db_main.stu_print(connect_to_db,add)
