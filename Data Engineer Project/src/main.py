from extract import extract_data
from transform import transform_data
from load import load_data

def main():

    customers, products, orders = extract_data()

    customers, products, orders = transform_data(
        customers,
        products,
        orders
    )

    load_data(
        customers,
        products,
        orders
    )

if __name__ == "__main__":
    main()