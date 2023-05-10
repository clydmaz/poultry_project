from django.template.defaultfilters import slugify

import factory
import factory.fuzzy

from .. models import Product

class ProductFactory(factory.django.DjangoModelFactory):
    
    product_id = factory.fuzzy.FuzzyText()
    product_name = factory.fuzzy.FuzzyText()
    description =factory.Faker('paragraph', nb_sentences=3)
    unit_price = factory.fuzzy.FuzzyFloat(low=3.6, high=8.0, precision=2)
    quantity_in_stock = factory.fuzzy.FuzzyInteger(low=0)
    unit_of_measure = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.product_name))

    class Meta:
        model = Product