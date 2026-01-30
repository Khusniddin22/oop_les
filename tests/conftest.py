import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Теперь импорт должен работать
from src.category_and_product import Category, Product


@pytest.fixture
def first_category():
    return Category(
        name="Ноутбуки",
        description="Для учебы",
        products=[
            Product(name="Lenovo", description="Норм ноут", price=60000, quantity=5),
            Product(name="Digma", description="Слабоватый", price=20000, quantity=2),
            Product(name="ASUS", description="Хороший ноут", price=100000, quantity=3),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Продукты питания",
        description="Продукты для обеда",
        products=[
            Product(name="Помидоры-черри", description="Помидоры для салата", price=200, quantity=5),
            Product(name="Мясо", description="Мясо для супа", price=700, quantity=2),
            Product(name="Торт", description="Десерт", price=1000, quantity=1),
        ],
    )


@pytest.fixture
def product():
    return Product(
        name="Мышка",
        description="Мышка для компьютера",
        price=1000,
        quantity=10,
    )


@pytest.fixture
def product_add():
    return Product(
        name="Колонка",
        description="Колонка для компьютера",
        price=500,
        quantity=2,
    )


@pytest.fixture
def products_print():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
    )


@pytest.fixture
def new_product():
    return Product.new_product(
        {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8}
    )
