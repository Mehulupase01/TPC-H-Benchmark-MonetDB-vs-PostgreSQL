# import psycopg2
# from psycopg2 import sql

# # Define your connection parameters
# conn_params = {
#     'dbname': 'your_dbname',
#     'user': 'your_username',
#     'password': 'your_password',
#     'host': 'your_host',
#     'port': 'your_port'
# }

# # Define your query and parameters
# query = """
# SELECT SUM(l_extendedprice * l_discount) as revenue
# FROM lineitem
# WHERE l_shipdate >= %(start_date)s
# AND l_shipdate < %(end_date)s
# AND l_discount BETWEEN %(discount_low)s AND %(discount_high)s
# AND l_quantity < %(quantity_threshold)s
# """

# params = {
#     'start_date': '1994-01-01',
#     'end_date': '1995-01-01',
#     'discount_low': 0.05,
#     'discount_high': 0.07,
#     'quantity_threshold': 24
# }

# def execute_query(query, params):
#     try:
#         # Connect to the PostgreSQL database
#         conn = psycopg2.connect(**conn_params)
#         cursor = conn.cursor()
        
#         # Execute the query
#         cursor.execute(query, params)
        
#         # Fetch the result
#         result = cursor.fetchone()
        
#         # Print the result
#         print(f"Revenue: {result[0]}")
        
#         # Close the cursor and connection
#         cursor.close()
#         conn.close()
        
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     execute_query(query, params)



from datetime import datetime, timedelta
import psycopg2
import time

ship_date = (datetime(1998, 12, 1) - timedelta(days=90)).date()

query = """
SELECT SUM(l_extendedprice * l_discount) as revenue
FROM lineitem
WHERE l_shipdate >= %(start_date)s
AND l_shipdate < %(end_date)s
AND l_discount BETWEEN %(discount_low)s AND %(discount_high)s
AND l_quantity < %(quantity_threshold)s
"""

params = {
    'start_date': '1994-01-01',
    'end_date': '1995-01-01',
    'discount_low': 0.05,
    'discount_high': 0.07,
    'quantity_threshold': 24
}

conn = psycopg2.connect(
    dbname="tpch3",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
start_time = time.perf_counter()
cursor.execute(query, params)
end_time = time.perf_counter()

revenue = cursor.fetchone()
with open('/Users/pradeep/Desktop/LeidenUni/sem3/ADM/Assignment 1/ADM-Assignment1/results_python.txt', 'a') as file:
    file.write(f"query 6 for SF-3 postgres\n")
    file.write(f"Revenue: {revenue[0]}\n")
    file.write(f"Query execution time: {end_time - start_time}\n")
print(f"Revenue: {revenue}")
print(f"Query execution time: {end_time - start_time}")

cursor.close()
conn.close()
