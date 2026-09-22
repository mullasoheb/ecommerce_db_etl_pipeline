def transform_data(customers, products, orders):

    customers = customers.drop_duplicates()

    products = products.drop_duplicates()

    orders = orders.drop_duplicates()

    orders["quantity"] = orders["quantity"].fillna(1)

    orders["order_date"] = orders["order_date"].astype(str)

    return customers, products, orders