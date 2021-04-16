from django.conf.urls import url
from django.urls import path
from .views import simpleCheckout

urlpatterns = [ 
    path('', simpleCheckout, name='checkout'),
    path('simple-checkout/', simpleCheckout, name='simple-checkout'),

]

app_name = 'checkout'