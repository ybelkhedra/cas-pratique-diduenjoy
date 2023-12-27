import pandas as pd
from src.package import Package
from src.item import Item
from src.order import Order

def open_excel_file(path):
    dataframe = pd.read_excel(path)
    return dataframe

def create_orders(orders_file_path):
    orders_excel = open_excel_file(orders_file_path)

    packages = {}

    for index, row in orders_excel.iterrows():
        package_id = row['packages']
        item_id = row['items']

        # Create package if it does not exist
        if package_id not in packages:
            packages[package_id] = Package(package_id, 0)
        
        # Create item if it does not exist
        if not packages[package_id].has_item(item_id):
            packages[package_id].add_item(Item(item_id))
        
        label = row['lables']
        value = row['values']
        packages[package_id][item_id].update_by_label(label, value)


    # Update item_id to be unique
    items_id = []
    for package_id in packages:
        for item in packages[package_id].get_items():
            if item.get_id() in items_id:
                item.update_by_label("item_id", items_id[-1] + 1)
            items_id.append(item.get_id())

    for package_id in packages:
        print(packages[package_id])
        packages[package_id].print_items()
    
    order = Order(0, "Test")
    for package_id in packages:
        order.add_package(packages[package_id])
    
    return order