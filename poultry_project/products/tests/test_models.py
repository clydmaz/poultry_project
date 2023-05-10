import pytest

pytestmark = pytest.mark.django_db

from .. models import Product

def test___str__():
    product = Product.objects.create(
        product_id = "cpl0001",
        product_name = "goose",
        description = "duck like fowl with long neck",
        unit_price = 0.1,
        quantity_in_stock = 7,
        unit_of_measure = "unit"
    )

    assert product.__str__() == "goose"
    assert str(product) == "goose"