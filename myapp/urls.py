from django.urls import path
from .views import *

urlpatterns = [
    path('api/customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/orders/', OrderListCreateView.as_view(), name='order-list-create'),
]



