import duckdb

con = duckdb.connect('data/olist.duckdb')

tables = con.execute("SHOW TABLES").fetchall()
for (table_name,) in tables:
    print(f"\nSchema for table: {table_name}")
    schema = con.execute(f"DESCRIBE {table_name}").fetchall()
    for col in schema:
        print(col)

con.close()

