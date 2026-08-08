import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("traces.db")
cursor = conn.cursor()

# Query to sum up the duration (end_time - start_time) for each span, excluding 'rag'
query = """
    SELECT name, SUM(end_time - start_time) AS total_duration
    FROM spans
    WHERE name != 'rag'
    GROUP BY name
"""

cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(f"Span: {row[0]} | Total Duration: {row[1]}")

conn.close()