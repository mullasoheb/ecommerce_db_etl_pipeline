import pandas as pd

def extract_data():

    customers = pd.read_csv("data/customers.csv")
    products = pd.read_csv("data/products.csv")
    orders = pd.read_csv("data/orders.csv")

    return customers, products, orders