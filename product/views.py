from django.urls import reverse
from django.views import generic
from .models import Products, Brand, Category


class BrandListView(generic.ListView):
    model = Brand
    template_name = 'product/brand.html'


class BrandCreateView(generic.CreateView):
    model = Brand
    fields = [
        'name',
    ]

    def get_success_url(self):
        return reverse('product:brand_list')


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'product/category.html'


class CategoryCreateView(generic.CreateView):
    model = Category
    fields = [
        'name',
    ]

    def get_success_url(self):
        return reverse('product:category_list')


class ProductListView(generic.ListView):
    model = Products
    template_name = 'product/products.html'


class ProductCreateView(generic.CreateView):
    model = Products
    fields = [
        'brand', 'category', 'name', 'code', 'price', 'image',
    ]

    def get_success_url(self):
        return reverse('product:product_list')

