conn = sqlite3.connect(":memory:")  # Lightning-fast processing 
df.to_sql("data", conn)  # Pandas DataFrame to SQL 
result = pd.read_sql(""" 
    WITH ranked AS ( 
        SELECT *, RANK() OVER (PARTITION BY region ORDER BY sales DESC) as rank 
        FROM sales 
    ) 
    SELECT * FROM ranked WHERE rank <= 3 
""", conn) 
