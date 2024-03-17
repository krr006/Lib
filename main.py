import psycopg2
from config import *


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )   
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute("select * from student where student_group = %s order by id;", ('b22-205',))
        rows = cursor.fetchall()

        for r in rows:
            print(r)



except psycopg2.Error as e:
    print("An error occurred: ")
    print(e)    




finally:
    if connection:
        connection.close()

        print("Connection closed")

