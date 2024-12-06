import sqlite3

def load_data_to_db(df, db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create sales_data table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales_data (
                ID TEXT PRIMARY KEY,
                OrderId INTEGER ,
                OrderItemId TEXT,
                QuantityOrdered INTEGER,
                ItemPrice REAL,
                PromotionDiscount REAL,
                TotalSales REAL,
                NetSales REAL,
                Region TEXT
            )
        ''')

        # Insert data
        df.to_sql('sales_data', conn, if_exists='replace', index=False)

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error loading data into database: {e}")
