import pymysql # pip install pymysql
from config import host, user, password, db_name # create config.py with host='your host', user='user', password='password', db_name='db_name'

try:
    connection = pymysql.connect(host=host, port=3306, user=user, password=password, database=db_name, cursorclass=pymysql.cursors.DictCursor)
    print('successfully connection')
    try:
        # cursor = connection.cursor()
        with connection.cursor() as cursor:
            create_table_query = "CREATE TABLE guitars(id int(11) AUTO_INCREMENT, name VARCHAR(30), color VARCHAR(10), price DECIMAL(7,2), PRIMARY KEY (`id`));"
            cursor.execute(create_table_query)
            print("Table created")
    finally:
        connection.close()
except Exception as ex:
    print('Connection refused...')
    print(ex)