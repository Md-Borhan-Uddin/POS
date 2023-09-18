from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _

# Create your models here.

class BaseModel(models.Model):
    create = models.DateTimeField(_("Create"), auto_now_add=True)
    update = models.DateTimeField(_("Update"), auto_now=True)


class Purches(BaseModel):
    product = models.ForeignKey("products.Product", verbose_name=_("Product"), on_delete=models.CASCADE,related_name='purches')
    quantity = models.PositiveSmallIntegerField('Quantity')
    offer = models.PositiveIntegerField(_("Offer"), null=True, blank=True)
    total = models.PositiveIntegerField(_("Total"))

    def __str__(self):
        return self.product.name
    
    def total(self):
        price = self.product.purches_price*self.quantity
        if self.offer:
            return price
        return price-self.offer 



class SaleProduct(BaseModel):
    product = models.ForeignKey("products.Product", verbose_name=_("Product"), on_delete=models.CASCADE,related_name='sales')
    quantity = models.PositiveSmallIntegerField('Quantity')
    offer = models.PositiveIntegerField(_("Offer"), null=True, blank=True)
    total = models.PositiveIntegerField(_("Total"))

    def __str__(self):
        return self.product.name
    
    def total(self):
        price = self.product.selling_price*self.quantity
        if self.offer:
            return price
        return price-self.offer    



class Store(BaseModel):
    product = models.OneToOneField("products.Product", verbose_name=_("Product"), on_delete=models.CASCADE,related_name='store')
    purches_quentity = models.PositiveIntegerField(_("Purches"))
    sales_quentity = models.PositiveIntegerField(_("Sales"))

    def __str__(self):
        return self.product.name
    
    # def total_sale(self):
    #     self.product.sales.annotation(total = sum('total'))
    #     return 



class SalesInvoice(BaseModel):
    sale_product = models.OneToOneField(SaleProduct, verbose_name=_("Product"), on_delete=models.CASCADE,related_name='sale_product')
    phone = models.CharField(_("Phone Number"), max_length=15)
    address = models.CharField(_("Address"), max_length=200,null=True,blank=True)
    seller = models.ForeignKey("accounts.User", verbose_name=_("Seller"), on_delete=models.CASCADE,related_name='sale_invoice')
    offer = models.PositiveIntegerField(_("Offer"), null=True, blank=True)
    is_pay = models.BooleanField(_("Payment Status"))

    def grand_total(self):
        total = self.sale_product.annotation(total=Sum('total')).values('total')
        print(total)
        return total
