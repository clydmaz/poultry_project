import pytest
from pytest_django.asserts import(
    assertContains,
    assertRedirects
)

from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware

from django.test import RequestFactory

from poultry_project.users.models import User
from .. models import Product
from .. views import (
    product_add_view,
    UpdateProductView,
    DeleteProductView,
    product_details_view,
    product_list_view
)

from . factories import ProductFactory

pytestmark = pytest.mark.django_db

def test_good_product_list_view_expanded(rf):
    #Determine the url
    url = reverse("products:list")
    #rf is pytest shotcut for django.test.Requestfactory
    #it is for generating a request as if a user is accessing the cheese listview
    request = rf.get(url)
    #lets pass in the request to the product_list_view() method to
    #get an HTTP response served up by Django.
    #remember product_list_view() is a callable object on the ListProductView
    response = product_list_view(request)
    # We will test that the HTTP response has 'Product List' 
    # in the HTML and it has a 200 response code
    assertContains(response,'Products List')
    # assertContains also tests for HTTP status

def good_product_detail_view(rf):#to be debuged
    # order some products from the factory
    product = ProductFactory()
    #make a request for our new product
    url = reverse("products:detail", kwargs={'slug':product.slug})
    request = rf.get(url)

    #use the request to get the response
    response = product_details_view(request, slug = product.slug)

    #test that the response is valid
    assertContains(response, product_name=product.product_name)

def test_good_product_create_view(rf, admin_user):
    #order some product form the factory
    product = ProductFactory()

    # Make a request for our new product
    url = reverse("products:add")
    request = rf.get(url)
    # add an autheticated user
    request.user = admin_user

    # use the request to get the response
    response = product_add_view(request)

    #test that the response is valid
    assert response.status_code == 200

def test_product_list_contains_2_cheeses(rf):
    # Create two products from Product factory
    product1 = ProductFactory()
    product2 = ProductFactory()

    # Createa request and the a response
    url = reverse("products:list")
    request = rf.get(url)
    response = product_list_view(request)

    # test that the response contains both product names
    assertContains(response, product1.product_name)
    assertContains(response, product2.product_name)

def detail_contains_product_data(rf):#to be debbuged
    #create a new product
    product = ProductFactory()
    #make a request for our pnew product
    url = reverse("products:detail",
                  kwargs={'slug':product.slug})
    request = rf.get(url)
    #use the request to generate a response
    response = product_details_view(request, slug=product.slug)
    #lets test our product details
    assertContains(response, product.product_name)
    assertContains(response, str(product.unit_price))
    
def test_product_create_form_valid(rf, admin_user):
    #submit the product form

    form_data = {
        "product_id": "0023",
        "product_name": "hyliner",
        "description": "a layers type",
        "unit_of_measure": "unit",
        "unit_price": 4.7
        }
    request = rf.post(reverse("products:add"),form_data)
    request.user = admin_user
    response = product_add_view(request)

    #get product based on the name
    product = Product.objects.get(product_name="hyliner")

    # test that the product matches our form
    assert product.description == "a layers type"
    assert product.product_id == "0023"
    assert product.unit_of_measure == "unit"
    assert product.unit_price == 4.7
    assert product.creator == admin_user