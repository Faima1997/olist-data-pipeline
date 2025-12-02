import duckdb

# Connect to DuckDB database
# Connect using 'data/olist.duckdb' which is relative to the root project folder
con = duckdb.connect('data/olist.duckdb')

# --- 1. Dimensional Flattening Transformation ---
# SQL to create the analytics-ready table by joining customers and orders.
# This implements the T_CWO operation described in the report's methodology.
sql_transformation = """
CREATE OR REPLACE TABLE customers_with_orders AS
SELECT 
    c.customer_id,
    c.customer_unique_id,
    c.customer_zip_code_prefix,
    c.customer_city,
    c.customer_state,
    o.order_id,
    o.order_status
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;
"""

print("Executing dimensional flattening (customers_with_orders)...")
con.execute(sql_transformation)
print("Transformation complete!")

# --- 2. Verification (Optional but Recommended) ---
# Check the resulting table schema and count
tables = con.execute("SHOW TABLES").fetchall()
print(f"Tables in the database: {tables}")

# Check the first few rows of the new table
# results = con.execute("SELECT * FROM customers_with_orders LIMIT 5").fetchall()
# print("\nFirst 5 rows of customers_with_orders:")
# for row in results:
#     print(row)

con.close()
