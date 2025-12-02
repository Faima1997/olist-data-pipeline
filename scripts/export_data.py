import duckdb
import os

# Connect to your DuckDB database file (adjust path if needed)
con = duckdb.connect('data/olist.duckdb')

# Folder to save CSV exports
export_folder = 'data/exported'
os.makedirs(export_folder, exist_ok=True)

# List of tables or views you want to export to CSV
tables_to_export = [
    'customers_with_orders',  # example transformed table/view you created
    # Add other tables or views if needed
]

for table in tables_to_export:
    csv_path = os.path.join(export_folder, f"{table}.csv")
    print(f"Exporting {table} to {csv_path}...")
    
    # Export to CSV with headers
    con.execute(f"COPY (SELECT * FROM {table}) TO '{csv_path}' (HEADER, DELIMITER ',')")
    
print("Export complete!")

con.close()

