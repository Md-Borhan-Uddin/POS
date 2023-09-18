from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class BaseModel(models.Model):
    create = models.DateTimeField(_("Create"), auto_now_add=True)
    update = models.DateTimeField(_("Update"), auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(_("Category Name"), max_length=50)

    def __str__(self) -> str:
        return self.name


class Product(BaseModel):
    name = models.CharField(_("Product Name"), max_length=200)
    description = models.TextField(_("Description"))
    category = models.ForeignKey(Category, verbose_name=_("Product Category"), on_delete=models.CASCADE,related_name="products")
    image = models.ImageField(_("Product Image"), upload_to='product', null=True, blank=True)
    selling_price = models.DecimalField(_("Selling Price"), max_digits=5, decimal_places=2)
    purches_price = models.DecimalField(_("Purches Price"), max_digits=5, decimal_places=2)
    
    def __str__(self) -> str:
        return self.name