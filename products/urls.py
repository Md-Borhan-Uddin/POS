from django.urls import path
from products.views import (
    ProductListView,ProductCreateView,
    ProductUpdateView,ProductDeleteView,
    ProductFormView,ProductTableView
)

app_name = 'products'

urlpatterns = [
    path("product-form/<int:pk>/", ProductFormView.as_view(), name="product_update_form"),
    path("product-form/", ProductFormView.as_view(), name="product_form"),
    path("product-table/", ProductTableView.as_view(), name="product_table"),
    path("", ProductListView.as_view(), name="list"),
    path("create/", ProductCreateView.as_view(), name="create"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="delete"),
]
