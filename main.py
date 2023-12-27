import sys
import os
import pandas as pd
from src.package import Package
from src.item import Item
from src.order import Order
from src.create_orders import create_orders
from src.add_orders import add_orders
import argparse

def open_excel_file(path):
    dataframe = pd.read_excel(path)
    return dataframe


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, default="Orders.xlsx", help="path to the xlsx file containing the orders")
    parser.add_argument("-H", "--host", type=str, default="localhost", help="host of the database")
    parser.add_argument("-d", "--database", type=str, default="postgres", help="database name")
    parser.add_argument("-u", "--user", type=str, default="postgres", help="user name")
    parser.add_argument("-p", "--password", type=str, default="postgres", help="password")
    args = parser.parse_args()
    orders_file_path = args.file

    orders_file_path = os.path.join(os.path.dirname(__file__), 'Orders.xlsx')
    orders = create_orders(orders_file_path)
    print(orders)
    add_orders(args.host, args.database, args.user, args.password, [orders])

