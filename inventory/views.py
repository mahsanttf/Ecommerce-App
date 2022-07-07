from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from .models import Vendor, Stock


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

    def get_queryset(self):
        super().get_queryset()
        order_by = self.request.GET.get('order_by')
        direction = self.request.GET.get('direction')
        if direction:
            if direction == 'asc':
                ordering = '{}'.format(order_by)
                stock = Stock.objects.all().order_by(ordering)
            else:
                ordering = '-{}'.format(order_by)
                stock = Stock.objects.all().order_by(ordering)
        else:
            stock = Stock.objects.all()
        return stock

# def get_queryset(self):
#     queryset = super(StockListView, self).get_queryset()
#     queryset = queryset.order_by('-total_price')
#     return queryset


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


# def create_session(request):
#     request.session['name'] = 'ahsan'
#     request.session['email'] = 'ahsanttf@hotmail.com'
#     return HttpResponse('<h1>New Session is set</h1>')
#
#
# def get_session(request):
#     my_name = request.session['name']
#     my_email = request.session['email']
#     return HttpResponse('Name: '+my_name+'<br>'+'Email: '+my_email)
#
#
# def delete_session(request):
#     try:
#         del request.session['name']
#         del request.session['email']
#     except KeyError:
#         pass
#     return HttpResponse("<h1>Session Data cleared</h1>")
#
#
# def cookie_session(request):
#     request.session.set_test_cookie()
#     return HttpResponse("<h1>New Cookie Created</h1>")
#
#
# def cookie_delete(request):
#     if request.session.test_cookie_worked():
#         request.session.delete_test_cookie()
#         response = HttpResponse("<h1>Cookie Deleted</h1>")
#     else:
#         response = HttpResponse("<h1>No Cookie Present</h1>")
#     return response


