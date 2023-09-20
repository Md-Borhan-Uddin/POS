
from typing import Any
from django.db.models import Q
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView,TemplateView, CreateView, UpdateView,DeleteView
from django.core.exceptions import ImproperlyConfigured
from django.utils import timezone



from inventory.models import SaleProduct,Store,Purches,SalesInvoice
from inventory.forms import SalesForm, PurchesForm


class TemplateMixin(TemplateView):
    template_name = None
    modal = None
    form = None
    update_url = None
    create_url = None

    def get(self, request, *args, **kwargs):
        if not self.template_name:
            raise ImproperlyConfigured('template name not set')
        if not self.modal:
            raise ImproperlyConfigured('modal not set')
        
        return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if kwargs.get('pk'):
            if not self.update_url:
                raise ImproperlyConfigured('update url not set')
        
            obj = self.modal.objects.get(id=kwargs.get('pk'))
            context['form'] = self.form(instance=obj)
            context['is_update'] = True
            context['url'] = reverse_lazy(self.update_url,kwargs={'pk':obj.pk})
        else:
            context['form'] = self.form()
            context['is_update'] = False
            if not self.create_url:
                raise ImproperlyConfigured('create url not set')
        
            context['url'] = reverse_lazy(self.create_url)
        return context



class SaleFormView(TemplateMixin):
    template_name = "inventory/sale/form.html"
    modal = SaleProduct
    form = SalesForm
    create_url = 'inventory:sale_create'
    update_url = 'inventory:sale_update'
    

    


class ProductTableView(TemplateView):
    template_name = "product/product_table.html"


    



class SaleListView(ListView):
    model = SaleProduct
    template_name = "inventory/sale/sales.html"
    context_object_name = 'sales'
    paginate_by = 10

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SalesForm()
        context['url'] = reverse_lazy('inventory:sale_create')
        return context


class SaleCreateView(View):
    model = SaleProduct
    success_url = reverse_lazy('inventory:sales')
    form_class = SalesForm
    template_name = "inventory/sale/sales.html"

    
    
    
    
    def get_invoice_number(self):
        id = 0
        try:
            id = SaleProduct.objects.last().pk
        except:
            id = 1
        return timezone.now().strftime('%Y%m%d')+str(id)
    

    def get(self,request,*args, **kwargs):
        context = {
            'form':self.form_class()
        }
        return render(request,self.template_name,context)
    
    def post(self, request,in_no=None, *args, **kwargs):
        
        invoice = None
        form = self.form_class(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            price = sale.product.selling_price*sale.quantity
            if sale.offer:
                sale.total = price - sale.offer
            else:
                sale.total = price
            sale.save()
            if in_no:
                invoice = SalesInvoice.objects.get(
                    invoice_no = in_no
                )
            else:
                invoice = SalesInvoice.objects.create(
                    invoice_no = self.get_invoice_number(),
                    seller = request.user
                    
                )
            invoice.sale_product.add(sale)
            context = {
                'form':self.form_class(),
                'invoice': invoice
            }
        else:
            context = {
                'form':form,
                'invoice': invoice
            }  
        
        return render(request,'inventory/sale/body.html',context)
    
   
    
    


class SaleUpdateView(UpdateView):
    model = SaleProduct
    form_class = SalesForm
    success_url = reverse_lazy('inventory:sales')

    def form_valid(self, form):
        form.instance.total = form.instance.quantity*form.instance.product.selling_price
        form.save()
        return super().form_valid(form)
    


class ProductDeleteView(DeleteView):
    model = SaleProduct
    success_url = reverse_lazy('products:list')
    template_name = 'product/product_table.html'

    def get(self, request, *args, **kwargs):
        self.delete(request)
        return render(request,self.template_name,{'products':SaleProduct.objects.all()})