import duckdb
import os

# Connect to DuckDB database file inside the data folder
con = duckdb.connect('data/olist.duckdb')

# Folder where your CSV files are
raw_data_folder = 'data/raw'

# Map CSV filenames to table names
csv_to_table = {
    'olist_customers_dataset.csv': 'customers',
    'olist_orders_dataset.csv': 'orders',
    'olist_order_items_dataset.csv': 'order_items',
    'olist_products_dataset.csv': 'products',
    'olist_sellers_dataset.csv': 'sellers',
    'olist_order_payments_dataset.csv': 'payments',
    'olist_order_reviews_dataset.csv': 'reviews',
    'olist_geolocation_dataset.csv': 'geolocation',
    'product_category_name_translation.csv': 'product_category_name_translation'
}

for csv_file, table_name in csv_to_table.items():
    csv_path = os.path.join(raw_data_folder, csv_file)
    if not os.path.exists(csv_path):
        print(f"ERROR: File {csv_path} does NOT exist!")
    else:
        print(f'Loading {csv_file} into table {table_name}...')
        con.execute(f"""
            CREATE OR REPLACE TABLE {table_name} AS
            SELECT * FROM read_csv_auto('{csv_path}')
        """)

print('Data ingestion complete!')
con.close()

