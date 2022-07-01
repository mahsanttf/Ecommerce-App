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
]