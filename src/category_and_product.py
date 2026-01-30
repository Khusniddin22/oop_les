class Product:
    """Класс продуктов"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, prod: dict):
        """Принимает на вход параметры товара в словаре и возвращать созданный объект класса"""
        name, description, price, quantity = prod.values()
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер возвращает цену товара"""
        return self.__price

    @price.setter
    def price(self, new_price: float):

        if new_price <= 0.0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                concest = input()
                if concest == "y":
                    self.__price = new_price
                else:
                    print("Отмена понижения цены")


class Category:
    """Класс категорий"""

    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Добавляет товар в список продуктов в категории"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер возвращает строку с описанием товаров"""
        str_prod = ""
        for product in self.__products:
            str_prod += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт\n"
        return str_prod
