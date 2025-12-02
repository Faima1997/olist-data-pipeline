import duckdb
import os

con = duckdb.connect('data/olist.duckdb')

# Create output folder if it doesn't exist
output_folder = 'data/exported'
os.makedirs(output_folder, exist_ok=True)

# Query 1: Orders by status
query1 = """
SELECT order_status, COUNT(*) AS order_count
FROM orders
GROUP BY order_status
ORDER BY order_count DESC
"""

con.execute(query1)
con.execute(f"COPY ({query1.rstrip(';')}) TO '{output_folder}/orders_by_status.csv' WITH (HEADER, DELIMITER ',')")

print("Exported orders_by_status.csv")

# Query 2: Orders by customer city
query2 = """
SELECT c.customer_city, COUNT(*) AS order_count
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_city
ORDER BY order_count DESC
LIMIT 10
"""

con.execute(query2)
con.execute(f"COPY ({query2.rstrip(';')}) TO '{output_folder}/orders_by_city.csv' WITH (HEADER, DELIMITER ',')")

print("Exported orders_by_city.csv")

con.close()
