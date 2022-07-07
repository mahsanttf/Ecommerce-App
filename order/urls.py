from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('order/', views.OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('add_order/', views.OrderCreateView.as_view(), name='order_create'),
]