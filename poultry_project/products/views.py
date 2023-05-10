from . models import Product

from django.views.generic import(
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView,
)

class CreateProductView(CreateView):
    model = Product
    fields = ["product_id", "product_name", "description", "unit_of_measure","unit_price", ]

class ListProductView(ListView):
    model = Product

class UpdateProductView(UpdateView):
    model = Product
    fields = ["product_id", "product_name", "description", "unit_of_measure","unit_price", ]

class DeleteProductView(DeleteView):
    model = Product

class ProductDetailsView(DetailView):
    model = Product

product_add_view = CreateProductView.as_view()
product_update_view =UpdateProductView.as_view()
product_delete_view = DeleteProductView.as_view()
product_list_view = ListProductView.as_view()
product_details_view=ProductDetailsView.as_view()