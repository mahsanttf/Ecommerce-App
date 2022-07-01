from django.db import transaction
from django.urls import reverse
from django.views import generic
from .models import Vendor, Stock
from product.models import Products


class VendorListView(generic.ListView):
    model = Vendor
    template_name = 'inventory/vendor.html'


class VendorCreateView(generic.CreateView):
    model = Vendor
    fields = [
        'name', 'address', 'phone_number',
    ]

    def get_success_url(self):
        return reverse('inventory:vendor_list')


class StockListView(generic.ListView):
    model = Stock
    template_name = 'inventory/stock.html'


class StockCreateView(generic.CreateView):
    model = Stock
    fields = [
        'vendor', 'products', 'quantity', 'total_price',
    ]

    def get_success_url(self):
        return reverse('inventory:stock_list')

    @transaction.atomic
    def form_valid(self, form):
        resp = super().form_valid(form)
        product = self.object.products
        product.quantity += self.object.quantity
        product.save()
        return resp
