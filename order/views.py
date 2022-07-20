from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Orders, OrderDetails


class OrderListView(generic.ListView):
    model = Orders
    template_name = 'order/orders.html'

    def get_queryset(self):
        super().get_queryset()
        order_by = self.request.GET.get('order_by')
        direction = self.request.GET.get('direction')
        order = Orders.objects.all()
        if direction:
            if direction == 'asc':
                ordering = '{}'.format(order_by)
            else:
                ordering = '-{}'.format(order_by)
            order = order.order_by(ordering)
        return order


class OrderCreateView(generic.CreateView):
    model = Orders
    fields = [
        'name',
    ]

    def get_success_url(self):
        return reverse('order:order_list')


class OrderDetailView(generic.DetailView):
    model = Orders
    template_name = 'order/orderdetails.html'

    def dispatch(self, request, *args, **kwargs):
        obj = get_object_or_404(Orders, pk=self.kwargs['pk'])
        if self.request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        else:
            if self.request.user.username == obj.name:
                return super().dispatch(request, *args, **kwargs)
            else:
                raise Http404
