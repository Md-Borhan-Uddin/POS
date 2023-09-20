from django.urls import path
from inventory.views import(
    SaleListView, SaleCreateView,SaleFormView,
    SaleUpdateView
)


app_name = 'inventory'

urlpatterns = [
    path('sales/',SaleListView.as_view(),name='sales'),
    path('sales/create/',SaleCreateView.as_view(),name='sale_create'),
    path('sales/create/<str:in_no>/',SaleCreateView.as_view(),name='sale_create_invoice'),
    path('sales/<int:pk>/update/',SaleUpdateView.as_view(),name='sale_update'),
    path('sales/form/',SaleFormView.as_view(),name='sale_form'),
    path('sales/form/<int:pk>/',SaleFormView.as_view(),name='sale_update_form'),
]
