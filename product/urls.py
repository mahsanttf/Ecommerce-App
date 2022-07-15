from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('brand/', views.BrandListView.as_view(), name='brand_list'),
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('add_product/', views.ProductCreateView.as_view(), name='product_create'),
    path('add_brand/', views.BrandCreateView.as_view(), name='brand_create'),
    path('add_category/', views.CategoryCreateView.as_view(), name='category_create'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/check_out/', views.check_out, name='check_out'),
    path('cart/', views.CartView.as_view(), name='cart_view'),
    path('accounts/signup', views.SignUpView.as_view(), name='signup'),
]
