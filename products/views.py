from typing import Any
from django.db.models import Q
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView,TemplateView, CreateView, UpdateView,DeleteView
from products.froms import ProductForm
from django.views.generic.edit import BaseDeleteView



from products.models import Product



class ProductFormView(TemplateView):
    template_name = "product/product_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if kwargs.get('pk'):
            product = Product.objects.get(id=kwargs.get('pk'))
            context['form'] = ProductForm(instance=product)
            context['is_update'] = True
            context['url'] = reverse_lazy('products:update',kwargs={'pk':product.pk})
        else:
            context['form'] = ProductForm()
            context['is_update'] = False
            context['url'] = reverse_lazy('products:create')
        return context


class ProductTableView(TemplateView):
    template_name = "product/product_table.html"


    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(
            Q(name__icontains=query)
        )
        context['products'] = products

        return context



class ProductListView(ListView):
    model = Product
    template_name = "product/list.html"
    context_object_name = 'products'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductForm()
        context['url'] = reverse_lazy('products:create')
        return context


class ProductCreateView(CreateView):
    model = Product
    success_url = reverse_lazy('products:list')
    form_class = ProductForm


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product/list.html"
    success_url = reverse_lazy('products:list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:list')
    template_name = 'product/product_table.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.delete(request)
        return render(request,self.template_name,{'products':Product.objects.all()})