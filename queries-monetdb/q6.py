###########################################
##############   Q6    ####################


from datetime import datetime, timedelta
from pymonetdb import connect
import time

start_date = datetime(1994, 1, 1).date()
end_date = (datetime(1994, 1, 1) + timedelta(days=365)).date()
discount_low = 0.05
discount_high = 0.07
quantity_threshold = 24

query = """
SELECT SUM(l_extendedprice * l_discount) as revenue
FROM lineitem
WHERE l_shipdate >= %(start_date)s
AND l_shipdate < %(end_date)s
AND l_discount BETWEEN %(discount_low)s AND %(discount_high)s
AND l_quantity < %(quantity_threshold)s
"""
params = {
    'start_date': start_date,
    'end_date': end_date,
    'discount_low': discount_low,
    'discount_high': discount_high,
    'quantity_threshold': quantity_threshold
}

conn = connect(username="monetdb", password="monetdb", hostname="localhost", database="tpch1", port=50000)
cursor = conn.cursor()
start_time = time.perf_counter()
cursor.execute(query, params)
end_time = time.perf_counter()

revenue = cursor.fetchone()
with open('/Users/pradeep/Desktop/LeidenUni/sem3/ADM/Assignment 1/ADM-Assignment1/results_python.txt', 'a') as file:
    file.write(f"query 6 for SF-1\n")
    file.write(f"Revenue: {revenue[0]}\n")
    file.write(f"Query execution time: {end_time - start_time}\n")
print(f"Revenue: {revenue}")
print(f"Query execution time: {end_time - start_time}")

conn.close()
