import time
import duckdb

conn = duckdb.connect('nyc_yellow_big.duckdb')
cursor = conn.cursor()
#Creation the table in duckdb

'''cursor.execute(
"CREATE TABLE trips AS SELECT * FROM read_csv_auto('nyc_yellow_big.csv');"
)'''

q1 = 'SELECT VendorID, count(*) FROM trips GROUP BY 1;'
q2 = 'SELECT passenger_count, avg(total_amount) FROM trips GROUP BY 1;'
q3 = '''SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), count(*) FROM trips GROUP BY 1, 2;'''
q4 = '''SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), round(trip_distance), count(*) FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;'''

sum = 0
print("First query")
for i in range(10):
    t0 = time.perf_counter()
    result = cursor.execute(q1).fetchall()
    t1 = time.perf_counter()
    sum += (t1 - t0)
    if i == 9:
        print("Result: ", result)
        print("Average time: ", sum / 10)

sum = 0
print("Second query")
for i in range(10):
    t0 = time.perf_counter()
    result = cursor.execute(q2).fetchall()
    t1 = time.perf_counter()
    sum += (t1 - t0)
    if i == 9:
        print("Result: ", result)
        print("Average time: ", sum / 10)

sum = 0
print("Third query")
for i in range(10):
    t0 = time.perf_counter()
    result = cursor.execute(q3).fetchall()
    t1 = time.perf_counter()
    sum += (t1 - t0)
    if i == 9:
        print("Result: ", result)
        print("Average time: ", sum / 10)

sum = 0
print("Forth query")
for i in range(10):
    t0 = time.perf_counter()
    result = cursor.execute(q4).fetchall()
    t1 = time.perf_counter()
    sum += (t1 - t0)
    if i == 9:
        print("Result: ", result)
        print("Average time: ", sum / 10)

cursor.close()
conn.close()
