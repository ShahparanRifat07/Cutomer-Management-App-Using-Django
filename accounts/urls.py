from django.urls import path
from .views import *

urlpatterns = [
   path('',homeView,name='home_url'),
   path('products/',productView,name='product_url'),
   path('customers/<int:pk>/',customerView,name='customer_url'),
   path('create_order/',createOrder,name='create_order_url'),
   path('update_order/<int:pk>/',updateOrder,name='update_order_url'),
   path('delete_order/<int:pk>',deleteOrder,name='delete_order_url'),
]