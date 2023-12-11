import time
import pandas as pd

data = pd.read_csv(r"D:\Study\бд\laba_3\nyc_yellow_big.csv")

sum = 0
print("First query")
for i in range(10):
    t0 = time.perf_counter()
    result = data.groupby(["VendorID"]).size()
    t1 = time.perf_counter()
    sum += (t1 - t0)
    if i == 9:
        print("Result: ", result)
        print("Average time: ", sum / 10)

sum = 0
print("Second query")
for i in range(10):
    t0 = time.perf_counter()
    result = data.groupby(["passenger_count"])["total_amount"].mean()
    t1 = time.perf_counter()
    sum += (t1 - t0)
    if i == 9:
        print("Result: ", result)
        print("Average time: ", sum / 10)

sum = 0
print("Third query")
for i in range(10):
    t0 = time.perf_counter()
    data['Year'] = pd.to_datetime(data['tpep_pickup_datetime']).dt.year
    result = data.groupby(['passenger_count', 'Year']).size()
    t1 = time.perf_counter()
    sum += (t1 - t0)
    if i == 9:
        print("Result: ", result)
        print("Average time: ", sum / 10)

sum = 0
print("Forth query")
for i in range(10):
    t0 = time.perf_counter()
    data['Year'] = pd.to_datetime(data['tpep_pickup_datetime']).dt.year
    data['trip_distance'] = data['trip_distance'].round()
    result = data.groupby(['passenger_count', 'Year', 'trip_distance']).size().reset_index(name='count').sort_values(['Year', 'count'], ascending=[True, False])
    t1 = time.perf_counter()
    sum += (t1 - t0)
    if i == 9:
        print("Result: ", result)
        print("Average time: ", sum / 10)
