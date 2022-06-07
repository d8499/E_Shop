from xml.etree.ElementInclude import include


# Custom path of model must be included
from .product import Product

#  Also it must be registered in admin.py  for Example:
# from .models.product import Product
# admin.site.register(Product)

from .category import Category
