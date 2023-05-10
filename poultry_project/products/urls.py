from django.urls import path

from poultry_project.products.views import (
    product_add_view,
    product_update_view,
    product_delete_view,
    product_list_view,
    product_details_view,
)

app_name = "products"

urlpatterns = [
    path("add/", view=product_add_view, name="add"),
    path("list/", view=product_list_view, name="list"),
    path("details/<str:pk>/", view=product_details_view, name="detail"),
    path("delete/<str:pk>/", view=product_delete_view, name="delete"),
    path("update/<str:pk>/", view=product_update_view, name="update"),

]
