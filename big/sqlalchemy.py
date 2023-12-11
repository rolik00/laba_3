import time
import sqlalchemy as db

engine = db.create_engine("sqlite:///nyc_yellow_big.db")
conn = engine.connect()
q1 = db.text('''SELECT "VendorID", count(*) FROM trips GROUP BY 1;''')
q2 = db.text('''SELECT "passenger_count", avg(total_amount) FROM trips GROUP BY 1;''')
q3 = db.text('''SELECT "passenger_count", strftime('%Y', "tpep_pickup_datetime"), count(*) FROM trips GROUP BY 1, 2;''')
q4 = db.text('''SELECT "passenger_count", strftime('%Y', "tpep_pickup_datetime"), round("trip_distance"), count(*) FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;''')

sum = 0
print("First query")
for i in range(10):
    t0 = time.perf_counter()
    result = conn.execute(q1)
    t1 = time.perf_counter()
    sum += (t1 - t0)
    if i == 9:
        print("Result: ", end='')
        for row in result: print(row)
        print("Average time: ", sum / 10)

sum = 0
print("Second query")
for i in range(10):
    t0 = time.perf_counter()
    result = conn.execute(q2)
    t1 = time.perf_counter()
    sum += (t1 - t0)
    if i == 9:
        print("Result: ", end='')
        for row in result: print(row)
        print("Average time: ", sum / 10)

sum = 0
print("Third query")
for i in range(10):
    t0 = time.perf_counter()
    result = conn.execute(q3)
    t1 = time.perf_counter()
    sum += (t1 - t0)
    if i == 9:
        print("Result: ", end='')
        for row in result: print(row)
        print("Average time: ", sum / 10)

sum = 0
print("Forth query")
for i in range(10):
    t0 = time.perf_counter()
    result = conn.execute(q4)
    t1 = time.perf_counter()
    sum += (t1 - t0)
    if i == 9:
        print("Result: ", end='')
        for row in result: print(row)
        print("Average time: ", sum / 10)
