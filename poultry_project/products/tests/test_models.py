import pytest

pytestmark = pytest.mark.django_db

from .. models import Product

from . factories import ProductFactory

def test___str__():
    product = ProductFactory(product_name = "goose")
    
    assert product.__str__() == "goose"
    assert str(product) == "goose"