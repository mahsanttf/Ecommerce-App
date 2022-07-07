from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from .models import Products, Brand, Category
from .Cart import Cart


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

    def get_queryset(self):
        super(ProductListView, self).get_queryset()
        order_by = self.request.GET.get('order_by')
        direction = self.request.GET.get('direction')
        if direction:
            if direction == 'asc':
                ordering = '{}'.format(order_by)
                product = Products.objects.all().order_by(ordering)
            else:
                ordering = '-{}'.format(order_by)
                product = Products.objects.all().order_by(ordering)
        else:
            product = Products.objects.all()
        return product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['cart_total'] = Cart(self.request).get_total()
        return context


class ProductCreateView(generic.CreateView):
    model = Products
    fields = [
        'brand', 'category', 'name', 'code', 'price', 'image',
    ]

    def get_success_url(self):
        return reverse('product:product_list')


def cart_add(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product)
    return redirect("product:product_list")


def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product)
    return redirect("product:product_list")


def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("product:product_list")


def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("product:product_list")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("product:product_list")

