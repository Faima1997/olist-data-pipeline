import duckdb

con = duckdb.connect('data/olist.duckdb')

results = con.execute("SELECT * FROM customers_with_orders LIMIT 5").fetchall()

for row in results:
    print(row)

con.close()

