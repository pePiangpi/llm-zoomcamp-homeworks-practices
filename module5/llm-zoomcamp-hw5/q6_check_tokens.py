import sqlite3
import pandas as pd

# 1. Load the SQLite data into a pandas DataFrame
conn = sqlite3.connect("traces.db")
df = pd.read_sql("SELECT * FROM spans", conn)
conn.close()

# 2. Filter for the llm spans and check the input tokens
llm_spans = df[df["name"] == "llm"]
print(llm_spans[["name", "input_tokens"]])