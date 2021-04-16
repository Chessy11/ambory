from django.shortcuts import render
from django.http import JsonResponse	
import json
from carts.models import Cart
from products.models import Product 

def simpleCheckout(request):
	return render(request, 'checkout/simple_checkout.html')
