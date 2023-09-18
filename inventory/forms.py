from core.forms import BaseModalForm
from inventory.models import SaleProduct,Purches


class SalesForm(BaseModalForm):

    class Meta:
        model = SaleProduct
        fields = ('product','quantity','offer')




class PurchesForm(BaseModalForm):

    class Meta:
        model = Purches
        fields = ('product','quantity','offer')