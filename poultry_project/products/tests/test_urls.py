import pytest
from django.urls import reverse, resolve
from . factories import ProductFactory
pytestmark = pytest.mark.django_db

@pytest.fixture
def product():
    return ProductFactory

def test_list_reverse():
    """products:list reverse to /products/list/"""
    assert reverse('products:list')=='/products/list/'

def test_list_resolve():
    """/products/list/ must resolve to products:list."""
    assert resolve('/products/list/').view_name == 'products:list'

def test_add_reverse():
    """products:add should reverse to /products/add/."""
    assert reverse('products:add') == '/products/add/'

def test_add_resolve():
    """/product/add/ must resolve to products:add"""
    assert resolve('/products/add/').view_name == 'products:add'

def detail_reverse(product):
    """products:detail must reverse to /products/details/productslug/."""
    print(f'THE PRODUCT SLUG SHOULD BE THIS {product.slug}')
    url = reverse('products:detail',
                  kwargs={'slug':product.slug}
                  )
    assert url == f'/products/details/{product.slug}/'

def detail_resolve(product):
    """/products/details/slug/ resloves to products:detail. """
    url = f'/products/details/{product.slug}/'
    assert resolve(url).view_name == 'products:details'

