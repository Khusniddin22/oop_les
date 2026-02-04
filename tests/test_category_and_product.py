from pydoc import resolve

import pytest

from src.category_and_product import Category, LawnGrass, Product, Smartphone


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
    assert category1.product_count == 3


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


def test_add_product_identical_products(first_smartphone, second_smartphone):
    """Тест на проверку сложения одинаковых продуктов"""
    result = first_smartphone + second_smartphone
    assert result == 2_000_000.0


def test_add_product_different_products(first_smartphone, first_lawng_rass):
    """Тест на проверку сложения разных категорий продуктов"""
    with pytest.raises(TypeError) as raise_type:
        first_lawng_rass + first_smartphone
    assert "Нельзя складывать продукты разных конкретных типов." in str(raise_type)


def test_add_product_of_category_error(first_category):
    """Тест на добавление продукта в категорию не относящийся к классу Продукты"""
    with pytest.raises(TypeError) as raise_type:
        first_category.add_product("Not a product")
    assert "Нельзя добавить категорию не относящуюся к Продуктам." in str(raise_type)


def test_MixinPrint(capsys):
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    captured = capsys.readouterr()

    expected_output = "Product, Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14\n"

    assert captured.out == expected_output


def test_MixinPrint_repr():
    # Тест на правильный возврат строки метода __repr__
    product4 = Product("Iphone", "64GB", 50000.0, 5)
    assert repr(product4) == "Product, Iphone, 64GB, 50000.0, 5"


def test_MixinPrint_Smartphone(capsys):
    smart1 = Smartphone("Samsung Galaxy S10", "256GB", 20000.0, 1, 90.5, "S10", 256, "Серый")
    captured = capsys.readouterr()
    expected_result = "Smartphone, Samsung Galaxy S10, 256GB, 20000.0, 1\n"
    assert captured.out == expected_result


def test_mixinPrint_LawnGrass(capsys):
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    captured = capsys.readouterr()
    expected_result = "LawnGrass, Газонная трава, Элитная трава для газона, 500.0, 20\n"
    assert captured.out == expected_result
