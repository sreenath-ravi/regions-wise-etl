import sqlite3

def validate_data(db_path='sales_data.db'):

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM sales_data")
    total_records = cursor.fetchone()[0]


    cursor.execute("SELECT Region, SUM(TotalSales) FROM sales_data GROUP BY Region")
    total_sales_by_region = cursor.fetchall()


    cursor.execute("SELECT AVG(NetSales) FROM sales_data")
    avg_sales_per_transaction = cursor.fetchone()[0]
  

    cursor.execute("SELECT COUNT(ID), COUNT(DISTINCT ID) FROM sales_data")
    counts = cursor.fetchone()
    has_duplicates = counts[0] != counts[1]
    
    conn.close()

    return {
        "total_records": total_records,
        "total_sales_by_region": total_sales_by_region,
        "avg_sales_per_transaction": avg_sales_per_transaction,
        "has_duplicates": has_duplicates
    }
