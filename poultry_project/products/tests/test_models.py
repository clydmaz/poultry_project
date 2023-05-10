import pytest

pytestmark = pytest.mark.django_db

from .. models import Product

from . factories import ProductFactory

def test___str__():
    product = ProductFactory()

    assert product.__str__() == product.product_name
    assert str(product) == product.product_name