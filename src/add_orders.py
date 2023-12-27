import psycopg2
from src.order import Order
from src.package import Package
from src.item import Item

def add_orders(host, database, user, password, orders):
    conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password)

    cursor = conn.cursor()

    for order in orders:
        add_order(cursor, order)
    
    conn.commit()
    cursor.close()
        


def add_order(cursor, order):
    cursor.execute("INSERT INTO orders (order_id, name) VALUES (%s, %s)", (order.get_id(), order.get_name()))
    for package in order.get_packages():
        cursor.execute("INSERT INTO packages (package_id, order_id) VALUES (%s, %s)", (package.get_id(), order.get_id()))
        for item in package.get_items():
            cursor.execute("INSERT INTO items (item_id, Name, Price, Ref, PackageID, Warranty, Duration) VALUES (%s, %s, %s, %s, %s, %s, %s)", (item.get_id(), item["name"], item["price"], item["ref"], package.get_id(), item["warranty"], item["duration"]))
            