import duckdb
import os

# Connect to DuckDB
con = duckdb.connect('data/olist.duckdb')

# Output folder
output_folder = 'data/exported'
os.makedirs(output_folder, exist_ok=True)

# Weekly order counts (batch output)
query = """
SELECT 
    date_trunc('week', order_purchase_timestamp) AS week_start,
    COUNT(*) AS total_orders
FROM orders
GROUP BY week_start
ORDER BY week_start
"""

print("Exporting weekly_orders.csv ...")
con.execute(f"""
    COPY (
        {query}
    )
    TO '{output_folder}/weekly_orders.csv'
    WITH (HEADER, DELIMITER ',')
""")

print("Export complete!")

