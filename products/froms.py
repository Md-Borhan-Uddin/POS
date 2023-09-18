from django import forms
from core.forms import BaseModalForm
from products.models import Product


class ProductForm(BaseModalForm):


    class Meta:
        model = Product
        exclude = ('create','update','id')

        widgets = {
            'description':forms.Textarea(attrs={
                'rows':3
            }),
            'image': forms.FileInput(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full'
            })
        }