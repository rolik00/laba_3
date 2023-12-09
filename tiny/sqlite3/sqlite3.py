import time
import sqlite3
conn = sqlite3.connect('nyc_yellow_tiny.db')
cursor = conn.cursor()
q1 = 'SELECT VendorID, count(*) FROM trips GROUP BY 1;'
q2 = 'SELECT passenger_count, avg(total_amount) FROM trips GROUP BY 1;'
q3 = '''SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), count(*) FROM trips GROUP BY 1, 2;'''
q4 = '''SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), round(trip_distance), count(*) FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;'''
sum = 0
for i in range(10):
    t0 = time.perf_counter()
    cursor.execute(q4)
    result = cursor.fetchall()
    t1 = time.perf_counter()
    print(result, t1 - t0)
    sum += (t1 - t0)
print(sum / 10)
cursor.close()
conn.close()
