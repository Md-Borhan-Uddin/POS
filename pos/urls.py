
from django.contrib import admin
from django.urls import path, include
from pos.settings import base
from pos import dev_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include('accounts.urls',namespace='accounts')),
    path("", include('core.urls',namespace='core')),
    path("product/", include('products.urls',namespace='products')),
    path("inventory/", include('inventory.urls',namespace='inventory')),
]

if base.DEBUG:
    urlpatterns += dev_urls.urlpatterns
