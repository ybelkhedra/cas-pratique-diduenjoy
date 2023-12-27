from src.package import Package

class Order:
    def __init__(self, order_id, name):
        self.order_id = order_id
        self.name = name
        self.packages = []

    def getId(self):
        return self.order_id

    def add_package(self, package):
        self.packages.append(package)

    def hasPackage(self, package_id):
        for package in self.packages:
            if package.getId() == package_id:
                return True
        return False

    def get_package_by_id(self, package_id):
        for package in self.packages:
            if package.getId() == package_id:
                return package
        return None

    def __getitem__(self, package_id):
        return self.get_package_by_id(package_id)
    
    def __str__(self):
        return f"Order ID : {self.order_id}, Name : {self.name}, Packages : {self.packages}"

    def print_packages(self):
        for package in self.packages:
            print(package)