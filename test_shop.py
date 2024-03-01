"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product_book():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def product_pen():
    return Product("pen", 15, "This is a good pen", 350)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product_book):
        # TODO напишите проверки на метод check_quantity
        assert product_book.check_quantity(1000)

    def test_product_buy(self, product_book):
        # TODO напишите проверки на метод buy
        product_book.buy(150)
        assert product_book.quantity == 850

    def test_product_buy_more_than_available(self, product_pen):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product_pen.buy(4231)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_zero_product(self, cart, product_book):
        with pytest.raises(ValueError):
            cart.add_product(product_book, 0)

    def test_add_product_in_a_cart(self, cart, product_book):
        cart.add_product(product_book, 7)
        assert cart.products[product_book] == 7
        cart.add_product(product_book, 11)
        assert cart.products[product_book] == 18

    def test_remove_from_cart(self, cart, product_book):
        cart.add_product(product_book, 38)
        cart.remove_product(product_book, 29)
        assert cart.products[product_book] == 9

    def test_remove_from_cart_same_product(self, cart, product_book):
        cart.add_product(product_book, 10)
        cart.remove_product(product_book,10)
        assert product_book not in cart.products

    def test_remove_from_cart_negative(self, cart, product_book):
        cart.add_product(product_book, 10)
        cart.remove_product(product_book, 100)
        assert product_book not in cart.products

    def test_clean_cart(self, cart, product_book, product_pen):
        cart.add_product(product_book, 78)
        cart.add_product(product_pen, 10)
        cart.clear()
        assert len(cart.products) == 0

    def test_books_price(self, cart, product_book):
        cart.add_product(product_book, 17)
        assert cart.get_total_price() == 1700
        cart.remove_product(product_book, 3)
        assert cart.get_total_price() == 1400
        cart.remove_product(product_book, 14)
        assert cart.get_total_price() == 0


