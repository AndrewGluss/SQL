import pymysql # pip install pymysql
from config import host, user, password, db_name # create config.py with host='your host', user='user', password='password', db_name='db_name'

try:
    connection = pymysql.connect(host=host, port=3306, user=user, password=password, database=db_name, cursorclass=pymysql.cursors.DictCursor)
    print('successfully connection')
    try:
        # cursor = connection.cursor()
        with connection.cursor() as cursor:
            insert_table_query = "INSERT INTO guitars(name, color, price) VALUES ('Ibanez S420', 'Black', 400.00);"
            #insert_table_query = "INSERT INTO guitars(name, color, price) VALUES ('Ibanez RG7321', 'Black', 375.00);"
            #insert_table_query = "INSERT INTO guitars(name, color, price) VALUES ('Fernandes V-Hawk', 'Black', 179.00);"
            cursor.execute(insert_table_query)
            connection.commit()
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM guitars;"
            cursor.execute(select_all_rows)

            rows = cursor.fetchall()
            for row in rows:
                print(row)
    finally:
        connection.close()
except Exception as ex:
    print('Connection refused...')
    print(ex)
