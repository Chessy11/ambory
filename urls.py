from django.conf.urls import url
from django.urls import path

from .views import ProductDetailSlugView, ProductDetailSlugView, ProductListView


urlpatterns = [
    path('products/', ProductListView.as_view(), name='list'),
    path('products/<slug:slug>/', ProductDetailSlugView.as_view(), name='detail')

]

app_name = 'products'