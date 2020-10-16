from django.urls import path
from .views import *

urlpatterns = [
   path('',homeView,name='home_url'),
   path('products/',productView,name='product_url'),
   path('customers/',customerView,name='customer_url'),
]