class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    # @classmethod
    # def create(cls, *args):
    #     return cls(*args)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def __eq__(self, other):
        return self.name == other.name


def is_product_exists(file, product):
    file.seek(0)
    products_list = file.read().splitlines()
    for temp in products_list:
        args = [tmp.strip() for tmp in temp.split(',')]
        # p = Product.create(*args)
        p = Product(*args)
        if product == p:
            return True
    return False


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        file = open(self.__file_name, 'a+')
        for product in products:
            if is_product_exists(file, product):
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(f'{str(product)}\n')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
