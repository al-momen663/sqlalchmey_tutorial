import sqlite3

conn = sqlite3.connect('analytics.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS metrics (model TEXT, accuracy REAL)')
cursor.execute('INSERT INTO metrics VALUES (?, ?)', ('XGBoost', 0.94))
conn.commit()
conn.close()
