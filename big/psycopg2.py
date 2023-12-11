import time
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="localhost",
                                  port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()

    # Creation database
    #sql_create_database = 'create database postgres_db'
    #cursor.execute(sql_create_database)

    q1 = 'SELECT "VendorID", count(*) FROM public.taxi group by 1;'
    q2 = 'SELECT "passenger_count", avg(total_amount) FROM public.taxi GROUP BY 1;'
    q3 = 'SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), count(*) FROM public.taxi GROUP BY 1, 2;'
    q4 = 'SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), round("trip_distance"), count(*) FROM public.taxi GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;'

    sum = 0
    print("First query")
    for i in range(10):
        t0 = time.perf_counter()
        cursor.execute(q1)
        result = cursor.fetchall()
        t1 = time.perf_counter()
        sum += (t1 - t0)
        if i == 9:
            print("Result: ", result)
            print("Average time: ", sum / 10)

    sum = 0
    print("Second query")
    for i in range(10):
        t0 = time.perf_counter()
        cursor.execute(q2)
        result = cursor.fetchall()
        t1 = time.perf_counter()
        sum += (t1 - t0)
        if i == 9:
            print("Result: ", result)
            print("Average time: ", sum / 10)

    sum = 0
    print("Third query")
    for i in range(10):
        t0 = time.perf_counter()
        cursor.execute(q3)
        result = cursor.fetchall()
        t1 = time.perf_counter()
        sum += (t1 - t0)
        if i == 9:
            print("Result: ", result)
            print("Average time: ", sum / 10)

    sum = 0
    print("Forth query")
    for i in range(10):
        t0 = time.perf_counter()
        cursor.execute(q4)
        result = cursor.fetchall()
        t1 = time.perf_counter()
        sum += (t1 - t0)
        if i == 9:
            print("Result: ", result)
            print("Average time: ", sum / 10)

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
