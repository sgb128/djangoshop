from django.urls import path
from .views import OrderList, OrderCreate#, order_forming_complete, OrderRead, OrderItemsUpdate, OrderDelete


app_name = 'ordersapp'

urlpatterns = [
    path('', OrderList.as_view(), name='orders_list'),
    # path('forming/complete/<int:pk>/', order_forming_complete, name='order_forming_complete'),
    path('create/', OrderCreate.as_view(), name='order_create'),
    # path('create/<int:pk>/', OrderRead.as_view(), name='order_read'),
    # path('update/<int:pk>/', OrderItemsUpdate.as_view(), name='order_update'),
    # path('create/<int:pk>/', OrderDelete.as_view(), name='order_delate'),
]
