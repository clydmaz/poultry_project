
from django.urls import reverse
from django.db import models
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField

class Product(TimeStampedModel):
    product_id = models.CharField("Product Id", max_length=250)
    product_name = models.CharField("The Name Of The Poultry Product", max_length=250)
    description = models.TextField("Product Description")
    unit_price = models.FloatField("Unit Price Dollars")
    quantity_in_stock = models.IntegerField("Units In Stock",default=0)
    unit_of_measure = models.CharField("Unit Of Measurement", max_length=4)
    slug = AutoSlugField("product_address", unique=True, always_update = False, populate_from="product_id")

    def __str__(self) -> str:
        return super().__str__(self.product_name)
    
    def get_absolute_url(self):
        return reverse("products:details", kwargs={"slug": self.slug})
    