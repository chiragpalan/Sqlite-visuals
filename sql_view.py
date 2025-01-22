
# read_db.py
import sqlite3
import pandas as pd

def read_tables(database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    # Get table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    for table_name in tables:
        table_name = table_name[0]
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, conn)
        
        # Drop duplicate rows based on 'Datetime' column
        df = df.drop_duplicates(subset='Datetime')
        
        # Get last 30 rows
        last_30_rows = df.tail(30)
        
        print(f"Table: {table_name}")
        print(last_30_rows)
        print("\n")
    
    conn.close()

if __name__ == "__main__":
    database_path = 'stock_predictions_rnn_v3/predictions/predictions.db'  # Update with the correct path if needed
    read_tables(database_path)
