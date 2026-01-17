import pytest

from src.category_and_product import Product


def test_category_init(first_category, second_category):
    # Тесты на проверку инициализацию категорий
    assert first_category.name == "Ноутбуки"
    assert first_category.description == "Для учебы"
    assert len(first_category.products) == 3
    assert first_category.product_count == 6
    assert first_category.category_count == 2  # 2 категории: ноутбуки и продукты питания

    assert second_category.name == "Продукты питания"
    assert second_category.description == "Продукты для обеда"
    assert len(second_category.products) == 3
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
