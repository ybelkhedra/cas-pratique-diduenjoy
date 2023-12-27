from src.package import Package

class Order:
    def __init__(self, order_id, name):
        self.order_id = order_id
        self.name = name
        self.packages = []

    def get_id(self):
        return self.order_id
    
    def get_name(self):
        return self.name

    def has_package(self, package_id):
        for package in self.packages:
            if package.get_id() == package_id:
                return True
        return False
    
    def add_package(self, package):
        self.packages.append(package)

    def get_package_by_id(self, package_id):
        for package in self.packages:
            if package.get_id() == package_id:
                return package
        return None

    def __getitem__(self, package_id):
        return self.get_package_by_id(package_id)

    def __len__(self):
        return len(self.packages)
    
    def get_packages(self):
        return self.packages
    
    def __str__(self):
        return f"Order ID : {self.order_id}, Name : {self.name}, Packages : {self.packages}"

    def print_packages(self):
        for package in self.packages:
            print(package)