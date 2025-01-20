from datetime import datetime, timedelta
import psycopg2
import time

ship_date = (datetime(1998, 12, 1) - timedelta(days=90)).date()

params = {
    'ship_date': ship_date
}

query = """
SELECT
    l_returnflag,
    l_linestatus,
    SUM(l_quantity) AS sum_qty,
    SUM(l_extendedprice) AS sum_base_price,
    SUM(l_extendedprice * (1 - l_discount)) AS sum_disc_price,
    SUM(l_extendedprice * (1 - l_discount) * (1 + l_tax)) AS sum_charge,
    avg(l_quantity) AS avg_qty,
    avg(l_extendedprice) AS avg_price,
    avg(l_discount) AS avg_disc,
    count(*) AS count_order
FROM
    lineitem
WHERE
    l_shipdate <= %(ship_date)s
GROUP BY
    l_returnflag,
    l_linestatus
ORDER BY
    l_returnflag,
    l_linestatus;
"""

conn = psycopg2.connect(
    dbname="tpch3",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
start_time = time.perf_counter()
cursor.execute(query, params)
end_time = time.perf_counter()

result = cursor.fetchall()
with open('/Users/pradeep/Desktop/LeidenUni/sem3/ADM/Assignment 1/ADM-Assignment1/results_python.txt', 'a') as file:
    file.write(f"query 1 for SF-3 postgres\n")
    for row in result:
        file.write(f"{row}\n")
    file.write(f"Query execution time: {end_time - start_time}")
print(result)
print(f"Query execution time: {end_time - start_time}")

cursor.close()
conn.close()
