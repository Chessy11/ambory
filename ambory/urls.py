"""ambory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from .views import home_page, about_page, contact_page, login_page, register_page
from products.views import ProductListView, product_list_view
# from carts.views import cart_home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    
    path('products-fbv', product_list_view),
    path('products/', include("products.urls", namespace='products')),
    path('contact/', contact_page, name='contact'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('about/', about_page, name='about'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('search/', include("search.urls", namespace='search')),
    # path('cart/', cart_home, name='cart'),
    path('cart/', include("carts.urls", namespace='cart')),
    path('checkout/', include("checkout.urls", namespace='checkout')),
    ]
   
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)