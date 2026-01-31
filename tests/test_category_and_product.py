import pytest

from src.category_and_product import Category, Product


def test_category_init(first_category, second_category):
    # Тесты на проверку инициализацию категорий
    assert first_category.name == "Ноутбуки"
    assert first_category.description == "Для учебы"
    assert first_category.product_count == 6
    assert first_category.category_count == 2  # 2 категории: ноутбуки и продукты питания

    assert second_category.name == "Продукты питания"
    assert second_category.description == "Продукты для обеда"
    assert second_category.product_count == 6
    assert second_category.category_count == 2  # 2 категории: ноутбуки и продукты питания


def test_product_init(product):
    assert product.name == "Мышка"
    assert product.description == "Мышка для компьютера"
    assert product.price == 1000
    assert product.quantity == 10


def test_product_isinstance(product):
    # Проверки на правильную типизацию данных при инициализации
    assert isinstance(product.price, int)
    assert isinstance(product.name, str)
    assert isinstance(product.description, str)
    assert isinstance(product.quantity, int)


def test_add_product_category(product_add):
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
    )
    category1.add_product(product_add)
    assert category1.product_count == 9


def test_products_print(products_print):
    assert (
        products_print.products
        == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт\nIphone 15, 210000.0 руб. Остаток: 8 шт\n"
    )


def test_new_product(new_product):
    assert new_product.price == 210000.0
    assert new_product.name == "Iphone 15"
    assert new_product.description == "512GB, Gray space"
    assert new_product.quantity == 8


def test_get_set_price(product):
    assert product.price == 1000
    new_price = product.price
    product.price = -50.0
    result = product.price
    assert result == new_price


def test_str_product(product):
    result = str(product.__str__())
    assert result == "Мышка, 1000 руб. Остаток: 10 шт."


def test_str_category(first_category):
    result = str(first_category.__str__())
    assert result == "Ноутбуки, количество продуктов: 10 шт."


def test_add_product(product, product_add):
    result = product + product_add
    assert result == 11000
