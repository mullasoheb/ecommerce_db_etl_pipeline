import mysql.connector
from config import DB_CONFIG


def load_data(customers, products, orders):

    conn = mysql.connector.connect(**DB_CONFIG)

    cursor = conn.cursor()

    # Customers
    for _, row in customers.iterrows():
        cursor.execute(
            """
            INSERT INTO customers
            (customer_id,name,city)
            VALUES (%s,%s,%s)
            """,
            tuple(row)
        )

    # Products
    for _, row in products.iterrows():
        cursor.execute(
            """
            INSERT INTO products
            (product_id,product_name,price)
            VALUES (%s,%s,%s)
            """,
            tuple(row)
        )

    # Orders
    for _, row in orders.iterrows():
        cursor.execute(
            """
            INSERT INTO orders
            (order_id,customer_id,
             product_id,quantity,order_date)
            VALUES (%s,%s,%s,%s,%s)
            """,
            tuple(row)
        )

    conn.commit()

    cursor.close()
    conn.close()

    print("Data Loaded Successfully")